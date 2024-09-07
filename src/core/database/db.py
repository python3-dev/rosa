"""Database session manager."""

import contextlib
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from src.core.exceptions import DatabaseSessionInitialisationError

from .connection import engine


class Base(DeclarativeBase):
    """SQLAlchemy declarative base."""


class DatabaseSessionManager:
    """Asynchronous database session manager."""

    def __init__(self) -> None:
        self._engine: AsyncEngine | None = engine
        self._sessionmaker: async_sessionmaker | None = async_sessionmaker(
            autocommit=False, bind=self._engine, class_=AsyncSession,
        )

    def initialise(self, host: str | None = None) -> None:
        """Initialise database session."""
        if self._engine is None:
            if host is None:
                raise DatabaseSessionInitialisationError
            self._engine = create_async_engine(host)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

    async def close(self) -> None:
        """Close database session."""
        if self._engine is None:
            raise DatabaseSessionInitialisationError
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        """Create database connection."""
        if self._engine is None:
            raise DatabaseSessionInitialisationError

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Create database session."""
        if self._sessionmaker is None:
            raise DatabaseSessionInitialisationError

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def create_all(self, connection: AsyncConnection) -> None:
        """Create all database tables."""
        await connection.run_sync(Base.metadata.create_all)

    async def drop_all(self, connection: AsyncConnection) -> None:
        """Drop all database tables."""
        await connection.run_sync(Base.metadata.drop_all)
