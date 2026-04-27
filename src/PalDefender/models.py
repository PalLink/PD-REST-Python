"""Helper models for PalDefender API requests and responses."""

from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass
from typing import Any


def model_to_dict(value: Any) -> Any:
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if is_dataclass(value):
        return {
            dataclass_field.name: model_to_dict(getattr(value, dataclass_field.name))
            for dataclass_field in fields(value)
            if dataclass_field.name != "raw"
        }
    if isinstance(value, dict):
        return {key: model_to_dict(item) for key, item in value.items()}
    if isinstance(value, list):
        return [model_to_dict(item) for item in value]
    return value


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


@dataclass(slots=True, frozen=True)
class VersionInfo:
    major: int
    minor: int
    patch: int
    build: int
    version_str: str
    version_str_long: str
    beta: bool

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "VersionInfo":
        return cls(
            major=data["major"],
            minor=data["minor"],
            patch=data["patch"],
            build=data["build"],
            version_str=data["version_str"],
            version_str_long=data["version_str_long"],
            beta=data["beta"],
        )


@dataclass(slots=True, frozen=True)
class Position:
    x: float | int | None = None
    y: float | int | None = None
    z: float | int | None = None
    raw: Any = None

    @classmethod
    def from_value(cls, value: Any) -> "Position":
        if isinstance(value, dict):
            return cls(
                x=value.get("x", value.get("X")),
                y=value.get("y", value.get("Y")),
                z=value.get("z", value.get("Z")),
                raw=value,
            )
        return cls(raw=value)


@dataclass(slots=True, frozen=True)
class GuildCampSummary:
    id: str
    world_pos: Position
    map_pos: Position

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GuildCampSummary":
        return cls(
            id=str(data.get("id", "")),
            world_pos=Position.from_value(data.get("world_pos")),
            map_pos=Position.from_value(data.get("map_pos")),
        )


@dataclass(slots=True, frozen=True)
class GuildSummary:
    id: str
    name: str
    level: int | None
    admin: str | None
    camp_count: int | None
    camps: list[GuildCampSummary]
    member_count: int | None
    members: list[str]

    @classmethod
    def from_dict(cls, guild_id: str, data: dict[str, Any]) -> "GuildSummary":
        return cls(
            id=guild_id,
            name=str(data.get("name", "")),
            level=data.get("Level"),
            admin=data.get("admin"),
            camp_count=data.get("camp_count"),
            camps=[GuildCampSummary.from_dict(item) for item in data.get("camps", [])],
            member_count=data.get("member_count"),
            members=[str(item) for item in data.get("members", [])],
        )


@dataclass(slots=True, frozen=True)
class GuildsResponse:
    guilds: dict[str, GuildSummary]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GuildsResponse":
        return cls({guild_id: GuildSummary.from_dict(guild_id, value) for guild_id, value in data.items()})


@dataclass(slots=True, frozen=True)
class GuildMember:
    player_uid: str
    player_name: str | None
    status: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GuildMember":
        return cls(
            player_uid=str(data.get("player_uid", "")),
            player_name=data.get("player_name"),
            status=data.get("status"),
        )


@dataclass(slots=True, frozen=True)
class GuildCampDetail:
    id: str
    world_pos: Position
    map_pos: Position
    level: int | None
    state: str | None
    pals: list[dict[str, Any]]
    buildings: list[dict[str, Any]]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GuildCampDetail":
        return cls(
            id=str(data.get("id", "")),
            world_pos=Position.from_value(data.get("world_pos")),
            map_pos=Position.from_value(data.get("map_pos")),
            level=data.get("level"),
            state=data.get("state"),
            pals=[item for item in data.get("pals", []) if isinstance(item, dict)],
            buildings=[item for item in data.get("buildings", []) if isinstance(item, dict)],
        )


@dataclass(slots=True, frozen=True)
class GuildStorage:
    container_id: str | None
    current: int | None
    max: int | None
    slots: dict[str, dict[str, Any]]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GuildStorage":
        slots = {
            key: value
            for key, value in data.items()
            if key not in {"container_id", "current", "max"} and isinstance(value, dict)
        }
        return cls(
            container_id=data.get("container_id"),
            current=data.get("current"),
            max=data.get("max"),
            slots=slots,
        )


@dataclass(slots=True, frozen=True)
class GuildDetail:
    name: str
    level: int | None
    admin: str | None
    member_count: int | None
    members: list[GuildMember]
    camp_count: int | None
    camps: list[GuildCampDetail]
    items: list[GuildStorage]
    expeditions: Any
    laboratory: Any
    raw: dict[str, Any] = field(repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GuildDetail":
        return cls(
            name=str(data.get("name", "")),
            level=data.get("Level"),
            admin=data.get("admin"),
            member_count=data.get("member_count"),
            members=[GuildMember.from_dict(item) for item in data.get("members", []) if isinstance(item, dict)],
            camp_count=data.get("camp_count"),
            camps=[GuildCampDetail.from_dict(item) for item in data.get("camps", [])],
            items=[GuildStorage.from_dict(item) for item in data.get("items", []) if isinstance(item, dict)],
            expeditions=data.get("expeditions"),
            laboratory=data.get("laboratory"),
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class PlayerInfo:
    name: str | None
    ip: str | None
    player_uid: str | None
    user_id: str | None
    guild_name: str | None
    guild_uuid: str | None
    world_location: Position
    map_location: Position
    raw: dict[str, Any] = field(repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerInfo":
        return cls(
            name=data.get("Name"),
            ip=data.get("IP"),
            player_uid=data.get("PlayerUID"),
            user_id=data.get("UserId"),
            guild_name=data.get("GuildName"),
            guild_uuid=data.get("GuildUUID"),
            world_location=Position.from_value(data.get("WorldLocation")),
            map_location=Position.from_value(data.get("MapLocation")),
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class PlayersResponse:
    players: list[PlayerInfo]

    @classmethod
    def from_list(cls, data: list[dict[str, Any]]) -> "PlayersResponse":
        return cls([PlayerInfo.from_dict(item) for item in data])


@dataclass(slots=True, frozen=True)
class PalInstance:
    instance_id: str
    attributes: dict[str, Any]

    @classmethod
    def from_dict(cls, instance_id: str, data: dict[str, Any]) -> "PalInstance":
        return cls(instance_id=instance_id, attributes=data)


@dataclass(slots=True, frozen=True)
class PlayerBaseCamp:
    id: str
    level: int | None
    world_pos: Position
    map_pos: Position
    state: str | None
    pals: dict[str, PalInstance]
    raw: dict[str, Any] = field(repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerBaseCamp":
        pals = {
            instance_id: PalInstance.from_dict(instance_id, pal_data)
            for instance_id, pal_data in data.get("pals", {}).items()
            if isinstance(pal_data, dict)
        }
        return cls(
            id=str(data.get("id", "")),
            level=data.get("level"),
            world_pos=Position.from_value(data.get("world_pos")),
            map_pos=Position.from_value(data.get("map_pos")),
            state=data.get("state"),
            pals=pals,
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class PlayerPalsResponse:
    team: dict[str, PalInstance]
    palbox: dict[str, PalInstance]
    base_camps: list[PlayerBaseCamp]
    raw: dict[str, Any] = field(repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerPalsResponse":
        return cls(
            team={
                instance_id: PalInstance.from_dict(instance_id, pal_data)
                for instance_id, pal_data in data.get("team", {}).items()
                if isinstance(pal_data, dict)
            },
            palbox={
                instance_id: PalInstance.from_dict(instance_id, pal_data)
                for instance_id, pal_data in data.get("palbox", {}).items()
                if isinstance(pal_data, dict)
            },
            base_camps=[PlayerBaseCamp.from_dict(item) for item in data.get("base_camps", []) if isinstance(item, dict)],
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class InventorySlot:
    item_id: str | None
    count: int | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "InventorySlot":
        return cls(item_id=data.get("ItemID"), count=data.get("Count"))


@dataclass(slots=True, frozen=True)
class InventorySection:
    available: int | None
    container_id: str | None
    used_slots: int | None
    max_slots: int | None
    free_slots: int | None
    slots: dict[str, InventorySlot]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "InventorySection":
        slot_data = data.get("Slots", {})
        return cls(
            available=data.get("Available"),
            container_id=data.get("ContainerID"),
            used_slots=data.get("UsedSlots"),
            max_slots=data.get("MaxSlots"),
            free_slots=data.get("FreeSlots"),
            slots={
                str(slot_index): InventorySlot.from_dict(slot)
                for slot_index, slot in slot_data.items()
                if isinstance(slot, dict)
            },
        )


@dataclass(slots=True, frozen=True)
class PlayerItemsResponse:
    items: InventorySection
    key_items: InventorySection
    weapons: InventorySection
    armor: InventorySection
    food: InventorySection
    drop_slot: InventorySection
    raw: dict[str, Any] = field(repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerItemsResponse":
        return cls(
            items=InventorySection.from_dict(data.get("Items", {})),
            key_items=InventorySection.from_dict(data.get("KeyItems", {})),
            weapons=InventorySection.from_dict(data.get("Weapons", {})),
            armor=InventorySection.from_dict(data.get("Armor", {})),
            food=InventorySection.from_dict(data.get("Food", {})),
            drop_slot=InventorySection.from_dict(data.get("DropSlot", {})),
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class PlayerTechsResponse:
    unlocked_count: int | None
    locked_count: int | None
    total_count: int | None
    unlocked: list[str]
    raw: dict[str, Any] = field(repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerTechsResponse":
        return cls(
            unlocked_count=data.get("UnlockedCount"),
            locked_count=data.get("LockedCount"),
            total_count=data.get("TotalCount"),
            unlocked=[str(item) for item in data.get("Unlocked", [])],
            raw=data,
        )


@dataclass(slots=True, frozen=True)
class ProgressionPlayer:
    level: int | None
    exp: int | None
    unused_status_points: int | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProgressionPlayer":
        return cls(
            level=data.get("level"),
            exp=data.get("exp"),
            unused_status_points=data.get("unusedStatusPoints"),
        )


@dataclass(slots=True, frozen=True)
class ProgressionCurrencies:
    lifmunks: int | None
    technology_points: int | None
    ancient_technology_points: int | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProgressionCurrencies":
        return cls(
            lifmunks=data.get("lifmunks"),
            technology_points=data.get("technologyPoints"),
            ancient_technology_points=data.get("ancientTechnologyPoints"),
        )


@dataclass(slots=True, frozen=True)
class ProgressionBosses:
    tower_boss_defeat_counts: Any
    normal_boss_defeat_flags: Any
    raid_boss_defeat_counts: Any
    total_boss_defeat_count: int | None
    predator_defeat_count: int | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProgressionBosses":
        return cls(
            tower_boss_defeat_counts=data.get("towerBossDefeatCounts"),
            normal_boss_defeat_flags=data.get("normalBossDefeatFlags"),
            raid_boss_defeat_counts=data.get("raidBossDefeatCounts"),
            total_boss_defeat_count=data.get("totalBossDefeatCount"),
            predator_defeat_count=data.get("predatorDefeatCount"),
        )


@dataclass(slots=True, frozen=True)
class ProgressionCaptures:
    tribe_capture_count: int | None
    pal_capture_counts: Any
    pal_capture_bonus_counts: Any
    pal_butcher_counts: Any

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProgressionCaptures":
        return cls(
            tribe_capture_count=data.get("tribeCaptureCount"),
            pal_capture_counts=data.get("palCaptureCounts"),
            pal_capture_bonus_counts=data.get("palCaptureBonusCounts"),
            pal_butcher_counts=data.get("palButcherCounts"),
        )


@dataclass(slots=True, frozen=True)
class ProgressionActivities:
    craft_item_counts: Any
    normal_dungeon_clear_count: int | None
    fixed_dungeon_clear_count: int | None
    oilrig_clear_count: int | None
    pal_rank_up_counts: Any
    arena_solo_clear_counts: Any
    npc_talk_counts: Any
    fishing_counts: Any
    found_treasure_count: int | None
    camp_conquered_count: int | None
    first_fishing_complete: bool | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProgressionActivities":
        return cls(
            craft_item_counts=data.get("craftItemCounts"),
            normal_dungeon_clear_count=data.get("normalDungeonClearCount"),
            fixed_dungeon_clear_count=data.get("fixedDungeonClearCount"),
            oilrig_clear_count=data.get("oilrigClearCount"),
            pal_rank_up_counts=data.get("palRankUpCounts"),
            arena_solo_clear_counts=data.get("arenaSoloClearCounts"),
            npc_talk_counts=data.get("npcTalkCounts"),
            fishing_counts=data.get("fishingCounts"),
            found_treasure_count=data.get("foundTreasureCount"),
            camp_conquered_count=data.get("campConqueredCount"),
            first_fishing_complete=data.get("firstFishingComplete"),
        )


@dataclass(slots=True, frozen=True)
class PlayerProgressionResponse:
    player_progression: ProgressionPlayer
    currencies: ProgressionCurrencies
    bosses: ProgressionBosses
    captures: ProgressionCaptures
    activities: ProgressionActivities
    level: int | None
    exp: int | None
    unused_status_points: int | None
    lifmunks: int | None
    technology_points: int | None
    ancient_technology_points: int | None
    raw: dict[str, Any] = field(repr=False)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerProgressionResponse":
        return cls(
            player_progression=ProgressionPlayer.from_dict(data.get("playerProgression", {})),
            currencies=ProgressionCurrencies.from_dict(data.get("currencies", {})),
            bosses=ProgressionBosses.from_dict(data.get("bosses", {})),
            captures=ProgressionCaptures.from_dict(data.get("captures", {})),
            activities=ProgressionActivities.from_dict(data.get("activities", {})),
            level=data.get("Level"),
            exp=data.get("EXP"),
            unused_status_points=data.get("UnusedStatusPoints"),
            lifmunks=data.get("Lifmunks"),
            technology_points=data.get("TechnologyPoints"),
            ancient_technology_points=data.get("AncientTechnologyPoints"),
            raw=data,
        )
