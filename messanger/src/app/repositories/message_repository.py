from src.app.dao.base import SQLAlchemyRepository
from src.app.models.message import Message

class MessageRepository(SQLAlchemyRepository):
    model = Message
