from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models.chat_users import UserRights
from src.app.repositories.chat_room_repository import ChatRoomRepository
from src.app.repositories.chat_users_repository import ChatUserRepository
from .schemes import CreateRoomRequest

class ChatRoomService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.chat_repo = ChatRoomRepository(session)

    async def create_room(self, user_id: int, room_data: CreateRoomRequest):
        chat_room = await self.chat_repo.create(**room_data.model_dump(), owner_id=user_id)
        await ChatUserRepository(self.session).create(user_id=user_id, chat_id = chat_room.chat_id, rights="GOD")
        return chat_room