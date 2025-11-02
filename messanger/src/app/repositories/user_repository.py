from sqlalchemy.ext.asyncio import AsyncSession
from src.app.dao.base import SQLAlchemyRepository
from src.app.models.user import User

class UserRepository(SQLAlchemyRepository):
    model = User

    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, email: str, password: str) -> User:
        instance = self.model(email=email, password=password)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance