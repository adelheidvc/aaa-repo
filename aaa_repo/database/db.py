from sqlmodel import create_engine

engine = create_engine(
    "sqlite:///aaa.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Log generated SQL
)