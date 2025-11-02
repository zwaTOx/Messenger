from src.app.models.timestamp import TimeStampMixin
from src.app.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, Text

class Message(Base, TimeStampMixin):
    __tablename__ = "messages"
    message_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat_rooms.chat_id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    message: Mapped[int] = mapped_column(Text, nullable=False)
    