"""Tag services."""

from collections.abc import Sequence

from sqlalchemy import ScalarResult, Select, desc, select
from sqlalchemy.orm import joinedload
from src.cms.models import Article, Tag
from src.core.database.db import DatabaseSessionManager


async def fetch_tags_from_db(n: int = 10) -> Sequence[Tag]:
    """Fetch 'n' tags."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Tag] = await session.scalars(
            select(Tag)
            .limit(n),
        )
        return result.fetchall()

async def fetch_tag_by_id(tag_id: int) -> Tag | None:
    """Fetch a tag by its ID."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        result: ScalarResult[Tag] =  await session.scalars(
            select(Tag).where(Tag.id == tag_id),
        )
        if result is None:
            raise ValueError
        return result.first()


async def fetch_tag_by_slug(tag_slug: str) -> Tag | None:
    """Fetch a tag by its slug."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_: Select[tuple[Tag]] = select(Tag).where(
            Tag.slug == tag_slug,

        )
        return (await session.execute(query_)).scalars().first()

async def fetch_articles_by_tag(tag_slug: str) -> Sequence[Article] | None:
    """Fetch an article by its slug."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_ = (
            select(Tag)
            .options(joinedload(Tag.articles))
            .where(Tag.slug == tag_slug)
            .order_by(
                desc(Article.published_date),
            )
        )

        tag_: Tag | None = (await session.execute(query_)).scalars().first()
        if tag_ is None:
            raise ValueError
        return tag_.articles


async def get_tag_id(tag_slug: str) -> int | None:
    """Get tag id."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        query_ = select(Tag.id).where(Tag.slug == tag_slug)
        return (await session.execute(query_)).scalar()


async def update_tag(tag: Tag) -> None:
    """Update a tag."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(tag)
        await session.commit()

async def create_tag(tag: Tag) -> None:
    """Create a Tag."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        session.add(tag)
        await session.commit()


async def delete_tag(tag: Tag) -> None:
    """Delete a Tag."""
    db_session = DatabaseSessionManager()
    db_session.connect()
    async with db_session.session() as session:
        await session.delete(tag)
        await session.commit()

