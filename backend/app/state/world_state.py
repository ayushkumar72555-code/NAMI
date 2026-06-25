from dataclasses import dataclass


@dataclass(slots=True)
class WorldState:
    active_window: str | None = None
    current_directory: str | None = None