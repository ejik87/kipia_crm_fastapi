from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import settings

# Common interaction with database
# create async engine
engine = create_async_engine(settings.REAL_DATABASE_URL,
                             future=True, echo=True, execution_options={"isolation_level": "AUTOCOMMIT"})
# create session for interaction with database
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
