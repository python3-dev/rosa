"""Category services."""

from collections.abc import Sequence

from sqlalchemy import ScalarResult, Select, desc, select
from src.cms.models import Article, Category
from src.core.database.db import DatabaseSessionManager


async def fetch_categories_from_db(n: int = 10) -> Sequence[Category]:
    """Fetch 'n' categories sorted by order index."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Category] = await session.scalars(
            select(Category)
            .order_by(
                desc(Category.order),
            )
            .limit(n),
        )
        return result.fetchall()

async def fetch_category_by_id(category_id: int) -> Category | None:
    """Fetch a category by its ID."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Category] =  await session.scalars(
            select(Category).where(Category.id == category_id),
        )
        if result is None:
            raise ValueError
        return result.first()


async def fetch_category_by_slug(category_slug: str) -> Category | None:
    """Fetch a category by its slug."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_: Select[tuple[Category]] = select(Category).where(
            Category.slug == category_slug,

        )
        return (await session.execute(query_)).scalars().first()

async def fetch_articles_by_category(category_slug: str) -> Sequence[Article] | None:
    """Fetch an article by its slug."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_: Select[tuple[Article]] = select(Article).where(
            Article.category_id == select(Category.id).where(Category.slug == category_slug),
        ).order_by(
                desc(Article.published_date),
            )
        return (await session.execute(query_)).scalars().all()


async def get_category_id(category_slug: str) -> int | None:
    """Get category id."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_: Select[tuple[int]] = select(Category.id).where(Category.slug == category_slug)
        return (await session.execute(query_)).scalar()


async def update_category(category: Category) -> None:
    """Update a category."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(category)
        await session.commit()

async def create_category(category: Category) -> None:
    """Create a category."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(category)
        await session.commit()


async def delete_category(category: Category) -> None:
    """Delete an article."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        await session.delete(category)
        await session.commit()

