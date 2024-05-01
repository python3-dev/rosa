"""API Config."""

from typing import ClassVar


class APIConfig:
    """API configurations."""

    CORS_ORIGINS: ClassVar[list[str]] = [
        "http://127.0.0.1:8000/",
        "https://127.0.0.1:8000/",
        "http://127.0.0.1:8000/*",
        "https://127.0.0.1:8000/*",
        "http://locahost:8000/",
        "https://localhost:8000/",
    ]

    TITLE: str = "rosa"
    DESCRIPTION: str = "Rosa is a simple, modular, customisable and fast CMS."
    VERSION: str = "v1"
