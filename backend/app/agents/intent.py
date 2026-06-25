from dataclasses import dataclass


@dataclass(slots=True)
class Intent:
    user_message: str
    objective: str