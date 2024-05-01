"""FastAPI server."""

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from src.core.config.api import APIConfig

app = FastAPI(
    title=APIConfig.TITLE,
    version=APIConfig.VERSION,
    description=APIConfig.DESCRIPTION,
    default_response_class=ORJSONResponse,
    docs_url=f"/{APIConfig.VERSION}/docs",
    redoc_url=f"/{APIConfig.VERSION}/redoc",
    openapi_url=f"/{APIConfig.VERSION}/openapi.json",
)

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=APIConfig.CORS_ORIGINS,
)


@app.get(
    f"/{APIConfig.VERSION}/",
    status_code=status.HTTP_200_OK,
    response_class=ORJSONResponse,
)
def home(request: Request) -> ORJSONResponse:
    """Home route."""
    return ORJSONResponse(content={"content": "successful response."})
