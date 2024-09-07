"""Articles services."""

from collections.abc import Sequence

from sqlalchemy import ScalarResult, Select, desc, select
from src.cms.models.article import Article
from src.cms.models.category import Category
from src.core.database.db import DatabaseSessionManager


async def fetch_latest_articles_from_db(n: int) -> Sequence[Article]:
    """Fetch 'n' articles sorted by reverse-chronological order of 'published_date'."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Article] = await session.scalars(
            select(Article)
            .order_by(
                desc(Article.published_date),
            )
            .limit(n),
        )
        return result.fetchall()

async def fetch_article_by_id(article_id: int) -> Article | None:
    """Fetch an article by its ID."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Article] =  await session.scalars(
            select(Article).where(Article.id == article_id),
        )
        if result is None:
            raise ValueError
        return result.first()


async def fetch_article_by_slug(category_slug: str, article_slug: str) -> Article | None:
    """Fetch an article by its slug."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_: Select[tuple[Article]] = select(Article).where(
            Article.slug == article_slug,
            Article.category_id == select(Category.id).where(Category.slug == category_slug),
        )
        return (await session.execute(query_)).scalars().first()


async def get_category_id(category: str) -> int | None:
    """Get category id."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        stmt = select(Category.id).where(Category.slug == category)
        return (await session.execute(stmt)).scalar()


async def update_article(article: Article) -> None:
    """Update an article."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(article)
        await session.commit()

async def create_article(article: Article) -> None:
    """Create an article."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(article)
        await session.commit()


async def delete_article(article: Article) -> None:
    """Delete an article."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        await session.delete(article)
        await session.commit()

