from collections.abc import Generator

from sqlmodel import Session, create_engine

from app.core.settings import get_settings

settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL,
)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    from app.models.db_models import SQLModel

    SQLModel.metadata.create_all(engine)
