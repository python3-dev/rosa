"""Unit tests for SQLAlchemy models."""

import asyncio

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.connection import engine
from src.cms.models import Article, Base, Category
from src.authentication.models import User


@pytest.fixture(scope="module", autouse=True)
def setup_db():
    """Set up and teardown."""

    async def init_models() -> None:
        """Create all tables in the database in asyncmode."""
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_models() -> None:
        """Drop all tables in the database in asyncmode."""
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    asyncio.run(init_models())

    yield

    asyncio.run(drop_models())


@pytest.fixture
async def db_connection():
    """Database session."""
    async with AsyncSession(engine) as session:
        return session
        # async with session.begin():
        #     # Create a new user
        #     new_user = User(name="John Doe", email="john@gmail.com")
        #     session.add(new_user)


@pytest.fixture
async def category(db_connection: AsyncSession) -> Category:
    """Create category."""
    category = Category(name="sample", description="sample")
    async with db_connection.begin():
        db_connection.add(category)
        await db_connection.commit()
    return category


@pytest.fixture
async def user(db_connection: AsyncSession) -> User:
    """Create category."""
    user = User(name="pratheesh", email="pratheesh@gmail.com", password_hash="asdasdaq2e")
    async with db_connection.begin():
        db_connection.add(user)
        await db_connection.commit()
    return user


@pytest.mark.asyncio
async def test_article_creation(
    db_connection: AsyncSession,
    category: Category,
    user: User,
) -> None:
    """Test article creation."""
    category_: Category = category
    article_data = {
        "title": "Test Article",
        "description": "Test article description",
        "published_date": "2024-05-01 12:00:00",
        "category_id": 1,
        "primary_image": "test_image.jpg",
        "body": "Test article body",
        "is_featured": True,
        "slug": "test-article",
    }

    article = Article(**article_data)
    async with db_connection.begin():
        db_connection.add(article)
        await db_connection.flush()

    assert article.id is not None


@pytest.mark.asyncio
async def test_article_retrieval(db_connection):
    """Test get article."""
    article_data = {
        "title": "Test Article",
        "description": "Test article description",
        "published_date": "2024-05-01 12:00:00",
        "category_id": 1,
        "primary_image": "test_image.jpg",
        "body": "Test article body",
        "is_featured": True,
        "slug": "test-article",
        "user_id": 1,
    }
    article = Article(**article_data)
    db_connection.add(article)
    await db_connection.commit()

    fetched_article = await db_connection.get(Article, article.id)

    assert fetched_article is not None
    assert fetched_article.title == article.title
