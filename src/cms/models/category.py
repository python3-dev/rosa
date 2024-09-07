"""Category model definition."""

from typing import Any

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from sqlalchemy.types import INTEGER, TEXT
from src.core.database.db import Base


class Category(Base):
    """Category schema."""

    __tablename__: str = "category"

    id: Mapped[int] = mapped_column(
        name="id",
        type_=INTEGER,
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        name="name",
        type_=TEXT,
    )
    order: Mapped[int] = mapped_column(
        name="order",
        type_=INTEGER,
        default=0,
        nullable=False,
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
        backref="categories",
    )
