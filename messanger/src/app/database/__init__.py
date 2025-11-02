from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker
from src.core.database_config import db_settings

async_engine = create_async_engine(
    url=db_settings.DATABASE_URL,
    echo=False
)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

        
async def get_session():
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session

DbSession = Annotated[AsyncSession, Depends(get_session)]


    