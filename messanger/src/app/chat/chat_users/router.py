from fastapi import APIRouter
from src.app.database import DbSession
from src.app.auth.dependencies import CurrentUser
from .schemes import InviteUserRequest
from .chat_users_service import ChatUsersService

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
    member = await ChatUsersService(session).invite_user(user.user_id, chat_id, inv_user_data)
    return member

@chat_users_router.get(
    "/chats/{chat_id}/members"
)
async def get_chat_members(
    user: CurrentUser,
    session: DbSession,
    chat_id: int,
):
    members = await ChatUsersService(session).get_chat_members(user.user_id, chat_id)
    return members