from __future__ import annotations

import sys
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.modules.setdefault("dotenv", types.SimpleNamespace(load_dotenv=lambda *_args, **_kwargs: None))

from examples.paldefender_cli.main import load_json_argument, parse_items


class PalDefenderCliTests(unittest.TestCase):
    def test_load_json_argument_parses_inline_array(self) -> None:
        parsed = load_json_argument('[{"ItemID":"Axe","Count":7}]')

        self.assertEqual(parsed, [{"ItemID": "Axe", "Count": 7}])

    def test_load_json_argument_error_mentions_powershell(self) -> None:
        with self.assertRaises(ValueError) as caught:
            load_json_argument("[{ItemID:Axe,Count:7}]")

        self.assertIn("If you are using PowerShell", str(caught.exception))

    def test_parse_items_maps_known_item_shape(self) -> None:
        parsed = parse_items('[{"ItemID":"Axe","Count":7}]')

        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0].to_dict(), {"ItemID": "Axe", "Count": 7})


if __name__ == "__main__":
    unittest.main()
