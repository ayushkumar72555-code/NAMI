from pydantic import BaseModel


class CommandResponse(BaseModel):
    status: str
    reply: str