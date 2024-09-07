"""FastAPI server."""

import textwrap

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from src.core.config.api import APIConfig

rosa = FastAPI(
    title=APIConfig.TITLE,
    version=APIConfig.VERSION,
    summary=APIConfig.SUMMARY,
    description=textwrap.dedent(APIConfig.DESCRIPTION),
    default_response_class=ORJSONResponse,
    root_path=f"/{APIConfig.VERSION}",
    redirect_slashes=True,
)

rosa.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=APIConfig.CORS_ORIGINS,
)


@rosa.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_class=ORJSONResponse,
)
def home() -> ORJSONResponse:
    """Home route."""
    return ORJSONResponse(content={"content": "successful response."})


from src.cms.api import article, author, category

rosa.include_router(router=article)
rosa.include_router(router=author)
rosa.include_router(router=category)
