# Asteroids

A small, classic-style Asteroids game implemented in Python using Pygame.

**Overview**
- **Project**: A minimal implementation of the arcade game Asteroids.
- **Language**: Python
- **Graphics**: Pygame
- **Purpose**: Playable demo, learning project for game programming and sprite/collision management.

**Features**
- **Player ship**: rotate, thrust, and shoot.
- **Asteroids**: spawn over time, break into smaller pieces when shot.
- **Simple collision handling**: player-asteroid and shot-asteroid interactions.
- **Logging**: game events and periodic state dumps are written to JSONL files for analysis.

**Requirements**
- **Python**: `>=3.12` (as declared in `pyproject.toml`)
- **Dependencies**: `pygame==2.6.1`

**Quick Install**
1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the dependency (either from `pyproject.toml` or directly):

```bash
python -m pip install --upgrade pip
python -m pip install pygame==2.6.1
# Or install the project (will install dependencies declared):
python -m pip install -e .
```

**Run the Game**

From the project root run:

```bash
python main.py
```

You should see the game window open at `1280x720` (values from `constants.py`). The game loop runs at roughly 60 FPS.

**Controls**
- **Rotate**: (left/right arrow keys or A/D depending on implementation) — check `player.py` for actual key handling.
- **Thrust / Move**: (up arrow or W)
- **Shoot**: (space bar)
- **Quit**: close the window or use standard OS window controls

If the exact keys are important for your use-case, open `player.py` to see how input is processed and mapped to actions.

**Files of Interest**
- `main.py`: game entry point and main loop.
- `player.py`: player ship implementation and shooting logic.
- `asteroid.py`, `asteroidfield.py`: asteroid objects and spawning logic.
- `shot.py`: projectile implementation.
- `constants.py`: screen size, speeds, radii, and tuning parameters.
- `logger.py`: writes `game_events.jsonl` and `game_state.jsonl` for events and periodic state dumps.

**Logging / Telemetry**
- `game_events.jsonl`: event stream (e.g., `player_hit`, `asteroid_shot`).
- `game_state.jsonl`: periodic game-state snapshots produced by `log_state()`.

These JSONL files are appended to as the game runs and can be parsed with standard JSONL utilities for debugging or analytics.

**Development Notes**
- The code uses Pygame sprite groups and simple bounding/circle collision checks. Constants in `constants.py` are tuned for playable behavior; tweak them to adjust difficulty and feel.
- The project is intentionally minimal and structured for learning — consider the following enhancements:
	- Add sound effects and music.
	- Improve collision response and add player lives / scoring.
	- Add unit tests for non-Pygame logic (e.g., asteroid splitting math).
	- Package as an executable with `pyinstaller` for distribution.

**Running from Source**
- Ensure your working directory is the project root (contains `main.py`).
- Run with the virtualenv activated to avoid system-wide package conflicts.

**Contributing**
- Fork the repository and open a pull request for bug fixes and enhancements.
- Keep changes focused and add tests for any pure logic you extract from the Pygame loop.

**Future Plans**
- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

