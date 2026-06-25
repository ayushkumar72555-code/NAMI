from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Event:
    type: str
    payload: dict
    timestamp: datetime = field(default_factory=datetime.utcnow)