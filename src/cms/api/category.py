"""Category routes."""

from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse
from src.cms.services.categories import fetch_articles_by_category, fetch_categories_from_db

category = APIRouter(
    prefix="/category",
    tags=["category"],
    default_response_class=ORJSONResponse,
)


@category.get(
    path="/",
    response_class=ORJSONResponse,
    tags=["category"],
    summary="Get a list of all categories ordered by their order index.",
    description="Get a list of all categories ordered by their order index.",
    deprecated=False,
    name="Category",
    status_code=status.HTTP_200_OK,
)
def fetch_categories() -> ORJSONResponse:
    """
    Fetch categories and return.

    Parameters
    ----------
    fetch_count : int, optional
        Number of categories to fetch, by default 10.

    Returns
    -------
    ORJSONResponse
        Returns list of categories in order of their index.
    """
    categories = fetch_categories_from_db()
    return ORJSONResponse(content=categories)


@category.get(
    path="/{category_name}/",
    response_class=ORJSONResponse,
    tags=["category", "article"],
    summary="List all articles in reverse chronological order.",
    description="Get the list of all articles ordered in reverse chronological order.",
    deprecated=False,
    name="Category-wise articles",
    status_code=status.HTTP_200_OK,
)
def fetch_articles(category_name: str) -> ORJSONResponse:
    """
    Fetch articles by category and return.

    Parameters
    ----------
    fetch_count : int, optional
        Number of articles to fetch, by default 10.

    Returns
    -------
    ORJSONResponse
        Returns list of articles in reverse chronological order.
    """
    articles = fetch_articles_by_category(category_slug=category_name)
    return ORJSONResponse(content=articles)
