"""Synchronous PalDefender REST API client."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Any
from urllib.parse import quote, urlsplit, urlunsplit

import requests

from .errors import PalDefenderApiError
from .models import GiveItem, GivePal, GivePalEgg, GiveProgressionRequest

JsonValue = dict[str, Any] | list[Any] | str | int | float | bool | None


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

    def version(self) -> JsonValue:
        return self._request("GET", "/v1/pdapi/version")

    def guilds(self) -> JsonValue:
        return self._request("GET", "/v1/pdapi/guilds")

    def guild(self, guild_id: str) -> JsonValue:
        return self._request("GET", f"/v1/pdapi/guild/{self._path_part(guild_id)}")

    def players(self) -> JsonValue:
        return self._request("GET", "/v1/pdapi/players")

    def player(self, player_identifier: str) -> JsonValue:
        return self._request("GET", f"/v1/pdapi/player/{self._path_part(player_identifier)}")

    def pals(self, player_identifier: str) -> JsonValue:
        return self._request("GET", f"/v1/pdapi/pals/{self._path_part(player_identifier)}")

    def items(self, player_identifier: str) -> JsonValue:
        return self._request("GET", f"/v1/pdapi/items/{self._path_part(player_identifier)}")

    def techs(self, player_identifier: str) -> JsonValue:
        return self._request("GET", f"/v1/pdapi/techs/{self._path_part(player_identifier)}")

    def progression(self, player_identifier: str) -> JsonValue:
        return self._request("GET", f"/v1/pdapi/progression/{self._path_part(player_identifier)}")

    def give_items(
        self,
        player_identifier: str,
        items: Sequence[GiveItem | dict[str, Any]],
    ) -> JsonValue:
        payload = {"Items": [self._serialize_entry(item) for item in items]}
        return self._request("POST", f"/v1/pdapi/give/items/{self._path_part(player_identifier)}", json=payload)

    def give_pals(
        self,
        player_identifier: str,
        pals: Sequence[GivePal | dict[str, Any]],
    ) -> JsonValue:
        payload = {"Pals": [self._serialize_entry(pal) for pal in pals]}
        return self._request("POST", f"/v1/pdapi/give/pals/{self._path_part(player_identifier)}", json=payload)

    def give_pal_templates(
        self,
        player_identifier: str,
        templates: Sequence[str],
    ) -> JsonValue:
        return self._request(
            "POST",
            f"/v1/pdapi/give/paltemplate/{self._path_part(player_identifier)}",
            json={"PalTemplates": list(templates)},
        )

    def give_pal_eggs(
        self,
        player_identifier: str,
        pal_eggs: Sequence[GivePalEgg | dict[str, Any]],
    ) -> JsonValue:
        payload = {"PalEggs": [self._serialize_entry(pal_egg) for pal_egg in pal_eggs]}
        return self._request("POST", f"/v1/pdapi/give/paleggs/{self._path_part(player_identifier)}", json=payload)

    def give_progression(
        self,
        player_identifier: str,
        request: GiveProgressionRequest | dict[str, Any],
    ) -> JsonValue:
        return self._request(
            "POST",
            f"/v1/pdapi/give/progression/{self._path_part(player_identifier)}",
            json=self._serialize_entry(request),
        )

    def learn_tech(
        self,
        player_identifier: str,
        technology: str | Sequence[str],
    ) -> JsonValue:
        return self._request(
            "POST",
            f"/v1/pdapi/learntech/{self._path_part(player_identifier)}",
            json={"Technology": self._technology_payload(technology)},
        )

    def forget_tech(
        self,
        player_identifier: str,
        technology: str | Sequence[str],
    ) -> JsonValue:
        return self._request(
            "POST",
            f"/v1/pdapi/forgettech/{self._path_part(player_identifier)}",
            json={"Technology": self._technology_payload(technology)},
        )

    @staticmethod
    def _serialize_entry(value: Any) -> Any:
        if hasattr(value, "to_dict"):
            return value.to_dict()
        return value

    @staticmethod
    def _technology_payload(technology: str | Sequence[str]) -> str | list[str]:
        if isinstance(technology, str):
            return technology
        if isinstance(technology, Iterable):
            return list(technology)
        raise TypeError("technology must be a string or a sequence of strings")

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
