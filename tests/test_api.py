"""Unit test cases for API endpoints."""

from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response
from main import rosa
from src.core.config.api import APIConfig

client = TestClient(rosa)


def test_home_endpoint() -> None:
    """Test case for home endpoint."""
    response: Response = client.get(f"/{APIConfig.VERSION}")
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "application/json"
    assert response.headers["content-length"] == "34"
    assert response.encoding == "utf-8"
    assert response.json() == {"content": "successful response."}


def test_articles_endpoint() -> None:
    """Test case for /articles endpoint."""
    response: Response = client.get(f"/{APIConfig.VERSION}/articles")
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "application/json"
    assert response.encoding == "utf-8"
