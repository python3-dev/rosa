"""API routes."""

from .article import article
from .author import author
from .category import category

__all__: list[str] = [
    "article",
    "author",
    "category",
]
