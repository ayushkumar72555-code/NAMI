from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    id: str
    title: str
    description: str