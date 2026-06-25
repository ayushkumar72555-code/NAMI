from dataclasses import dataclass


@dataclass(slots=True)
class Intent:
    original_message: str
    objective: str