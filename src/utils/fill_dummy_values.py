"""Fill dummy values in the database."""

import asyncio
import random
from datetime import datetime
from string import ascii_lowercase

from sqlalchemy import select
from src.authentication.models.user import User
from src.cms.models.article import Article
from src.core.database.db import DatabaseSessionManager


async def add_dummy_user() -> None:
    """
    Add a dummy user to the database.

    Returns
    -------
    None
    """
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        user = User(
            name="dummy_user",
            email="dummy_user@example.com",
            password_hash="asbaasdasdasdasdbasd1123213$!@#!@#ASDASD",
            is_superuser=False,
        )
        session.add(user)
        await session.commit()


async def add_dummy_entries(n: int) -> None:
    """
    Add 'n' number of random dummy entries to the article database.

    Parameters
    ----------
    n : int
        Number of dummy entries to add.

    Returns
    -------
    None
    """
    db_session = DatabaseSessionManager()
    async with db_session.connect() as connection:

        users = await connection.scalars(connection.execute(select(User))).fetchall()
        categories = await connection.scalars(
            connection.execute(select(Article.category_id).distinct()),
        ).fetchall()
        languages = await connection.scalars(
            connection.execute(select(Article.language_id).distinct()),
        ).fetchall()

        for _ in range(n):
            author_id = random.choice(users).id
            category_id = random.choice(categories).category_id
            language_id = random.choice(languages).language_id

            title: str = "".join(random.choice(ascii_lowercase) for _ in range(10))
            description: str = "".join(random.choice(ascii_lowercase) for _ in range(20))

            article = Article(
                title=title,
                description=description,
                published_date=datetime.now(),
                category_id=category_id,
                language_id=language_id,
                primary_image="",
                body="",
                is_featured=False,
                slug=title.lower().replace(" ", "-"),
                author_id=author_id,
            )
            await connection.add(article)


if __name__ == "__main__":
    asyncio.run(add_dummy_user())
