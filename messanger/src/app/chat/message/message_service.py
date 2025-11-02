from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.message_repository import MessageRepository
from src.app.chat.chat_users.chat_users_service import ChatUserRepository
from .schemes import CreateMessageRequest
from src.app.exceptions.chat_exceptions import PermissionException 

class MessageService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.message_repo = MessageRepository(session)

    async def post_message(self, user_id: int, chat_id: int, message_data: CreateMessageRequest):
        chat_member = await ChatUserRepository(self.session).get(user_id=user_id, chat_id=chat_id)
        if not chat_member:
            raise PermissionException
        message = await self.message_repo.create(
            chat_id=chat_id,
            user_id=user_id,
            message=message_data.message
        )
        return message
    
    async def get_chat_messages(self, user_id: int, chat_id: int):
        chat_member = await ChatUserRepository(self.session).get(user_id=user_id, chat_id=chat_id)
        if not chat_member:
            raise PermissionException
        return await self.message_repo.get_all(chat_id=chat_id)