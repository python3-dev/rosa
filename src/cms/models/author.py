"""Author model definition."""

from typing import Any

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from sqlalchemy.types import INTEGER, TEXT
from src.core.database.db import Base

from .associations import article_author_association


class Author(Base):
    """Author schema."""

    __tablename__: str = "author"

    id: Mapped[int] = mapped_column(
        name="id",
        type_=INTEGER,
        primary_key=True,
        autoincrement=True,
    )

    first_name: Mapped[str] = mapped_column(
        name="first_name",
        type_=TEXT,
    )

    last_name: Mapped[str] = mapped_column(
        name="last_name",
        type_=TEXT,
    )
    biography: Mapped[str] = mapped_column(
        name="biography",
        type_=TEXT,
    )
    photo_url: Mapped[str] = mapped_column(
        name="photo_url",
        type_=TEXT,
    )
    email: Mapped[str] = mapped_column(
        name="email",
        type_=TEXT,
    )
    website: Mapped[str] = mapped_column(
        name="website",
        type_=TEXT,
        nullable=True,
    )

    slug: Mapped[str] = mapped_column(
        name="slug",
        type_=TEXT,
        nullable=False,
        unique=True,
    )

    articles: _RelationshipDeclared[Any] = relationship(
        "Article",
        secondary=article_author_association,
        back_populates="authors",
    )


