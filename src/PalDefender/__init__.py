"""Python client for the PalDefender REST API."""

from .client import RESTClient
from .errors import PalDefenderApiError
from .models import GiveItem, GivePal, GivePalEgg, GiveProgressionRequest

PalDefenderClient = RESTClient

__all__ = [
    "GiveItem",
    "GivePal",
    "GivePalEgg",
    "GiveProgressionRequest",
    "PalDefenderApiError",
    "PalDefenderClient",
    "RESTClient",
]
