from sqlalchemy.orm import mapped_column, Mapped
from src.app.database import Base

class User(Base):
    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] 
    username: Mapped[str] = mapped_column(None, nullable=True)
    password: Mapped[str]