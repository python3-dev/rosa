"""Unit test cases for API endpoints."""

from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from main import app
from src.core.config.api import APIConfig

client = TestClient(app)


def test_home_endpoint() -> None:
    """Test case."""
    response: Response = client.get(f"/{APIConfig.VERSION}")
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["content-type"] == "application/json"
    assert response.headers["content-length"] == "34"
    assert response.encoding == "utf-8"
    assert response.json() == {"content": "successful response."}
