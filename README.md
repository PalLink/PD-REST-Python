# PalDefender-REST-Client (Python)

Installable Python client for the PalDefender REST API. The package covers every route currently registered in the PalDefender reference implementation under `Reference/`.

## Install

```bash
pip install .
```

## Quick Start

```python
from PalDefender import RESTClient

with RESTClient(
    base_url="http://127.0.0.1",
    bearer_token="your-token",
) as client:
    version = client.get_version()
    players = client.get_players()
    result = client.give_items("player-uid-or-userid", "Stone", ("Stone", 99))
```

Or:

```python
import PalDefender
```

## Example Project

A runnable example CLI is included in [examples/paldefender_cli](examples/paldefender_cli). It uses a local `.env` file for credentials and server settings, and covers every client endpoint.

```bash
pip install -e .[examples]
python examples/paldefender_cli/main.py version
```

Copy `examples/paldefender_cli/.env.example` to `examples/paldefender_cli/.env`, then fill in your settings before running the example.

If `base_url` omits a port, the client defaults to `17993`.

## Available Methods

### Read operations

- `get_version()`
- `get_guilds()`
- `get_guild(guild_id)`
- `get_players()`
- `get_player(player_identifier)`
- `get_pals(player_identifier)`
- `get_items(player_identifier)`
- `get_techs(player_identifier)`
- `get_progression(player_identifier)`

### Write operations

- `give_items(player_identifier, *items)`
- `give_recipe_materials(player_identifier, product, quantity=1)`
- `give_pals(player_identifier, pals)`
- `give_pal_templates(player_identifier, templates)`
- `give_pal_eggs(player_identifier, pal_eggs)`
- `give_progression(player_identifier, request)`
- `learn_tech(player_identifier, technology)`
- `forget_tech(player_identifier, technology)`
- `delete_base(base_camp_identifier)`

## Helper Models

The package includes request helper dataclasses:

- `GiveItem`
- `GivePal`
- `GivePalEgg`
- `GiveProgressionRequest`

## Constants And Recipes

Generated constants and recipe helpers are exported from the package root:

- `ItemId`, `PalId`, `PassiveId`, `SkillId`, `TechnologyId`
- `ITEM_ID_TO_NAME`, `PAL_ID_TO_NAME`, `PASSIVE_ID_TO_NAME`, `SKILL_ID_TO_NAME`, `TECHNOLOGY_ID_TO_NAME`
- `Recipe`, `has_recipe()`, `get_recipe()`, `get_recipe_materials()`, `get_recipes()`

`give_recipe_materials()` resolves a product recipe locally and then calls the existing `give_items()` endpoint with the required material counts.

`give_items()` accepts strings, `(item_id, count)` tuples, `GiveItem` objects, or a single list/tuple containing those values. Duplicate item ids are merged before the request is sent.

You can also pass plain dictionaries when that is more convenient.

## Errors

HTTP errors raise `PalDefenderApiError`. The exception exposes:

- `status_code`
- `method`
- `path`
- `response_body`

## Endpoint Reference

Full endpoint documentation is in [docs/ENDPOINTS.md](docs/ENDPOINTS.md).

## Usage Guide

For a more detailed Python-focused guide with examples for typed GET responses, friendly POST helpers, constants, recipes, and error handling, see [docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md).
