from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from paldefender_cli.cli import load_json_argument, load_settings, parse_items, resolve_env_path


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

    def test_resolve_env_path_prefers_explicit_path(self) -> None:
        resolved = resolve_env_path("./custom.env")

        self.assertTrue(resolved is not None)
        self.assertEqual(resolved.name, "custom.env")

    def test_load_settings_reads_values_from_env_file(self) -> None:
        with TemporaryDirectory() as tmp_dir:
            env_path = Path(tmp_dir) / ".env"
            env_path.write_text(
                "PALDEFENDER_BASE_URL=http://localhost\n"
                "PALDEFENDER_BEARER_TOKEN=secret\n"
                "PALDEFENDER_TIMEOUT=45\n",
                encoding="utf-8",
            )

            old_base_url = os.environ.pop("PALDEFENDER_BASE_URL", None)
            old_bearer_token = os.environ.pop("PALDEFENDER_BEARER_TOKEN", None)
            old_timeout = os.environ.pop("PALDEFENDER_TIMEOUT", None)
            try:
                settings = load_settings(env_path)
            finally:
                if old_base_url is not None:
                    os.environ["PALDEFENDER_BASE_URL"] = old_base_url
                else:
                    os.environ.pop("PALDEFENDER_BASE_URL", None)
                if old_bearer_token is not None:
                    os.environ["PALDEFENDER_BEARER_TOKEN"] = old_bearer_token
                else:
                    os.environ.pop("PALDEFENDER_BEARER_TOKEN", None)
                if old_timeout is not None:
                    os.environ["PALDEFENDER_TIMEOUT"] = old_timeout
                else:
                    os.environ.pop("PALDEFENDER_TIMEOUT", None)

        self.assertEqual(settings["base_url"], "http://localhost")
        self.assertEqual(settings["bearer_token"], "secret")
        self.assertEqual(settings["timeout"], 45.0)


if __name__ == "__main__":
    unittest.main()
