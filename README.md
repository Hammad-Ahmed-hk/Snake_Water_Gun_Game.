# Snake, Water, Gun

A command-line version of the classic game against the computer, written in Python. No third-party packages are needed.

## Rules

| Choice | Key | Beats |
|---|---|---|
| Snake | `s` | Water (snake drinks it) |
| Water | `w` | Gun (water douses it) |
| Gun | `g` | Snake (gun kills it) |

Same choice on both sides is a tie.

## Run it

Requires Python 3.8+.

```bash
git clone https://github.com/Hammad-Ahmed-hk/Snake_Water_Gun_Game..git
cd Snake_Water_Gun_Game.
python snake_water_Gun_Game.py
```

After each round you can choose to play again.

## Changes from the first version

- Fixed a rule bug: the computer's gun beating your snake was reported as a player win.
- Rules are now a small lookup table instead of nine `elif` branches, so they are easy to check.
- Added replay and clearer messages that show both choices.

## Author

Hammad Ahmed, [@Hammad-Ahmed-hk](https://github.com/Hammad-Ahmed-hk)
