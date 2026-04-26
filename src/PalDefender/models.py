"""Helper payload models for PalDefender API requests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class GiveItem:
    item_id: str
    count: int

    def __post_init__(self) -> None:
        if not self.item_id:
            raise ValueError("item_id must not be empty")
        if self.count <= 0:
            raise ValueError("count must be a positive integer")

    def to_dict(self) -> dict[str, Any]:
        return {"ItemID": self.item_id, "Count": self.count}


@dataclass(slots=True, frozen=True)
class GivePal:
    pal_id: str
    level: int

    def __post_init__(self) -> None:
        if not self.pal_id:
            raise ValueError("pal_id must not be empty")
        if self.level <= 0:
            raise ValueError("level must be a positive integer")

    def to_dict(self) -> dict[str, Any]:
        return {"PalID": self.pal_id, "Level": self.level}


@dataclass(slots=True, frozen=True)
class GivePalEgg:
    egg_id: str
    pal_id: str | None = None
    pal_template: str | None = None
    level: int | None = None

    def __post_init__(self) -> None:
        if not self.egg_id:
            raise ValueError("egg_id must not be empty")
        if (self.pal_id is None) == (self.pal_template is None):
            raise ValueError("exactly one of pal_id or pal_template must be provided")
        if self.level is not None and self.level <= 0:
            raise ValueError("level must be a positive integer when provided")

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"EggID": self.egg_id}
        if self.pal_id is not None:
            payload["PalID"] = self.pal_id
        if self.pal_template is not None:
            payload["PalTemplate"] = self.pal_template
        if self.level is not None:
            payload["Level"] = self.level
        return payload


@dataclass(slots=True, frozen=True)
class GiveProgressionRequest:
    exp: int | None = None
    lifmunks: int | None = None
    technology_points: int | None = None
    ancient_technology_points: int | None = None

    def __post_init__(self) -> None:
        if (
            self.exp is None
            and self.lifmunks is None
            and self.technology_points is None
            and self.ancient_technology_points is None
        ):
            raise ValueError("at least one progression field must be provided")

        for field_name, value in (
            ("exp", self.exp),
            ("lifmunks", self.lifmunks),
            ("technology_points", self.technology_points),
            ("ancient_technology_points", self.ancient_technology_points),
        ):
            if value is not None and value <= 0:
                raise ValueError(f"{field_name} must be a positive integer")

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {}
        if self.exp is not None:
            payload["EXP"] = self.exp
        if self.lifmunks is not None:
            payload["Lifmunks"] = self.lifmunks
        if self.technology_points is not None:
            payload["TechnologyPoints"] = self.technology_points
        if self.ancient_technology_points is not None:
            payload["AncientTechnologyPoints"] = self.ancient_technology_points
        return payload
