from datetime import datetime
from sqlalchemy import DateTime, Enum, String, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.app.database import Base
import enum

class UserRights(enum.Enum):
    GOD = "GOD"
    ADMIN = "ADMIN" 
    USER = "USER"

class ChatUsers(Base):
    __tablename__ = "chat_users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat_rooms.chat_id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    rights: Mapped[UserRights] = mapped_column(
        Enum(UserRights), 
        default=UserRights.USER,
        nullable=False
    )
    joined_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now, 
        nullable=False
    )