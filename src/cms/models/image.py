"""Image model defintions."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import INTEGER, TEXT
from src.core.database.db import Base


class Image(Base):
    """Image schema."""

    __tablename__: str = "image"

    id: Mapped[int] = mapped_column(
        name="id",
        type_=INTEGER,
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(
        name="title",
        type_=TEXT,
    )
    description: Mapped[str] = mapped_column(
        name="description",
        type_=TEXT,
    )
    url: Mapped[str] = mapped_column(
        name="url",
        type_=TEXT,
    )
    article_id: Mapped[int] = mapped_column(
        ForeignKey("article.id"),
        type_=INTEGER,
    )
