from dataclasses import dataclass


@dataclass(slots=True)
class WorldState:
    active_window: str | None = None
    explorer_path: str | None = None