"""Synchronous PalDefender REST API client."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any
from urllib.parse import quote, urlsplit, urlunsplit

import requests

from .errors import PalDefenderApiError
from .models import (
    GiveItem,
    GivePal,
    GivePalEgg,
    GiveProgressionRequest,
    GuildDetail,
    GuildsResponse,
    PlayerInfo,
    PlayerItemsResponse,
    PlayerPalsResponse,
    PlayerProgressionResponse,
    PlayerTechsResponse,
    PlayersResponse,
    VersionInfo,
)
from .pal_constants import ItemId, get_recipe_materials as resolve_recipe_materials
from .pal_constants import PalId, TechnologyId

JsonValue = dict[str, Any] | list[Any] | str | int | float | bool | None
ItemInput = str | tuple[str, int] | GiveItem | dict[str, Any]
PalInput = str | PalId | tuple[str | PalId, int] | GivePal | dict[str, Any]
PalEggTupleInput = tuple[str, str | PalId] | tuple[str, str | PalId, int]
PalEggInput = GivePalEgg | dict[str, Any] | PalEggTupleInput
TechnologyInput = str | TechnologyId | Sequence[str | TechnologyId]


class RESTClient:
    """Client for the PalDefender REST API."""

    def __init__(
        self,
        base_url: str,
        bearer_token: str,
        *,
        timeout: float = 30.0,
        display_address: str | None = None,
        session: requests.Session | None = None,
    ) -> None:
        if not base_url:
            raise ValueError("base_url must not be empty")
        if not bearer_token:
            raise ValueError("bearer_token must not be empty")

        self.base_url = self._normalize_base_url(base_url)
        self.timeout = timeout
        self.session = session or requests.Session()
        self.session.headers.setdefault("Authorization", f"Bearer {bearer_token}")
        self.session.headers.setdefault("Accept", "application/json")
        if display_address:
            self.session.headers.setdefault("DisplayAddress", display_address)

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "RESTClient":
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.close()

    def get_version(self) -> VersionInfo:
        return VersionInfo.from_dict(self._request_json("GET", "/v1/pdapi/version"))

    def get_guilds(self) -> GuildsResponse:
        return GuildsResponse.from_dict(self._request_json("GET", "/v1/pdapi/guilds"))

    def get_guild(self, guild_id: str) -> GuildDetail:
        return GuildDetail.from_dict(self._request_json("GET", f"/v1/pdapi/guild/{self._path_part(guild_id)}"))

    def get_players(self) -> PlayersResponse:
        return PlayersResponse.from_list(self._request_json("GET", "/v1/pdapi/items/players"))

    def get_player(self, player_identifier: str) -> PlayerInfo:
        return PlayerInfo.from_dict(
            self._request_json("GET", f"/v1/pdapi/items/player/{self._path_part(player_identifier)}")
        )

    def get_pals(self, player_identifier: str) -> PlayerPalsResponse:
        return PlayerPalsResponse.from_dict(
            self._request_json("GET", f"/v1/pdapi/items/pals/{self._path_part(player_identifier)}")
        )

    def get_items(self, player_identifier: str) -> PlayerItemsResponse:
        return PlayerItemsResponse.from_dict(
            self._request_json("GET", f"/v1/pdapi/items/{self._path_part(player_identifier)}")
        )

    def get_techs(self, player_identifier: str) -> PlayerTechsResponse:
        return PlayerTechsResponse.from_dict(
            self._request_json("GET", f"/v1/pdapi/techs/{self._path_part(player_identifier)}")
        )

    def get_progression(self, player_identifier: str) -> PlayerProgressionResponse:
        return PlayerProgressionResponse.from_dict(
            self._request_json("GET", f"/v1/pdapi/progression/{self._path_part(player_identifier)}")
        )

    def version(self) -> VersionInfo:
        return self.get_version()

    def guilds(self) -> GuildsResponse:
        return self.get_guilds()

    def guild(self, guild_id: str) -> GuildDetail:
        return self.get_guild(guild_id)

    def players(self) -> PlayersResponse:
        return self.get_players()

    def player(self, player_identifier: str) -> PlayerInfo:
        return self.get_player(player_identifier)

    def pals(self, player_identifier: str) -> PlayerPalsResponse:
        return self.get_pals(player_identifier)

    def items(self, player_identifier: str) -> PlayerItemsResponse:
        return self.get_items(player_identifier)

    def techs(self, player_identifier: str) -> PlayerTechsResponse:
        return self.get_techs(player_identifier)

    def progression(self, player_identifier: str) -> PlayerProgressionResponse:
        return self.get_progression(player_identifier)

    def give_items(
        self,
        player_identifier: str,
        *items: ItemInput,
    ) -> JsonValue:
        normalized_items = self._normalize_item_inputs(items)
        payload = {"Items": [self._serialize_entry(item) for item in normalized_items]}
        return self._request("POST", f"/v1/pdapi/give/items/{self._path_part(player_identifier)}", json=payload)

    def give_pals(
        self,
        player_identifier: str,
        *pals: PalInput,
    ) -> JsonValue:
        normalized_pals = self._normalize_pal_inputs(pals)
        payload = {"Pals": [self._serialize_entry(pal) for pal in normalized_pals]}
        return self._request("POST", f"/v1/pdapi/give/pals/{self._path_part(player_identifier)}", json=payload)

    def give_pal_templates(
        self,
        player_identifier: str,
        *templates: str | Sequence[str],
    ) -> JsonValue:
        normalized_templates = self._normalize_string_inputs(templates, label="templates")
        return self._request(
            "POST",
            f"/v1/pdapi/give/paltemplate/{self._path_part(player_identifier)}",
            json={"PalTemplates": normalized_templates},
        )

    def give_pal_eggs(
        self,
        player_identifier: str,
        *pal_eggs: PalEggInput,
    ) -> JsonValue:
        normalized_pal_eggs = self._normalize_pal_egg_inputs(pal_eggs)
        payload = {"PalEggs": [self._serialize_entry(pal_egg) for pal_egg in normalized_pal_eggs]}
        return self._request("POST", f"/v1/pdapi/give/paleggs/{self._path_part(player_identifier)}", json=payload)

    def give_recipe_materials(
        self,
        player_identifier: str,
        product: ItemId | str,
        *,
        quantity: int = 1,
    ) -> JsonValue:
        if quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        recipe_materials = resolve_recipe_materials(product)
        if recipe_materials is None:
            raise ValueError(f"No recipe found for product {product!r}")

        items: list[GiveItem] = []
        for material_id, count in recipe_materials.items():
            if not isinstance(material_id, ItemId):
                raise ValueError(
                    f"Recipe for {product!r} includes non-item material {material_id!r}, "
                    "which cannot be granted through give_items."
                )
            items.append(GiveItem(item_id=material_id.value, count=count * quantity))

        return self.give_items(player_identifier, *items)

    def give_progression(
        self,
        player_identifier: str,
        request: GiveProgressionRequest | dict[str, Any] | None = None,
        *,
        exp: int | None = None,
        lifmunks: int | None = None,
        technology_points: int | None = None,
        ancient_technology_points: int | None = None,
    ) -> JsonValue:
        payload = self._normalize_progression_request(
            request=request,
            exp=exp,
            lifmunks=lifmunks,
            technology_points=technology_points,
            ancient_technology_points=ancient_technology_points,
        )
        return self._request(
            "POST",
            f"/v1/pdapi/give/progression/{self._path_part(player_identifier)}",
            json=self._serialize_entry(payload),
        )

    def learn_tech(
        self,
        player_identifier: str,
        *technology: TechnologyInput,
    ) -> JsonValue:
        return self._request(
            "POST",
            f"/v1/pdapi/learntech/{self._path_part(player_identifier)}",
            json={"Technology": self._technology_payload(*technology)},
        )

    def forget_tech(
        self,
        player_identifier: str,
        *technology: TechnologyInput,
    ) -> JsonValue:
        return self._request(
            "POST",
            f"/v1/pdapi/forgettech/{self._path_part(player_identifier)}",
            json={"Technology": self._technology_payload(*technology)},
        )

    def delete_base(self, base_camp_identifier: str) -> JsonValue:
        return self._request("POST", f"/v1/pdapi/deletebase/{self._path_part(base_camp_identifier)}")

    @staticmethod
    def _serialize_entry(value: Any) -> Any:
        if hasattr(value, "to_dict"):
            return value.to_dict()
        return value

    @classmethod
    def _normalize_item_inputs(cls, values: Sequence[ItemInput]) -> list[GiveItem | dict[str, Any]]:
        values = cls._flatten_single_sequence(values, cls._looks_like_item_tuple)

        counts: dict[str, int] = {}
        passthrough: list[dict[str, Any]] = []

        for value in values:
            if isinstance(value, str):
                counts[value] = counts.get(value, 0) + 1
                continue
            if isinstance(value, GiveItem):
                counts[value.item_id] = counts.get(value.item_id, 0) + value.count
                continue
            if isinstance(value, tuple):
                if len(value) != 2:
                    raise ValueError("item tuples must contain exactly (item_id, count)")
                item_id, count = value
                if not isinstance(item_id, str):
                    raise TypeError("item tuple item_id must be a string")
                if not isinstance(count, int):
                    raise TypeError("item tuple count must be an integer")
                if count <= 0:
                    raise ValueError("item tuple count must be a positive integer")
                counts[item_id] = counts.get(item_id, 0) + count
                continue
            if isinstance(value, dict):
                if {"ItemID", "Count"} <= value.keys():
                    item_id = value["ItemID"]
                    count = value["Count"]
                    if not isinstance(item_id, str):
                        raise TypeError("ItemID must be a string")
                    if not isinstance(count, int):
                        raise TypeError("Count must be an integer")
                    if count <= 0:
                        raise ValueError("Count must be a positive integer")
                    counts[item_id] = counts.get(item_id, 0) + count
                else:
                    passthrough.append(value)
                continue
            raise TypeError("items must be strings, (item_id, count) tuples, GiveItem objects, or dictionaries")

        normalized = [GiveItem(item_id=item_id, count=count) for item_id, count in counts.items()]
        normalized.extend(passthrough)
        if not normalized:
            raise ValueError("at least one item must be provided")
        return normalized

    @classmethod
    def _normalize_pal_inputs(cls, values: Sequence[PalInput]) -> list[GivePal | dict[str, Any]]:
        values = cls._flatten_single_sequence(values, cls._looks_like_pal_tuple)

        normalized: list[GivePal | dict[str, Any]] = []
        for value in values:
            if isinstance(value, PalId):
                normalized.append(GivePal(pal_id=value.value, level=1))
                continue
            if isinstance(value, str):
                normalized.append(GivePal(pal_id=value, level=1))
                continue
            if isinstance(value, GivePal):
                normalized.append(value)
                continue
            if isinstance(value, tuple):
                if len(value) != 2:
                    raise ValueError("pal tuples must contain exactly (pal_id, level)")
                pal_id, level = value
                if isinstance(pal_id, PalId):
                    pal_id = pal_id.value
                if not isinstance(pal_id, str):
                    raise TypeError("pal tuple pal_id must be a string or PalId")
                if not isinstance(level, int):
                    raise TypeError("pal tuple level must be an integer")
                normalized.append(GivePal(pal_id=pal_id, level=level))
                continue
            if isinstance(value, dict):
                if {"PalID", "Level"} <= value.keys():
                    pal_id = value["PalID"]
                    if isinstance(pal_id, PalId):
                        pal_id = pal_id.value
                    normalized.append(GivePal(pal_id=pal_id, level=value["Level"]))
                else:
                    normalized.append(value)
                continue
            raise TypeError("pals must be strings, PalId values, (pal_id, level) tuples, GivePal objects, or dictionaries")

        if not normalized:
            raise ValueError("at least one pal must be provided")
        return normalized

    @classmethod
    def _normalize_pal_egg_inputs(cls, values: Sequence[PalEggInput]) -> list[GivePalEgg | dict[str, Any]]:
        values = cls._flatten_single_sequence(values, cls._looks_like_pal_egg_tuple)

        normalized: list[GivePalEgg | dict[str, Any]] = []
        for value in values:
            if isinstance(value, GivePalEgg):
                normalized.append(value)
                continue
            if isinstance(value, tuple):
                if len(value) not in {2, 3}:
                    raise ValueError("pal egg tuples must be (egg_id, pal_or_template) or (egg_id, pal_or_template, level)")
                egg_id = value[0]
                pal_or_template = value[1]
                level = value[2] if len(value) == 3 else None
                if isinstance(pal_or_template, PalId):
                    normalized.append(GivePalEgg(egg_id=egg_id, pal_id=pal_or_template.value, level=level))
                elif isinstance(pal_or_template, str):
                    if pal_or_template.endswith(".json") or not cls._is_known_pal_id(pal_or_template):
                        normalized.append(GivePalEgg(egg_id=egg_id, pal_template=pal_or_template, level=level))
                    else:
                        normalized.append(GivePalEgg(egg_id=egg_id, pal_id=pal_or_template, level=level))
                else:
                    raise TypeError("pal egg tuple second value must be a string or PalId")
                continue
            if isinstance(value, dict):
                if "EggID" in value:
                    pal_id = value.get("PalID")
                    if isinstance(pal_id, PalId):
                        pal_id = pal_id.value
                    normalized.append(
                        GivePalEgg(
                            egg_id=value["EggID"],
                            pal_id=pal_id,
                            pal_template=value.get("PalTemplate"),
                            level=value.get("Level"),
                        )
                    )
                else:
                    normalized.append(value)
                continue
            raise TypeError("pal eggs must be GivePalEgg objects, dictionaries, or tuples")

        if not normalized:
            raise ValueError("at least one pal egg must be provided")
        return normalized

    @staticmethod
    def _normalize_string_inputs(values: Sequence[str | Sequence[str]], *, label: str) -> list[str]:
        if len(values) == 1 and isinstance(values[0], Sequence) and not isinstance(values[0], (str, bytes, bytearray)):
            values = list(values[0])
        normalized: list[str] = []
        for value in values:
            if not isinstance(value, str):
                raise TypeError(f"{label} entries must be strings")
            normalized.append(value)
        if not normalized:
            raise ValueError(f"at least one {label.rstrip('s')} must be provided")
        return normalized

    @staticmethod
    def _normalize_progression_request(
        *,
        request: GiveProgressionRequest | dict[str, Any] | None,
        exp: int | None,
        lifmunks: int | None,
        technology_points: int | None,
        ancient_technology_points: int | None,
    ) -> GiveProgressionRequest | dict[str, Any]:
        has_keyword_values = any(
            value is not None
            for value in (exp, lifmunks, technology_points, ancient_technology_points)
        )
        if request is not None and has_keyword_values:
            raise ValueError("pass either request or progression keyword arguments, not both")
        if request is not None:
            return request
        return GiveProgressionRequest(
            exp=exp,
            lifmunks=lifmunks,
            technology_points=technology_points,
            ancient_technology_points=ancient_technology_points,
        )

    @staticmethod
    def _looks_like_item_tuple(value: Sequence[Any]) -> bool:
        return len(value) == 2 and isinstance(value[0], str) and isinstance(value[1], int)

    @staticmethod
    def _looks_like_pal_tuple(value: Sequence[Any]) -> bool:
        return len(value) == 2 and isinstance(value[0], (str, PalId)) and isinstance(value[1], int)

    @staticmethod
    def _looks_like_pal_egg_tuple(value: Sequence[Any]) -> bool:
        return (
            len(value) in {2, 3}
            and isinstance(value[0], str)
            and isinstance(value[1], (str, PalId))
            and (len(value) == 2 or isinstance(value[2], int))
        )

    @staticmethod
    def _is_known_pal_id(value: str) -> bool:
        return value in PalId._value2member_map_

    @staticmethod
    def _flatten_single_sequence(values: Sequence[Any], tuple_predicate: Any) -> Sequence[Any]:
        if len(values) == 1 and isinstance(values[0], Sequence) and not isinstance(values[0], (str, bytes, bytearray)):
            nested_values = values[0]
            if not tuple_predicate(nested_values):
                return list(nested_values)
        return values

    @staticmethod
    def _technology_payload(*technology: TechnologyInput) -> str | list[str]:
        flattened = RESTClient._flatten_single_sequence(technology, lambda value: False)
        if not flattened:
            raise ValueError("at least one technology must be provided")

        normalized: list[str] = []
        for value in flattened:
            if isinstance(value, TechnologyId):
                normalized.append(value.value)
                continue
            if isinstance(value, str):
                normalized.append(value)
                continue
            raise TypeError("technology values must be strings or TechnologyId values")

        if len(normalized) == 1:
            return normalized[0]
        if "All" in normalized:
            raise ValueError('"All" is only valid when passed by itself')
        return normalized

    @staticmethod
    def _path_part(value: str) -> str:
        return quote(value, safe="")

    @staticmethod
    def _normalize_base_url(base_url: str) -> str:
        normalized = base_url.rstrip("/")
        parts = urlsplit(normalized)
        if not parts.scheme or not parts.netloc:
            return normalized
        if parts.port is not None:
            return normalized

        hostname = parts.hostname
        if hostname is None:
            return normalized

        netloc = hostname
        if ":" in hostname and not hostname.startswith("["):
            netloc = f"[{hostname}]"
        if parts.username is not None:
            credentials = parts.username
            if parts.password is not None:
                credentials = f"{credentials}:{parts.password}"
            netloc = f"{credentials}@{netloc}"

        return urlunsplit((parts.scheme, f"{netloc}:17993", parts.path, parts.query, parts.fragment))

    def _request(self, method: str, path: str, *, json: Any = None) -> JsonValue:
        response = self.session.request(
            method=method,
            url=f"{self.base_url}{path}",
            json=json,
            timeout=self.timeout,
        )

        data = self._decode_response(response)
        if response.status_code >= 400:
            raise PalDefenderApiError(
                self._error_message(response.status_code, data),
                status_code=response.status_code,
                method=method,
                path=path,
                response_body=data,
            )
        return data

    def _request_json(self, method: str, path: str, *, json: Any = None) -> dict[str, Any] | list[Any]:
        data = self._request(method, path, json=json)
        if not isinstance(data, (dict, list)):
            raise TypeError(f"Expected a JSON object or array from {method} {path}, got {type(data).__name__}")
        return data

    @staticmethod
    def _decode_response(response: requests.Response) -> JsonValue:
        if not response.text:
            return None

        try:
            return response.json()
        except ValueError:
            return response.text

    @staticmethod
    def _error_message(status_code: int, data: JsonValue) -> str:
        if isinstance(data, dict):
            if "Error" in data:
                return f"PalDefender API returned {status_code}: {data['Error']}"
            return f"PalDefender API returned {status_code}: {data}"
        if isinstance(data, str) and data:
            return f"PalDefender API returned {status_code}: {data}"
        return f"PalDefender API returned status {status_code}"
