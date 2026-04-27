from __future__ import annotations

import sys
import unittest
from importlib.util import find_spec
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from PalDefender import (
    GiveItem,
    GivePal,
    GivePalEgg,
    GiveProgressionRequest,
    ItemId,
    PalDefenderApiError,
    PalId,
    RESTClient,
    TechnologyId,
)


class PalDefenderClientTests(unittest.TestCase):
    def test_old_package_is_not_importable(self) -> None:
        self.assertIsNone(find_spec("paldefender_rest_client"))

    def test_get_endpoint_path(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"major":1,"minor":0,"patch":0,"build":5,"version_str":"1.0.0","version_str_long":"1.0.0+5","beta":false}'
        response.json.return_value = {
            "major": 1,
            "minor": 0,
            "patch": 0,
            "build": 5,
            "version_str": "1.0.0",
            "version_str_long": "1.0.0+5",
            "beta": False,
        }
        session.request.return_value = response

        client = RESTClient("http://localhost", "secret", session=session)
        data = client.get_version()

        self.assertEqual(data.version_str, "1.0.0")
        session.request.assert_called_once_with(
            method="GET",
            url="http://localhost:17993/v1/pdapi/version",
            json=None,
            timeout=30.0,
        )

    def test_explicit_port_is_preserved(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"major":1,"minor":0,"patch":0,"build":5,"version_str":"1.0.0","version_str_long":"1.0.0+5","beta":false}'
        response.json.return_value = {
            "major": 1,
            "minor": 0,
            "patch": 0,
            "build": 5,
            "version_str": "1.0.0",
            "version_str_long": "1.0.0+5",
            "beta": False,
        }
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.get_version()

        session.request.assert_called_once_with(
            method="GET",
            url="http://localhost:8212/v1/pdapi/version",
            json=None,
            timeout=30.0,
        )

    def test_post_serializes_item_payload(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"Items":1}}'
        response.json.return_value = {"Granted": {"Items": 1}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_items("player-1", GiveItem("Stone", 50))

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/items/player-1",
            json={"Items": [{"ItemID": "Stone", "Count": 50}]},
            timeout=30.0,
        )

    def test_give_pals_accepts_friendly_inputs(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"Pals":3}}'
        response.json.return_value = {"Granted": {"Pals": 3}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_pals("player-1", PalId.Lamball, (PalId.Foxparks, 5), GivePal("Anubis", 10))

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/pals/player-1",
            json={"Pals": [{"PalID": "SheepBall", "Level": 1}, {"PalID": "Kitsunebi", "Level": 5}, {"PalID": "Anubis", "Level": 10}]},
            timeout=30.0,
        )

    def test_give_pal_templates_accepts_varargs(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"PalTemplates":2}}'
        response.json.return_value = {"Granted": {"PalTemplates": 2}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_pal_templates("player-1", "starter_build", "shadowfox.json")

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/paltemplate/player-1",
            json={"PalTemplates": ["starter_build", "shadowfox.json"]},
            timeout=30.0,
        )

    def test_players_uses_registered_items_prefix_route(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '[{"Name":"A","IP":"127.0.0.1","PlayerUID":"p1","UserId":"u1","GuildName":"G","GuildUUID":"g1","WorldLocation":{"x":1},"MapLocation":{"x":2}}]'
        response.json.return_value = [
            {
                "Name": "A",
                "IP": "127.0.0.1",
                "PlayerUID": "p1",
                "UserId": "u1",
                "GuildName": "G",
                "GuildUUID": "g1",
                "WorldLocation": {"x": 1},
                "MapLocation": {"x": 2},
            }
        ]
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        data = client.get_players()

        self.assertEqual(data.players[0].player_uid, "p1")
        session.request.assert_called_once_with(
            method="GET",
            url="http://localhost:8212/v1/pdapi/items/players",
            json=None,
            timeout=30.0,
        )

    def test_player_uses_registered_items_prefix_route(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Name":"A","IP":"127.0.0.1","PlayerUID":"p1","UserId":"u1","GuildName":"G","GuildUUID":"g1","WorldLocation":{"x":1},"MapLocation":{"x":2}}'
        response.json.return_value = {
            "Name": "A",
            "IP": "127.0.0.1",
            "PlayerUID": "p1",
            "UserId": "u1",
            "GuildName": "G",
            "GuildUUID": "g1",
            "WorldLocation": {"x": 1},
            "MapLocation": {"x": 2},
        }
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        data = client.get_player("player-1")

        self.assertEqual(data.user_id, "u1")
        session.request.assert_called_once_with(
            method="GET",
            url="http://localhost:8212/v1/pdapi/items/player/player-1",
            json=None,
            timeout=30.0,
        )

    def test_pals_uses_registered_items_prefix_route(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"team":{"pal-1":{"PalID":"Lamball","team_slot_index":0}},"palbox":{},"base_camps":[]}'
        response.json.return_value = {
            "team": {"pal-1": {"PalID": "Lamball", "team_slot_index": 0}},
            "palbox": {},
            "base_camps": [],
        }
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        data = client.get_pals("player-1")

        self.assertEqual(data.team["pal-1"].attributes["PalID"], "Lamball")
        session.request.assert_called_once_with(
            method="GET",
            url="http://localhost:8212/v1/pdapi/items/pals/player-1",
            json=None,
            timeout=30.0,
        )

    def test_post_serializes_egg_payload(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"PalEggs":1}}'
        response.json.return_value = {"Granted": {"PalEggs": 1}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_pal_eggs("player-1", [GivePalEgg("PalEgg_Dark", pal_template="shadowfox", level=15)])

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/paleggs/player-1",
            json={"PalEggs": [{"EggID": "PalEgg_Dark", "PalTemplate": "shadowfox", "Level": 15}]},
            timeout=30.0,
        )

    def test_give_pal_eggs_accepts_friendly_tuples(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"PalEggs":2}}'
        response.json.return_value = {"Granted": {"PalEggs": 2}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_pal_eggs("player-1", ("PalEgg_Dark", PalId.Foxparks, 8), ("PalEgg_Common", "starter_build.json"))

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/paleggs/player-1",
            json={
                "PalEggs": [
                    {"EggID": "PalEgg_Dark", "PalID": "Kitsunebi", "Level": 8},
                    {"EggID": "PalEgg_Common", "PalTemplate": "starter_build.json"},
                ]
            },
            timeout=30.0,
        )

    def test_progression_payload_uses_server_field_names(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"EXP":1000}}'
        response.json.return_value = {"Granted": {"EXP": 1000}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_progression("player-1", GiveProgressionRequest(exp=1000, technology_points=5))

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/progression/player-1",
            json={"EXP": 1000, "TechnologyPoints": 5},
            timeout=30.0,
        )

    def test_give_progression_accepts_keywords(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"EXP":1000}}'
        response.json.return_value = {"Granted": {"EXP": 1000}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_progression("player-1", exp=1000, ancient_technology_points=2)

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/progression/player-1",
            json={"EXP": 1000, "AncientTechnologyPoints": 2},
            timeout=30.0,
        )

    def test_give_recipe_materials_uses_recipe_materials(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"Items":5}}'
        response.json.return_value = {"Granted": {"Items": 5}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_recipe_materials("player-1", ItemId.WoodenClub)

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/items/player-1",
            json={"Items": [{"ItemID": "Wood", "Count": 5}]},
            timeout=30.0,
        )

    def test_give_recipe_materials_scales_quantity(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"Items":30}}'
        response.json.return_value = {"Granted": {"Items": 30}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_recipe_materials("player-1", ItemId.PalSphere, quantity=2)

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/items/player-1",
            json={
                "Items": [
                    {"ItemID": "Pal_crystal_S", "Count": 2},
                    {"ItemID": "Wood", "Count": 6},
                    {"ItemID": "Stone", "Count": 6},
                ]
            },
            timeout=30.0,
        )

    def test_give_recipe_materials_rejects_non_item_recipe_materials(self) -> None:
        client = RESTClient("http://localhost:8212", "secret", session=Mock())

        with self.assertRaises(ValueError) as caught:
            client.give_recipe_materials("player-1", ItemId.NutrientTonic)

        self.assertIn("non-item material", str(caught.exception))

    def test_give_recipe_materials_requires_existing_recipe(self) -> None:
        client = RESTClient("http://localhost:8212", "secret", session=Mock())

        with self.assertRaises(ValueError) as caught:
            client.give_recipe_materials("player-1", "NotARealRecipe")

        self.assertIn("No recipe found", str(caught.exception))

    def test_delete_base_uses_registered_route(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Errors":0}'
        response.json.return_value = {"Errors": 0}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.delete_base("base-camp-1")

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/deletebase/base-camp-1",
            json=None,
            timeout=30.0,
        )

    def test_error_response_raises_api_error(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 404
        response.text = "Player not found."
        response.json.side_effect = ValueError("not json")
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)

        with self.assertRaises(PalDefenderApiError) as caught:
            client.get_player("missing")

        self.assertEqual(caught.exception.status_code, 404)
        self.assertEqual(caught.exception.response_body, "Player not found.")

    def test_give_items_accepts_friendly_varargs_and_merges_counts(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"Granted":{"Items":44}}'
        response.json.return_value = {"Granted": {"Items": 44}}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.give_items("player-1", "Wood", "Stone", ("Wood", 42))

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/items/player-1",
            json={"Items": [{"ItemID": "Wood", "Count": 43}, {"ItemID": "Stone", "Count": 1}]},
            timeout=30.0,
        )

    def test_learn_tech_accepts_technology_ids(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"UnlockedCount":2}'
        response.json.return_value = {"UnlockedCount": 2}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.learn_tech("player-1", TechnologyId.PrimitiveWorkbench, TechnologyId.GigaShield)

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/learntech/player-1",
            json={"Technology": ["Workbench", "Shield_03"]},
            timeout=30.0,
        )

    def test_forget_tech_accepts_technology_ids(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"ForgottenCount":2}'
        response.json.return_value = {"ForgottenCount": 2}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.forget_tech("player-1", TechnologyId.PrimitiveWorkbench, TechnologyId.GigaShield)

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/forgettech/player-1",
            json={"Technology": ["Workbench", "Shield_03"]},
            timeout=30.0,
        )

    def test_technology_all_must_be_passed_alone(self) -> None:
        client = RESTClient("http://localhost:8212", "secret", session=Mock())

        with self.assertRaises(ValueError) as caught:
            client.forget_tech("player-1", "All", TechnologyId.PrimitiveWorkbench)

        self.assertIn('"All" is only valid', str(caught.exception))


if __name__ == "__main__":
    unittest.main()
