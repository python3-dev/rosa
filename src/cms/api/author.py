"""Author routes."""

from fastapi import APIRouter, Query, status
from fastapi.responses import ORJSONResponse
from src.cms.services.authors import fetch_articles_by_author, fetch_authors_from_db
from src.core.config.api import ArticleConfig

author = APIRouter(
    prefix="/author",
    tags=["author"],
    default_response_class=ORJSONResponse,
)


@author.get(
    path="/",
    response_class=ORJSONResponse,
    tags=["author"],
    summary="List all published authors.",
    description="List all published authors in the alphabetic order of their first name",
    deprecated=False,
    name="Author",
    status_code=status.HTTP_200_OK,
)
def fetch_authors(
    fetch_count: int = Query(
        default=ArticleConfig.DEFAULT_FETCHABLE_ARTICLES,
        alias="fetch_count",
        le=ArticleConfig.MAX_FETCHABLE_ARTICLES,
        ge=ArticleConfig.MIN_FETCHABLE_ARTICLES,
    ),
) -> ORJSONResponse:
    """
    Fetch authors and return.

    Parameters
    ----------
    fetch_count : int, optional
        Number of authors to fetch, by default 10.

    Returns
    -------
    ORJSONResponse
        Returns list of authors in alphabetical order.
    """
    if fetch_count > ArticleConfig.MAX_FETCHABLE_ARTICLES:
        fetch_count = ArticleConfig.MAX_FETCHABLE_ARTICLES
    elif fetch_count < ArticleConfig.MIN_FETCHABLE_ARTICLES:
        fetch_count = ArticleConfig.MIN_FETCHABLE_ARTICLES

    authors = fetch_authors_from_db()
    return ORJSONResponse(content=authors)


@author.get(
    path="/{author_slug}/",
    response_class=ORJSONResponse,
    tags=["author", "article"],
    summary="List all articles in reverse chronological order.",
    description="Get the list of all articles ordered in reverse chronological order.",
    deprecated=False,
    name="Category-wise articles",
    status_code=status.HTTP_200_OK,
)
def fetch_articles(author_slug: str) -> ORJSONResponse:
    """
    Fetch articles by author and return.

    Parameters
    ----------
    fetch_count : int, optional
        Number of articles to fetch, by default 10.

    Returns
    -------
    ORJSONResponse
        Returns list of articles in reverse chronological order.
    """
    articles = fetch_articles_by_author(author_slug=author_slug)
    return ORJSONResponse(content=articles)
