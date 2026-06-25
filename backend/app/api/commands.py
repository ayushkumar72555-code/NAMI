from fastapi import APIRouter

from app.schemas.command import CommandRequest
from app.schemas.response import CommandResponse
from app.services.command_service import CommandService

router = APIRouter(prefix="/commands", tags=["Commands"])

service = CommandService()


@router.post("", response_model=CommandResponse)
async def execute_command(command: CommandRequest):
    return service.execute(command)