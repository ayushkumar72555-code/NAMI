from dataclasses import dataclass


@dataclass(slots=True)
class Action:

    name: str

    description: str