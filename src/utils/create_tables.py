"""Create tables."""

import asyncio

from src.authentication.models import *
from src.cms.models import *
from src.core.database.db import DatabaseSessionManager


async def init_tables() -> None:
    """Create all tables in the database in asyncmode."""
    db_session = DatabaseSessionManager()
    async with db_session.connect() as connection:
        await db_session.create_all(connection)


if __name__ == "__main__":
    asyncio.run(init_tables())
