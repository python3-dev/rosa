"""Database model associations."""

from sqlalchemy import Column, ForeignKey, Table
from src.core.database.db import Base

article_author_association = Table(
    "article_author_association",
    Base.metadata,
    Column("article_id", ForeignKey("article.id"), primary_key=True),
    Column("author_id", ForeignKey("author.id"), primary_key=True),
)

article_tag_association = Table(
    "article_tag_association",
    Base.metadata,
    Column("article_id", ForeignKey("article.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)
