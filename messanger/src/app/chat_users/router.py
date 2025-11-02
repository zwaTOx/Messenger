from fastapi import APIRouter
from src.app.database import DbSession
from src.app.auth.dependencies import CurrentUser
from .schemes import InviteUserRequest

chat_users_router = APIRouter()

@chat_users_router.post(
    "/chats/{chat_id}/invite"
)
async def invite_user_in_chat(
    user: CurrentUser,
    session: DbSession,
    chat_id: int,
    inv_user_data: InviteUserRequest
):
    pass