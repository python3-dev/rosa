"""Tag model definition."""

from typing import Any

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from sqlalchemy.types import INTEGER, TEXT
from src.core.database.db import Base

from .associations import article_tag_association


class Tag(Base):
    """Tag schema."""

    __tablename__: str = "tag"

    id: Mapped[int] = mapped_column(
        name="id",
        type_=INTEGER,
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        name="name",
        type_=TEXT,
    )
    description: Mapped[str] = mapped_column(
        name="description",
        type_=TEXT,
    )

    slug: Mapped[str] = mapped_column(
        name="slug",
        type_=TEXT,
        nullable=False,
        unique=True,
    )

    articles: _RelationshipDeclared[Any] = relationship(
        "Article",
        secondary=article_tag_association,
        back_populates="tags",
    )
