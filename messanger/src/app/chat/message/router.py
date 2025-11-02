from fastapi import APIRouter, status, BackgroundTasks
from src.app.database import DbSession
from src.app.auth.dependencies import CurrentUser
from .schemes import CreateMessageRequest
from .message_service import MessageService
from src.app.websocket.manager import ws_manager

message_router = APIRouter()

@message_router.post(
    "/chats/{chat_id}/messages",
    status_code=status.HTTP_201_CREATED
)
async def create_chat_message(
    session: DbSession,
    background_tasks: BackgroundTasks,
    user: CurrentUser,
    chat_id: int,
    message_data: CreateMessageRequest
):
    posted_message = await MessageService(session).post_message(user.user_id, chat_id, message_data)
    # background_tasks.add_task(ws_manager.broadcast_to_chat, session, chat_id, message_data)
    await ws_manager.broadcast_to_chat(session, chat_id, posted_message.model_dump())
    return posted_message

@message_router.get(
    "/chats/{chat_id}/messages",
)
async def get_chat_messages(
    session: DbSession,
    user: CurrentUser,
    chat_id: int
):
    messages = await MessageService(session).get_chat_messages(user.user_id, chat_id)
    return messages