"""Error types raised by the PalDefender client."""

from __future__ import annotations

from typing import Any


class PalDefenderApiError(RuntimeError):
    """Raised when the PalDefender API returns an error response."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        method: str,
        path: str,
        response_body: Any = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.method = method
        self.path = path
        self.response_body = response_body
