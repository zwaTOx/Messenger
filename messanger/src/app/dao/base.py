from typing import Any, Dict
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel

class SQLAlchemyRepository:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, **filters: Dict[str, Any]):
        query = select(self.model)
        for field, value in filters.items():
            if hasattr(self.model, field):
                query = query.where(getattr(self.model, field) == value)
        result = await self.session.execute(query)
        return result.scalars().first()
    
    async def get_all(self, **filters: Dict[str, Any]):
        query = select(self.model)
        for field, value in filters.items():
            if hasattr(self.model, field):
                query = query.where(getattr(self.model, field) == value)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, **extra_fields: Dict[str, Any]):
        instance = self.model(**extra_fields)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def update(self, id: int, data: BaseModel):
        instance = await self.get(id)
        if instance:
            update_data = data.model_dump(exclude_none=True)
            for key, value in update_data.items():
                setattr(instance, key, value)
            await self.session.commit()
            await self.session.refresh(instance)
        return instance

    async def delete(self, id: int):
        instance = await self.get(id)
        if not instance:
            return False
        await self.session.delete(instance)
        await self.session.commit()
        return True