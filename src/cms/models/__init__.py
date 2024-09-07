"""CMS models definitions."""

from sqlalchemy import Column, ForeignKey, Table
from src.authentication.models import User
from src.core.database.db import Base

from .article import Article
from .author import Author
from .category import Category
from .image import Image
from .language import Language
from .tag import Tag
