"""Database related routines."""

import os

import orjson
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine

load_dotenv()


def orjson_serialiser(object_: object) -> str:
    """User orjson to serialise."""
    return orjson.dumps(object_).decode()


db_uri: str | None = os.getenv("DB_URI")

if db_uri is None:
    raise FileNotFoundError
else:
    engine: AsyncEngine = create_async_engine(
        url=db_uri,
        json_deserializer=orjson.loads,
        json_serializer=orjson_serialiser,
    )
