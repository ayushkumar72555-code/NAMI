from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(slots=True)
class Session:
    id: str = field(default_factory=lambda: str(uuid4()))
    goal: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))