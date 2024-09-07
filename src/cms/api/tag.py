"""Tag routes."""

from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

tag = APIRouter(
    prefix="/tag",
    tags=["tag"],
    default_response_class=ORJSONResponse,
)



@tag.get(
    path="/{tag_name}/",
    response_class=ORJSONResponse,
    tags=["tag", "article"],
    summary="List all articles in reverse chronological order.",
    description="Get the list of all articles ordered in reverse chronological order.",
    deprecated=False,
    name="Tag-wise articles",
    status_code=status.HTTP_200_OK,
)
def fetch_articles(category_name: str) -> ORJSONResponse:
    """
    Fetch articles by tag and return.

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
