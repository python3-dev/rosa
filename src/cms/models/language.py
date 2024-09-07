"""Language model definition."""

from typing import Any

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.relationships import _RelationshipDeclared
from sqlalchemy.types import INTEGER, TEXT
from src.core.database.db import Base


class Language(Base):
    """Language schema."""

    __tablename__: str = "language"

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
    iso_code: Mapped[str] = mapped_column(
        name="iso_code",
        type_=TEXT,
        default="ml",
    )
    articles: _RelationshipDeclared[Any] = relationship(
        "Article",
        backref="languages",
    )
