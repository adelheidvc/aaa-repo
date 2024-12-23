from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class SQLiteBase(DeclarativeBase):
    """
    Base class for ORM
    """

engine = create_engine(
    "sqlite:///aaa.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Log generated SQL
)