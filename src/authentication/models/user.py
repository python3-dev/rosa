"""User model."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import INTEGER, TEXT
from src.core.database.db import Base


class User(Base):
    """User schema."""

    __tablename__: str = "user"

    id: Mapped[int] = mapped_column(
        name="id",
        primary_key=True,
        autoincrement="auto",
        type_=INTEGER,
    )
    name: Mapped[str] = mapped_column(
        name="username",
        type_=TEXT,
        nullable=False,
        unique=True,
    )

    email: Mapped[str] = mapped_column(
        name="email",
        type_=TEXT,
        nullable=False,
        unique=True,
    )

    is_superuser: Mapped[bool] = mapped_column(default=False)

    password_hash: Mapped[str] = mapped_column(
        name="password_hash",
        type_=TEXT,
        nullable=False,
    )

    published_article_id: Mapped[int] = mapped_column(
        ForeignKey("article.id"),
        type_=INTEGER,
        nullable=True,
    )
