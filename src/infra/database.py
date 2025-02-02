from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field, InitVar
from typing import Any

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)


@dataclass
class Database:
    url: InitVar[str]

    _async_engine: AsyncEngine = field(init=False)
    _async_session: async_sessionmaker[AsyncSession] = field(init=False)

    def __post_init__(self, url: str) -> None:
        self._async_engine = create_async_engine(
            url=url,
            pool_pre_ping=False,
            echo=False,
        )
        self._async_session = async_sessionmaker(
            bind=self._async_engine,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_async_session(self) -> AsyncGenerator[AsyncSession, Any]:
        async_session: AsyncSession = self._async_session()
        try:
            yield async_session
        except SQLAlchemyError:
            await async_session.rollback()
            raise
        finally:
            await async_session.commit()
            await async_session.close()
