from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.chat_room_repository import ChatRoomRepository
from .schemes import CreateRoomRequest

class ChatRoomService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.chat_repo = ChatRoomRepository(session)

    async def create_room(self, user_id: int, room_data: CreateRoomRequest):
        chat_room = await self.chat_repo.create(room_data, owner_id=user_id)
        return chat_room