from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class SQLiteBase(DeclarativeBase):
    """
    Base class for ORM
    """


engine = create_engine(
    "sqlite:///aaa.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True,  # Log generated SQL
)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    """
    get database session
    """
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


DatabaseSession = Annotated[Session, Depends(get_session)]
