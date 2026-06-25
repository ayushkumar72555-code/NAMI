from app.schemas.response import CommandResponse


class AgentService:
    def process(self, message: str) -> CommandResponse:
        return CommandResponse(
            status="success",
            reply=f"I received your command: '{message}'",
        )