from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Text
from src.app.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class ChatRoom(Base):
    __tablename__ = "chat_rooms"
    
    chat_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)  
    info: Mapped[str] = mapped_column(Text, nullable=True)  
    isPrivate: Mapped[bool] = mapped_column(default=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now,
        onupdate=datetime.now, 
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,  
        nullable=False
    )