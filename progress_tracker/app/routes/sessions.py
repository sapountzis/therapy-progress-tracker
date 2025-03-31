from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.responses import JSONResponse
from sqlmodel import Session, desc, select

from app.dependencies import get_session
from app.models.db_models import TherapySessionModel
from app.schemas import TherapySessionSummary

router = APIRouter(prefix="/api")


@router.post("/sessions", response_class=JSONResponse)
async def create_session(
    client_id: Annotated[int, Form()],
    session_file: Annotated[UploadFile, File()],
    db: Annotated[Session, Depends(get_session)],
):
    content = await session_file.read()
    session_data = TherapySessionSummary.model_validate_json(content)

    session = TherapySessionModel(
        client_id=client_id,
        session_data=session_data.model_dump(by_alias=True),
        timestamp=datetime.now(tz=timezone.utc),
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "id": session.id,
        "timestamp": session.timestamp.isoformat(),
        "client_id": session.client_id,
    }


@router.get("/clients/{client_id}/sessions", response_model=list[dict])
async def get_sessions(
    client_id: int,
    db: Annotated[Session, Depends(get_session)],
):
    statement = (
        select(TherapySessionModel)
        .where(
            TherapySessionModel.client_id == client_id,
        )
        .order_by(desc(TherapySessionModel.timestamp))
    )

    sessions = db.exec(statement).all()

    return [
        {
            "id": session.id,
            "timestamp": session.timestamp.isoformat(),
            "data": TherapySessionSummary.model_validate(
                session.session_data,
            ).model_dump(),
        }
        for session in sessions
    ]
