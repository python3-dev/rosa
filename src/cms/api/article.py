"""Article routes."""

from fastapi import APIRouter, Query, status
from fastapi.responses import ORJSONResponse
from src.cms.services.articles import fetch_latest_articles_from_db
from src.core.config.api import ArticleConfig

article = APIRouter(
    prefix="/article",
    tags=["article"],
    default_response_class=ORJSONResponse,
)


@article.get(
    path="/",
    response_class=ORJSONResponse,
    tags=["article"],
    summary="List all articles in reverse chronological order.",
    description="Get the list of all articles ordered in reverse chronological order.",
    deprecated=False,
    name="Article",
    status_code=status.HTTP_200_OK,
)
def fetch_articles(
    fetch_count: int = Query(
        default=ArticleConfig.DEFAULT_FETCHABLE_ARTICLES,
        alias="fetch_count",
        le=ArticleConfig.MAX_FETCHABLE_ARTICLES,
        ge=ArticleConfig.MIN_FETCHABLE_ARTICLES,
    ),
) -> ORJSONResponse:
    """
    Fetch articles and return.

    Parameters
    ----------
    fetch_count : int, optional
        Number of articles to fetch, by default 10.

    Returns
    -------
    ORJSONResponse
        Returns list of articles in reverse chronological order.
    """
    if fetch_count > ArticleConfig.MAX_FETCHABLE_ARTICLES:
        fetch_count = ArticleConfig.MAX_FETCHABLE_ARTICLES
    elif fetch_count < ArticleConfig.MIN_FETCHABLE_ARTICLES:
        fetch_count = ArticleConfig.MIN_FETCHABLE_ARTICLES

    articles = fetch_latest_articles_from_db(n=fetch_count)
    return ORJSONResponse(content=articles)
