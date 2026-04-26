from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from PalDefender import (
    GiveItem,
    GivePal,
    GivePalEgg,
    GiveProgressionRequest,
    PalDefenderApiError,
    RESTClient,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Full example CLI for the PalDefender REST client.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("version", help="Fetch server version.")
    subparsers.add_parser("guilds", help="List guilds.")
    subparsers.add_parser("players", help="List players.")

    guild_parser = subparsers.add_parser("guild", help="Fetch one guild.")
    guild_parser.add_argument("guild_id", help="Guild identifier.")

    for command_name, help_text in (
        ("player", "Fetch one player."),
        ("pals", "Fetch pal data for a player."),
        ("items", "Fetch inventory data for a player."),
        ("techs", "Fetch technology data for a player."),
        ("progression", "Fetch progression data for a player."),
    ):
        player_parser = subparsers.add_parser(command_name, help=help_text)
        player_parser.add_argument("player_identifier", help="Player UID or user ID.")

    give_items_parser = subparsers.add_parser("give-items", help="Grant items to a player.")
    give_items_parser.add_argument("player_identifier", help="Player UID or user ID.")
    give_items_parser.add_argument(
        "payload",
        help='JSON array or "@path/to/file.json". Example: \'[{"ItemID":"Stone","Count":100}]\'',
    )

    give_pals_parser = subparsers.add_parser("give-pals", help="Grant pals to a player.")
    give_pals_parser.add_argument("player_identifier", help="Player UID or user ID.")
    give_pals_parser.add_argument(
        "payload",
        help='JSON array or "@path/to/file.json". Example: \'[{"PalID":"Lamball","Level":10}]\'',
    )

    pal_templates_parser = subparsers.add_parser(
        "give-pal-templates",
        help="Grant pal templates to a player.",
    )
    pal_templates_parser.add_argument("player_identifier", help="Player UID or user ID.")
    pal_templates_parser.add_argument(
        "templates",
        nargs="+",
        help="Template names such as starter_build or shadowfox.json.",
    )

    give_pal_eggs_parser = subparsers.add_parser("give-pal-eggs", help="Grant pal eggs to a player.")
    give_pal_eggs_parser.add_argument("player_identifier", help="Player UID or user ID.")
    give_pal_eggs_parser.add_argument(
        "payload",
        help=(
            'JSON array or "@path/to/file.json". Example: '
            '\'[{"EggID":"PalEgg_Dark","PalID":"Foxparks","Level":8}]\''
        ),
    )

    give_progression_parser = subparsers.add_parser(
        "give-progression",
        help="Grant progression values to a player.",
    )
    give_progression_parser.add_argument("player_identifier", help="Player UID or user ID.")
    give_progression_parser.add_argument(
        "payload",
        help=(
            'JSON object or "@path/to/file.json". Example: '
            '\'{"EXP":1000,"TechnologyPoints":5}\''
        ),
    )

    for command_name, help_text in (
        ("learn-tech", "Unlock one or more technologies."),
        ("forget-tech", "Forget one or more technologies."),
    ):
        tech_parser = subparsers.add_parser(command_name, help=help_text)
        tech_parser.add_argument("player_identifier", help="Player UID or user ID.")
        tech_parser.add_argument(
            "technology",
            nargs="+",
            help='One or more technology ids, or a single "All".',
        )

    return parser


def load_settings(env_path: Path) -> dict[str, Any]:
    load_dotenv(env_path)

    base_url = os.getenv("PALDEFENDER_BASE_URL", "").strip()
    bearer_token = os.getenv("PALDEFENDER_BEARER_TOKEN", "").strip()
    display_address = os.getenv("PALDEFENDER_DISPLAY_ADDRESS", "").strip() or None
    timeout_raw = os.getenv("PALDEFENDER_TIMEOUT", "30").strip()

    if not base_url:
        raise ValueError(f"PALDEFENDER_BASE_URL is required in {env_path}")
    if not bearer_token:
        raise ValueError(f"PALDEFENDER_BEARER_TOKEN is required in {env_path}")

    try:
        timeout = float(timeout_raw)
    except ValueError as exc:
        raise ValueError("PALDEFENDER_TIMEOUT must be a number") from exc

    return {
        "base_url": base_url,
        "bearer_token": bearer_token,
        "display_address": display_address,
        "timeout": timeout,
    }


def load_json_argument(raw_value: str) -> Any:
    if raw_value.startswith("@"):
        json_path = Path(raw_value[1:]).expanduser()
        content = json_path.read_text(encoding="utf-8")
    else:
        content = raw_value

    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON payload: {exc}") from exc


def parse_items(payload: str) -> list[GiveItem | dict[str, Any]]:
    value = load_json_argument(payload)
    if not isinstance(value, list):
        raise ValueError("give-items payload must be a JSON array")
    return [
        GiveItem(item["ItemID"], item["Count"]) if isinstance(item, dict) and {"ItemID", "Count"} <= item.keys() else item
        for item in value
    ]


def parse_pals(payload: str) -> list[GivePal | dict[str, Any]]:
    value = load_json_argument(payload)
    if not isinstance(value, list):
        raise ValueError("give-pals payload must be a JSON array")
    return [
        GivePal(pal["PalID"], pal["Level"]) if isinstance(pal, dict) and {"PalID", "Level"} <= pal.keys() else pal
        for pal in value
    ]


def parse_pal_eggs(payload: str) -> list[GivePalEgg | dict[str, Any]]:
    value = load_json_argument(payload)
    if not isinstance(value, list):
        raise ValueError("give-pal-eggs payload must be a JSON array")

    parsed: list[GivePalEgg | dict[str, Any]] = []
    for egg in value:
        if isinstance(egg, dict) and "EggID" in egg:
            parsed.append(
                GivePalEgg(
                    egg_id=egg["EggID"],
                    pal_id=egg.get("PalID"),
                    pal_template=egg.get("PalTemplate"),
                    level=egg.get("Level"),
                )
            )
        else:
            parsed.append(egg)
    return parsed


def parse_progression(payload: str) -> GiveProgressionRequest | dict[str, Any]:
    value = load_json_argument(payload)
    if not isinstance(value, dict):
        raise ValueError("give-progression payload must be a JSON object")

    known_fields = {
        "EXP": "exp",
        "Lifmunks": "lifmunks",
        "TechnologyPoints": "technology_points",
        "AncientTechnologyPoints": "ancient_technology_points",
    }
    if set(value).issubset(known_fields):
        return GiveProgressionRequest(
            **{known_fields[key]: value[key] for key in value}
        )
    return value


def technology_argument(values: list[str]) -> str | list[str]:
    if len(values) == 1:
        return values[0]
    return values


def print_json(data: Any) -> None:
    print(json.dumps(data, indent=2, sort_keys=True))


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    example_dir = Path(__file__).resolve().parent
    env_path = example_dir / ".env"

    try:
        settings = load_settings(env_path)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    try:
        with RESTClient(**settings) as client:
            if args.command == "version":
                result = client.version()
            elif args.command == "guilds":
                result = client.guilds()
            elif args.command == "guild":
                result = client.guild(args.guild_id)
            elif args.command == "players":
                result = client.players()
            elif args.command == "player":
                result = client.player(args.player_identifier)
            elif args.command == "pals":
                result = client.pals(args.player_identifier)
            elif args.command == "items":
                result = client.items(args.player_identifier)
            elif args.command == "techs":
                result = client.techs(args.player_identifier)
            elif args.command == "progression":
                result = client.progression(args.player_identifier)
            elif args.command == "give-items":
                result = client.give_items(args.player_identifier, parse_items(args.payload))
            elif args.command == "give-pals":
                result = client.give_pals(args.player_identifier, parse_pals(args.payload))
            elif args.command == "give-pal-templates":
                result = client.give_pal_templates(args.player_identifier, args.templates)
            elif args.command == "give-pal-eggs":
                result = client.give_pal_eggs(args.player_identifier, parse_pal_eggs(args.payload))
            elif args.command == "give-progression":
                result = client.give_progression(args.player_identifier, parse_progression(args.payload))
            elif args.command == "learn-tech":
                result = client.learn_tech(args.player_identifier, technology_argument(args.technology))
            elif args.command == "forget-tech":
                result = client.forget_tech(args.player_identifier, technology_argument(args.technology))
            else:
                parser.error(f"Unsupported command: {args.command}")
                return 2
    except (ValueError, OSError) as exc:
        print(exc, file=sys.stderr)
        return 2
    except PalDefenderApiError as exc:
        print(f"{exc.method} {exc.path} failed with {exc.status_code}", file=sys.stderr)
        if exc.response_body is not None:
            print_json(exc.response_body)
        return 1

    print_json(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
