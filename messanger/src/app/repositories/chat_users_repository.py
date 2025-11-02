from sqlalchemy.ext.asyncio import AsyncSession
from src.app.dao.base import SQLAlchemyRepository
from src.app.models.chat_users import ChatUsers

class ChatUserRepository(SQLAlchemyRepository):
    model = ChatUsers
