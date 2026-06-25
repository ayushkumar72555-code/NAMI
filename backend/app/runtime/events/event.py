from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True)
class Event:
    name: str
    payload: dict[str, Any]
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))