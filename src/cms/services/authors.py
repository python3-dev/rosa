"""Author services."""

from collections.abc import Sequence

from sqlalchemy import ScalarResult, Select, desc, select
from sqlalchemy.orm import joinedload
from src.cms.models import Article, Author
from src.core.database.db import DatabaseSessionManager


async def fetch_authors_from_db() -> Sequence[Author]:
    """Fetch 'n' authors from databased sorted by first name."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Author] = await session.scalars(
            select(Author)
            .order_by(
                Author.first_name,
            ),
        )
        return result.fetchall()

async def fetch_author_by_id(author_id: int) -> Author | None:
    """Fetch a author by its ID."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Author] =  await session.scalars(
            select(Author).where(Author.id == author_id),
        )
        if result is None:
            raise ValueError
        return result.first()


async def fetch_author_by_slug(author_slug: str) -> Author | None:
    """Fetch a category by its slug."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_: Select[tuple[Author]] = select(Author).where(
            Author.slug == author_slug,

        )
        return (await session.execute(query_)).scalars().first()

async def fetch_articles_by_author(author_slug: str) -> Sequence[Article] | None:
    """Fetch an articles by an author."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_ = (
            select(Author)
            .options(joinedload(Author.articles))
            .where(Author.slug == author_slug)
            .order_by(
                desc(Article.published_date),
            )
        )

        author: Author | None = (await session.execute(query_)).scalars().first()
        if author is None:
            raise ValueError
        return author.articles


async def get_author_id(author_slug: str) -> int | None:
    """Get category id."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_: Select[tuple[int]] = select(Author.id).where(Author.slug == author_slug)
        return (await session.execute(query_)).scalar()


async def update_author(author: Author) -> None:
    """Update a author."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(author)
        await session.commit()

async def create_author(author: Author) -> None:
    """Create a author."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(author)
        await session.commit()


async def delete_author(author: Author) -> None:
    """Delete an article."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        await session.delete(author)
        await session.commit()

