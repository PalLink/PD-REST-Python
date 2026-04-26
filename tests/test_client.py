from __future__ import annotations

import sys
import unittest
from importlib.util import find_spec
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from PalDefender import GiveItem, GivePalEgg, GiveProgressionRequest, PalDefenderApiError, RESTClient


class PalDefenderClientTests(unittest.TestCase):
    def test_old_package_is_not_importable(self) -> None:
        self.assertIsNone(find_spec("paldefender_rest_client"))

    def test_get_endpoint_path(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.text = '{"version_str":"1.0.0"}'
        response.json.return_value = {"version_str": "1.0.0"}
        session.request.return_value = response

        client = RESTClient("http://localhost", "secret", session=session)
        data = client.version()

        self.assertEqual(data["version_str"], "1.0.0")
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
        response.text = '{"version_str":"1.0.0"}'
        response.json.return_value = {"version_str": "1.0.0"}
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)
        client.version()

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
        client.give_items("player-1", [GiveItem("Stone", 50)])

        session.request.assert_called_once_with(
            method="POST",
            url="http://localhost:8212/v1/pdapi/give/items/player-1",
            json={"Items": [{"ItemID": "Stone", "Count": 50}]},
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

    def test_error_response_raises_api_error(self) -> None:
        session = Mock()
        response = Mock()
        response.status_code = 404
        response.text = "Player not found."
        response.json.side_effect = ValueError("not json")
        session.request.return_value = response

        client = RESTClient("http://localhost:8212", "secret", session=session)

        with self.assertRaises(PalDefenderApiError) as caught:
            client.player("missing")

        self.assertEqual(caught.exception.status_code, 404)
        self.assertEqual(caught.exception.response_body, "Player not found.")


if __name__ == "__main__":
    unittest.main()
