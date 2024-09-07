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
    SUMMARY: str = "Rosa is a REST API for a simple, modular, customisable and fast CMS."
    DESCRIPTION: str = """
    Rosa
    ===

    ---

    Rosa is the backend for a simple, modular, customisable and fast CMS.

    It is built on the following design principles.

    - Customisable
    - Quick responding
    - Flexible with load
    - Minimalistic
    - Extendable
    - Maintainable
    - Fully open source
    - Full test coverage
    - Fully typed
    - Fully documented
    - Compliance to PEP8, PEP257, and PEP484 guidelines

    You can use it as the backend of your own project or to create your own custom CMS.

    """
    VERSION: str = "v1"


class ArticleConfig:
    """Article configurations."""

    DEFAULT_FETCHABLE_ARTICLES: int = 10
    MAX_FETCHABLE_ARTICLES: int = 100
    MIN_FETCHABLE_ARTICLES: int = 1
