# PalDefender Python Client Guide

This guide focuses on how to use the Python package in real code.
For raw route and payload reference, see [ENDPOINTS.md](./ENDPOINTS.md).

## Install

From the repository root:

```bash
pip install .
```

For the example CLI:

```bash
pip install -e .
```

## Creating a Client

```python
from PalDefender import RESTClient

client = RESTClient(
    base_url="http://127.0.0.1",
    bearer_token="your-token",
)
```

You can also use a context manager so the underlying `requests.Session` is closed automatically:

```python
from PalDefender import RESTClient

with RESTClient(
    base_url="http://127.0.0.1",
    bearer_token="your-token",
) as client:
    version = client.get_version()
```

## Connection Settings

- `base_url`: base server URL such as `http://127.0.0.1`
- `bearer_token`: required API bearer token
- `timeout`: request timeout in seconds, defaults to `30.0`
- `display_address`: optional `DisplayAddress` header used by the server for logging
- `session`: optional existing `requests.Session`

If `base_url` does not include a port, the client automatically uses `17993`.

Example:

```python
from PalDefender import RESTClient

with RESTClient(
    base_url="http://192.168.1.20",
    bearer_token="secret",
    timeout=10.0,
    display_address="AdminPanel",
) as client:
    print(client.get_version().version_str)
```

## GET Methods

The `get_*` methods return typed Python dataclasses instead of raw JSON dictionaries.

Available methods:

- `get_version()`
- `get_guilds()`
- `get_guild(guild_id)`
- `get_players()`
- `get_player(player_identifier)`
- `get_pals(player_identifier)`
- `get_items(player_identifier)`
- `get_techs(player_identifier)`
- `get_progression(player_identifier)`

Example:

```python
from PalDefender import RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    version = client.get_version()
    print(version.version_str)

    players = client.get_players()
    for player in players.players:
        print(player.name, player.player_uid, player.user_id)
```

The older names such as `version()` and `players()` still exist as aliases, but `get_*` is the preferred API.

## Working With Typed Responses

GET methods return models such as:

- `VersionInfo`
- `GuildsResponse`
- `GuildDetail`
- `PlayersResponse`
- `PlayerInfo`
- `PlayerPalsResponse`
- `PlayerItemsResponse`
- `PlayerTechsResponse`
- `PlayerProgressionResponse`

Example:

```python
from PalDefender import RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    inventory = client.get_items("player-uid-or-userid")
    print(inventory.items.free_slots)

    techs = client.get_techs("player-uid-or-userid")
    print(techs.unlocked_count)
```

If you want plain nested dictionaries again, use `model_to_dict()`:

```python
from PalDefender import RESTClient, model_to_dict

with RESTClient("http://127.0.0.1", "token") as client:
    data = client.get_progression("player-uid-or-userid")
    raw_like_dict = model_to_dict(data)
```

## Item Constants

The package exports constant enums and lookup maps:

- `ItemId`
- `PalId`
- `PassiveId`
- `SkillId`
- `TechnologyId`
- `ITEM_ID_TO_NAME`
- `PAL_ID_TO_NAME`
- `PASSIVE_ID_TO_NAME`
- `SKILL_ID_TO_NAME`
- `TECHNOLOGY_ID_TO_NAME`

These enums contain the actual API ids as their `.value`.

Example:

```python
from PalDefender import ItemId, PalId, TechnologyId

print(ItemId.Wood.value)
print(PalId.Lamball.value)
print(TechnologyId.PrimitiveWorkbench.value)
```

## POST Methods

Available write methods:

- `give_items(player_identifier, *items)`
- `give_recipe_materials(player_identifier, product, quantity=1)`
- `give_pals(player_identifier, *pals)`
- `give_pal_templates(player_identifier, *templates)`
- `give_pal_eggs(player_identifier, *pal_eggs)`
- `give_progression(player_identifier, request=None, *, exp=None, lifmunks=None, technology_points=None, ancient_technology_points=None)`
- `learn_tech(player_identifier, *technology)`
- `forget_tech(player_identifier, *technology)`
- `delete_base(base_camp_identifier)`

## Giving Items

`give_items()` accepts several input styles:

- plain strings
- `(item_id, count)` tuples
- `GiveItem`
- dictionaries with `ItemID` and `Count`
- a single list or tuple containing any of those

Duplicate item ids are merged before the request is sent.

Example:

```python
from PalDefender import GiveItem, ItemId, RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.give_items(
        "player-uid-or-userid",
        ItemId.Wood.value,
        (ItemId.Stone.value, 50),
        GiveItem(ItemId.Wood.value, 10),
    )
```

That sends `Wood x11` and `Stone x50`.

## Giving Recipe Materials

`give_recipe_materials()` resolves recipe ingredients locally from the exported recipe database and then calls `give_items()`.

Example:

```python
from PalDefender import ItemId, RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.give_recipe_materials(
        "player-uid-or-userid",
        ItemId.PalSphere,
        quantity=2,
    )
```

Useful exports:

- `has_recipe(product)`
- `get_recipe(product)`
- `get_recipe_materials(product)`
- `get_recipes()`

## Giving Pals

`give_pals()` accepts:

- plain strings
- `PalId`
- `(pal_id, level)` tuples
- `GivePal`
- dictionaries with `PalID` and `Level`
- a single list or tuple containing any of those

Examples:

```python
from PalDefender import GivePal, PalId, RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.give_pals(
        "player-uid-or-userid",
        PalId.Lamball,
        (PalId.Foxparks, 10),
        GivePal("Anubis", 20),
    )
```

Passing `PalId.Lamball` alone defaults to level `1`.

## Giving Pal Templates

`give_pal_templates()` accepts varargs or a single sequence of template names.

```python
from PalDefender import RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.give_pal_templates(
        "player-uid-or-userid",
        "starter_build.json",
        "shadowfox.json",
    )
```

## Giving Pal Eggs

`give_pal_eggs()` accepts:

- `GivePalEgg`
- dictionaries
- tuples like `(egg_id, pal_id_or_template)`
- tuples like `(egg_id, pal_id_or_template, level)`

Examples:

```python
from PalDefender import GivePalEgg, PalId, RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.give_pal_eggs(
        "player-uid-or-userid",
        ("PalEgg_Dark", PalId.Foxparks, 8),
        ("PalEgg_Common", "starter_build.json"),
        GivePalEgg("PalEgg_Dark", pal_template="shadowfox.json", level=12),
    )
```

If the second tuple value is a known `PalId`, it is sent as `PalID`.
If it is a template filename such as `starter_build.json`, it is sent as `PalTemplate`.

## Giving Progression

You can use either a request dataclass or keyword arguments.

Dataclass style:

```python
from PalDefender import GiveProgressionRequest, RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.give_progression(
        "player-uid-or-userid",
        GiveProgressionRequest(exp=1000, technology_points=5),
    )
```

Keyword style:

```python
from PalDefender import RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.give_progression(
        "player-uid-or-userid",
        exp=1000,
        lifmunks=3,
        technology_points=5,
        ancient_technology_points=1,
    )
```

Do not pass both a request object and keyword progression values in the same call.

## Learning And Forgetting Technology

`learn_tech()` and `forget_tech()` accept:

- strings
- `TechnologyId`
- multiple varargs
- a single list or tuple of values

Examples:

```python
from PalDefender import RESTClient, TechnologyId

with RESTClient("http://127.0.0.1", "token") as client:
    client.learn_tech(
        "player-uid-or-userid",
        TechnologyId.PrimitiveWorkbench,
        TechnologyId.CommonShield,
    )

    client.forget_tech(
        "player-uid-or-userid",
        TechnologyId.PrimitiveWorkbench,
    )
```

The special value `"All"` is only valid by itself:

```python
client.forget_tech("player-uid-or-userid", "All")
```

## Deleting A Base

Use `delete_base()` with a base camp GUID:

```python
from PalDefender import RESTClient

with RESTClient("http://127.0.0.1", "token") as client:
    client.delete_base("00000000-0000-0000-0000-000000000000")
```

## Error Handling

HTTP failures raise `PalDefenderApiError`.

The exception exposes:

- `status_code`
- `method`
- `path`
- `response_body`

Example:

```python
from PalDefender import PalDefenderApiError, RESTClient

try:
    with RESTClient("http://127.0.0.1", "token") as client:
        client.get_player("missing-player")
except PalDefenderApiError as exc:
    print(exc.status_code)
    print(exc.method, exc.path)
    print(exc.response_body)
```

## Full Example CLI

The package also installs a `paldefender-cli` command for terminal use.

It is useful when you want to:

- verify credentials quickly
- inspect live responses
- call endpoints without writing your own script first
