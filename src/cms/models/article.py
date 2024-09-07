"""Article model definition."""

from datetime import datetime
from typing import Any

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from sqlalchemy.types import BOOLEAN, INTEGER, TEXT, TIMESTAMP
from src.core.database.db import Base

from .associations import article_author_association, article_tag_association


class Article(Base):
    """Article schema."""

    __tablename__: str = "article"

    id: Mapped[int] = mapped_column(
        name="id",
        primary_key=True,
        autoincrement="auto",
        type_=INTEGER,
        index=True,
    )
    title: Mapped[str] = mapped_column(
        name="title",
        type_=TEXT,
    )
    description: Mapped[str] = mapped_column(
        name="description",
        type_=TEXT,
    )
    published_date: Mapped[datetime] = mapped_column(
        name="published_date",
        type_=TIMESTAMP(timezone=True),
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id", ondelete="CASCADE"),
        type_=INTEGER,
        nullable=False,
    )
    language_id: Mapped[int] = mapped_column(
        ForeignKey("language.id", ondelete="CASCADE"),
        type_=INTEGER,
        nullable=False,
    )
    primary_image: Mapped[str] = mapped_column(
        name="primary_image",
        type_=TEXT,
    )
    body: Mapped[str] = mapped_column(
        name="body",
        type_=TEXT,
    )
    is_featured: Mapped[bool] = mapped_column(
        name="is_featured",
        type_=BOOLEAN,
    )
    slug: Mapped[str] = mapped_column(
        name="slug",
        type_=TEXT,
        nullable=False,
    )

    authors: _RelationshipDeclared[Any] = relationship(
        "Author",
        secondary=article_author_association,
        back_populates="articles",
        cascade="all, delete",
    )
    tags: _RelationshipDeclared[Any] = relationship(
        "Tag",
        secondary=article_tag_association,
        back_populates="articles",
    )

    optional_images: _RelationshipDeclared[Any] = relationship(
        "Image",
        backref="articles",
    )

    publisher: _RelationshipDeclared[Any] = relationship(
        "User",
        backref="user_articles",
    )
