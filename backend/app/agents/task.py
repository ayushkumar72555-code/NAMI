from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    name: str
    description: str