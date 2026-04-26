# PalDefender-REST-Client (Python)

Installable Python client for the PalDefender REST API. The package covers every route currently registered in the PalDefender reference implementation under `Reference/`.

## Install

```bash
pip install .
```

## Quick Start

```python
from PalDefender import GiveItem, RESTClient

with RESTClient(
    base_url="http://127.0.0.1:8212",
    bearer_token="your-token",
) as client:
    version = client.version()
    players = client.players()
    result = client.give_items("player-uid-or-userid", [GiveItem("Stone", 100)])
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

## Available Methods

### Read operations

- `version()`
- `guilds()`
- `guild(guild_id)`
- `players()`
- `player(player_identifier)`
- `pals(player_identifier)`
- `items(player_identifier)`
- `techs(player_identifier)`
- `progression(player_identifier)`

### Write operations

- `give_items(player_identifier, items)`
- `give_pals(player_identifier, pals)`
- `give_pal_templates(player_identifier, templates)`
- `give_pal_eggs(player_identifier, pal_eggs)`
- `give_progression(player_identifier, request)`
- `learn_tech(player_identifier, technology)`
- `forget_tech(player_identifier, technology)`

## Helper Models

The package includes request helper dataclasses:

- `GiveItem`
- `GivePal`
- `GivePalEgg`
- `GiveProgressionRequest`

You can also pass plain dictionaries when that is more convenient.

## Errors

HTTP errors raise `PalDefenderApiError`. The exception exposes:

- `status_code`
- `method`
- `path`
- `response_body`

## Endpoint Reference

Full endpoint documentation is in [docs/ENDPOINTS.md](docs/ENDPOINTS.md).
