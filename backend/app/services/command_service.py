from app.schemas.command import CommandRequest
from app.schemas.response import CommandResponse
from app.services.agent_service import AgentService


class CommandService:
    def __init__(self) -> None:
        self.agent = AgentService()

    def execute(self, command: CommandRequest) -> CommandResponse:
        return self.agent.process(command.message)