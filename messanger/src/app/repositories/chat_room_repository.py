from sqlalchemy.ext.asyncio import AsyncSession
from src.app.dao.base import SQLAlchemyRepository
from src.app.models.chat_room import ChatRoom

class ChatRoomRepository(SQLAlchemyRepository):
    model = ChatRoom