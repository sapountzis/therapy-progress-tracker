from datetime import datetime
from typing import Any, Optional

from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, Relationship, SQLModel


class ClientModel(SQLModel, table=True):
    __tablename__ = "client"

    id: Optional["int"] = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={"autoincrement": "auto"},
    )
    name: str = Field(unique=True)
    sessions: list["TherapySessionModel"] = Relationship(back_populates="client")


class TherapySessionModel(SQLModel, table=True):
    __tablename__ = "session"

    id: Optional["int"] = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={"autoincrement": "auto"},
    )
    session_data: dict[str, Any] = Field(default_factory=dict, sa_type=JSONB)
    timestamp: datetime = Field(default_factory=datetime.now)

    client_id: int = Field(foreign_key="client.id")
    client: Optional["ClientModel"] = Relationship(back_populates="sessions")
