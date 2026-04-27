# PalDefender REST API Endpoints

This document mirrors the routes registered in `Reference/RESTAPI.cpp` and the handler behavior implemented under `Reference/RESTAPI/GET` and `Reference/RESTAPI/POST`.

## Common Behavior

- Base path: `/v1/pdapi`
- Authentication: `Authorization: Bearer <token>` is required on every request.
- Optional header: `DisplayAddress` is accepted by the server for logging.
- CORS:
  - `OPTIONS` preflight is supported.
  - Requests from disallowed origins return `403`.
- Startup guard: requests may return `403` with `Server has not been started up yet.`
- Invalid JSON request bodies return `400` with a plain-text error string prefixed by `Error:`.

## GET Endpoints

### `GET /v1/pdapi/version`

Returns the PalDefender version payload:

```json
{
  "major": 0,
  "minor": 0,
  "patch": 0,
  "build": 0,
  "version_str": "0.0.0",
  "version_str_long": "0.0.0+build",
  "beta": true
}
```

### `GET /v1/pdapi/guilds`

Returns a JSON object keyed by guild id. Each guild entry contains:

- `name`
- `Level`
- `admin`
- `camp_count`
- `camps`
- `member_count`
- `members`

Camp entries contain:

- `id`
- `world_pos`
- `map_pos`

The `members` array contains player UID strings.

### `GET /v1/pdapi/guild/{guild_id}`

Returns one guild object. If the guild is missing, the body is the JSON string `Guild '{guild_id}' not found.`.

The guild payload contains:

- `name`
- `Level`
- `admin`
- `member_count`
- `members`
- `camp_count`
- `camps`
- `items`
- `expeditions`
- `laboratory`

Camp entries add:

- `level`
- `state`
- `pals`
- `buildings`

Guild item storage includes:

- `container_id`
- `current`
- `max`
- numeric slot keys whose values may contain `item_id` and `count`

Guild member entries contain:

- `player_uid`
- `player_name`
- `status`

### `GET /v1/pdapi/items/players`

Returns an array of players. Each player entry contains:

- `Name`
- `IP`
- `PlayerUID`
- `UserId`
- `GuildName`
- `GuildUUID`
- `WorldLocation`
- `MapLocation`

### `GET /v1/pdapi/items/player/{player_identifier}`

Returns one player object. If the player is missing, the server returns:

- status: `404`
- body: `Player with UserId or PlayerUID '{player_identifier}' not found.`

`player_identifier` may be either the PalDefender `UserId` or `PlayerUID`.

### `GET /v1/pdapi/items/pals/{player_identifier}`

Returns:

- `team`
- `palbox`
- `base_camps`

`team` and `palbox` are objects keyed by pal instance id. Individual pal payloads come from the server-side `PalTemplate::ToJSON` serializer and then add location metadata:

- `team_slot_index` on team pals
- `page` and `slot` on palbox pals

`base_camps` is an array. Each entry contains:

- `id`
- `level`
- `world_pos`
- `map_pos`
- `state`
- `pals`

Base-camp pal entries add `base_camp_slot_index`.

Missing player returns `404` with `Player with UserId or PlayerUID '{player_identifier}' not found.`. Missing player state returns `404` with `PlayerState for UserId or PlayerUID '{player_identifier}' not found.`.

### `GET /v1/pdapi/items/{player_identifier}`

Returns six inventory sections:

- `Items`
- `KeyItems`
- `Weapons`
- `Armor`
- `Food`
- `DropSlot`

Each section contains:

- `Available`
- `ContainerID`
- `UsedSlots`
- `MaxSlots`
- `FreeSlots`
- `Slots`

Non-empty `Slots` are keyed by slot index and contain:

- `ItemID`
- `Count`

### `GET /v1/pdapi/techs/{player_identifier}`

Returns:

- `UnlockedCount`
- `LockedCount`
- `TotalCount`
- `Unlocked`

### `GET /v1/pdapi/progression/{player_identifier}`

Returns structured progression data:

- `playerProgression`
- `currencies`
- `bosses`
- `captures`
- `activities`

`playerProgression` contains:

- `level`
- `exp`
- `unusedStatusPoints`

`currencies` contains:

- `lifmunks`
- `technologyPoints`
- `ancientTechnologyPoints`

`bosses` contains:

- `towerBossDefeatCounts`
- `normalBossDefeatFlags`
- `raidBossDefeatCounts`
- `totalBossDefeatCount`
- `predatorDefeatCount`

`captures` contains:

- `tribeCaptureCount`
- `palCaptureCounts`
- `palCaptureBonusCounts`
- `palButcherCounts`

`activities` contains:

- `craftItemCounts`
- `normalDungeonClearCount`
- `fixedDungeonClearCount`
- `oilrigClearCount`
- `palRankUpCounts`
- `arenaSoloClearCounts`
- `npcTalkCounts`
- `fishingCounts`
- `foundTreasureCount`
- `campConqueredCount`
- `firstFishingComplete`

The response also preserves older top-level compatibility fields:

- `Level`
- `EXP`
- `UnusedStatusPoints`
- `Lifmunks`
- `TechnologyPoints`
- `AncientTechnologyPoints`

## POST Endpoints

### `POST /v1/pdapi/give/items/{player_identifier}`

Request body:

```json
{
  "Items": [
    { "ItemID": "Stone", "Count": 100 }
  ]
}
```

Rules:

- `Items` must be an array.
- Every item needs `ItemID` and `Count`.
- `Count` must be a positive integer.
- The request fails when validation or inventory insertion fails.

Success response:

```json
{
  "Errors": 0,
  "Error": {},
  "Granted": {
    "Items": 100
  }
}
```

`Granted.Items` is the sum of granted item counts, not the number of array entries.

### `POST /v1/pdapi/give/pals/{player_identifier}`

Request body:

```json
{
  "Pals": [
    { "PalID": "Lamball", "Level": 10 }
  ]
}
```

Rules:

- `Pals` must be an array.
- Each entry needs `PalID` and `Level`.
- `Level` must be a positive integer.
- Free slots are checked across the player team and pal storage together.

Success response returns `Granted.Pals`.

### `POST /v1/pdapi/give/paltemplate/{player_identifier}`

Request body:

```json
{
  "PalTemplates": [
    "shadowfox.json"
  ]
}
```

Rules:

- `PalTemplates` must be an array of template file names.
- Missing `.json` is added by the server automatically.
- Free slots are checked across the player team and pal storage together.

Success response returns `Granted.PalTemplates`.

### `POST /v1/pdapi/give/paleggs/{player_identifier}`

Request body:

```json
{
  "PalEggs": [
    { "EggID": "PalEgg_Dark", "PalID": "Foxparks", "Level": 8 },
    { "EggID": "PalEgg_Common", "PalTemplate": "starter_build.json" }
  ]
}
```

Rules:

- `PalEggs` must be an array.
- Every entry requires `EggID`.
- Every entry must contain exactly one of `PalID` or `PalTemplate`.
- `Level` is optional and defaults to `1`.
- If provided, `Level` must be a positive integer.
- The player must have enough free normal inventory slots for the number of egg entries.

Success response returns `Granted.PalEggs`.

### `POST /v1/pdapi/give/progression/{player_identifier}`

Request body may include one or more of:

```json
{
  "EXP": 1000,
  "Lifmunks": 3,
  "TechnologyPoints": 5,
  "AncientTechnologyPoints": 1
}
```

Rules:

- At least one of those fields must be present.
- Each present value must be a positive integer.
- `EXP` also requires a player handle and internal exp function to be available.

Success response returns:

- `Granted`
- optional `Totals.Lifmunks`
- optional `Totals.TechnologyPoints`
- optional `Totals.AncientTechnologyPoints`

### `POST /v1/pdapi/learntech/{player_identifier}`

Request body:

```json
{
  "Technology": "TechName"
}
```

or

```json
{
  "Technology": ["TechA", "TechB"]
}
```

or

```json
{
  "Technology": "All"
}
```

Rules:

- `Technology` is required.
- It must be a string or an array of strings.
- `All` is only valid when sent as a single string.
- Array entries must all be strings.

Success response returns:

- `Errors`
- `UnlockedCount`
- `Unlocked`
- `Skipped`

### `POST /v1/pdapi/forgettech/{player_identifier}`

Request body matches `learntech`.

Special behavior:

- `Technology: "All"` removes every unlocked technology.
- When forgetting all, `Forgotten` is the string `"All"` instead of an array.

Success response returns:

- `Errors`
- `ForgottenCount`
- `Forgotten`
- `Skipped`

### `POST /v1/pdapi/deletebase/{base_camp_identifier}`

Request body is ignored and can be empty.

`base_camp_identifier` must parse as a GUID.

Possible outcomes:

- `400` when the identifier is not a valid GUID
- `404` when the base camp does not exist
- `500` when the base-camp manager cannot be retrieved or destruction fails

Success response includes:

- `Errors`
- `BaseCamp.Id`
- `BaseCamp.Summary`
- `Deleted.BaseCampPals`
- `Deleted.StorageContainers`
- `Deleted.ItemStacks`
- `Deleted.ItemCount`
- `Deleted.Buildings`
- `Deleted.DropItems`
- `Deleted.DefenseModels`
- `Deleted.OtherMapObjects`
- `Deleted.PalBox`
- `Archive`

## Error Shapes

The server uses multiple error formats depending on the endpoint:

- Plain text:
  - `Unauthorized.`
  - `Player with UserId or PlayerUID '...' not found.`
  - `PlayerState for UserId or PlayerUID '...' not found.`
  - `Server has not been started up yet.`
- JSON:

```json
{
  "Errors": 1,
  "Error": {
    "Items": "Expected an array field named 'Items'."
  }
}
```

Or with detailed arrays / nested objects:

```json
{
  "Errors": 2,
  "Error": {
    "Pals": [
      "Pal 1 is missing the \"PalID\" key."
    ],
    "PalStorage": {
      "message": "Pal storage space is 0 (0 player + 0 storage) but trying to give 1 pals.",
      "details": {
        "free_slots_player": 0,
        "free_slots_storage": 0,
        "free_slots_total": 0,
        "pals_count": 1
      }
    }
  }
}
```
