# PalDefender REST API Endpoints

This document mirrors the routes registered in `Reference/RESTAPI.cpp` and the request validation implemented in `Reference/RESTAPI/GET` and `Reference/RESTAPI/POST`.

## Common Behavior

- Base path: `/v1/pdapi`
- Authentication: `Authorization: Bearer <token>` is required on every request.
- Optional header: `DisplayAddress` is accepted by the server for logging.
- CORS:
  - `OPTIONS` preflight is supported.
  - Requests from disallowed origins return `403`.
- Startup guard: requests may return `403` with `Server has not been started up yet.`
- Invalid JSON request bodies return `400` with a plain-text error string from the server.

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

### `GET /v1/pdapi/guild/{guild_id}`

Returns one guild object, or the string `Guild '{guild_id}' not found.` when the guild is missing.

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
- indexed slot entries with `item_id` and `count`

### `GET /v1/pdapi/players`

Returns an array of players. Each player entry contains:

- `Name`
- `IP`
- `PlayerUID`
- `UserId`
- `GuildName`
- `GuildUUID`
- `WorldLocation`
- `MapLocation`

### `GET /v1/pdapi/player/{player_identifier}`

Returns one player object. If the player is missing, the server returns:

- status: `404`
- body: `Player with UserId or PlayerUID '{player_identifier}' not found.`

`player_identifier` may be either the PalDefender `UserId` or `PlayerUID`.

### `GET /v1/pdapi/pals/{player_identifier}`

Returns:

- `team`
- `palbox`
- `base_camps`

`team` and `palbox` are objects keyed by pal instance id. Individual pal payloads come from the server-side `PalTemplate::ToJSON` serializer and then add location metadata:

- `team_slot_index` on team pals
- `page` and `slot` on palbox pals
- `base_camp_slot_index` on base camp pals

Missing player or player state returns `404` with a plain-text error string.

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

It also preserves the older top-level compatibility fields:

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
- `ItemID` must be a valid PalDefender item id.
- The request fails when the player inventory has fewer free slots than the number of requested array entries.

Success response:

```json
{
  "Errors": 0,
  "Error": {},
  "Granted": {
    "Items": 1
  }
}
```

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
- The pal id must be valid and PalDefender must be able to generate save parameters.
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
- Each template must import successfully from PalDefender's pal template directory.
- Free slots are checked across team and storage.

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
- `EggID` must be a valid item id.
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
- `EXP` also depends on the player handle and internal exp function being available.

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

Success response returns:

- `Errors`
- `UnlockedCount`
- `Unlocked`
- `Skipped`

### `POST /v1/pdapi/forgettech/{player_identifier}`

Request body matches `learntech`.

Special behavior:

- `Technology: "All"` removes every unlocked technology.

Success response returns:

- `Errors`
- `ForgottenCount`
- `Forgotten`
- `Skipped`

## Error Shapes

The server uses multiple error formats depending on the endpoint:

- Plain text:
  - `Unauthorized.`
  - `Player with UserId or PlayerUID '...' not found.`
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

or with detailed arrays / nested objects:

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
