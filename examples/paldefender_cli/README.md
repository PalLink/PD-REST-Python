# PalDefender CLI Example

Example project for `paldefender-rest-client` with `.env`-based configuration and support for every client endpoint.

## Setup

From the repository root:

```bash
pip install -e .[examples]
```

Copy `examples/paldefender_cli/.env.example` to `examples/paldefender_cli/.env`, then edit `examples/paldefender_cli/.env` and set:

- `PALDEFENDER_BASE_URL`
- `PALDEFENDER_BEARER_TOKEN`
- `PALDEFENDER_DISPLAY_ADDRESS` (optional)
- `PALDEFENDER_TIMEOUT` (optional)

## Read Commands

```bash
python examples/paldefender_cli/main.py version
python examples/paldefender_cli/main.py guilds
python examples/paldefender_cli/main.py guild guild-id
python examples/paldefender_cli/main.py players
python examples/paldefender_cli/main.py player player-uid-or-userid
python examples/paldefender_cli/main.py pals player-uid-or-userid
python examples/paldefender_cli/main.py items player-uid-or-userid
python examples/paldefender_cli/main.py techs player-uid-or-userid
python examples/paldefender_cli/main.py progression player-uid-or-userid
```

## Write Commands

Inline JSON:

```bash
python examples/paldefender_cli/main.py give-items player-uid '[{"ItemID":"Stone","Count":100}]'
python examples/paldefender_cli/main.py give-pals player-uid '[{"PalID":"Lamball","Level":10}]'
python examples/paldefender_cli/main.py give-pal-templates player-uid starter_build shadowfox.json
python examples/paldefender_cli/main.py give-pal-eggs player-uid '[{"EggID":"PalEgg_Dark","PalID":"Foxparks","Level":8}]'
python examples/paldefender_cli/main.py give-progression player-uid '{"EXP":1000,"TechnologyPoints":5}'
python examples/paldefender_cli/main.py learn-tech player-uid TechA TechB
python examples/paldefender_cli/main.py forget-tech player-uid All
```

JSON from a file:

```bash
python examples/paldefender_cli/main.py give-items player-uid @payloads/items.json
```

## Notes

- The script loads `.env` from the same directory as `main.py`.
- Mutating commands accept inline JSON or `@path/to/file.json` where noted.
- API errors are printed with status code and response body.
