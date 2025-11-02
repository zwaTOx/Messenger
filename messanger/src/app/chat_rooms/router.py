from fastapi import APIRouter
from src.app.database import DbSession
from src.app.auth.dependencies import CurrentUser
from .schemes import CreateRoomRequest, InviteUserRequest
from .chat_service import ChatRoomService

chat_rooms_router = APIRouter()

@chat_rooms_router.post(
    "/chats"
)
async def create_chat(
    user: CurrentUser,
    session: DbSession,
    chat_data: CreateRoomRequest
):
    room = await ChatRoomService(session).create_room(user.user_id, chat_data)
    return room

