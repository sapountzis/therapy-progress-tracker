from typing import Annotated, cast

from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.core.agent import Agent, OverallState, TherapySession
from app.dependencies import get_session
from app.models import TherapySessionModel
from app.schemas import TherapySessionSummary

router = APIRouter(prefix="/api")
templates = Jinja2Templates(directory="app/templates")


@router.post("/compare-sessions", response_class=JSONResponse)
async def compare_sessions(
    client_id: Annotated[int, Form()],
    session_ids: Annotated[list[int], Form()],
    db: Annotated[Session, Depends(get_session)],
):
    therapy_sessions = []
    for therapy_session_id in session_ids:
        session_stmt = select(TherapySessionModel).where(
            (TherapySessionModel.id == therapy_session_id)
            & (TherapySessionModel.client_id == client_id),
        )
        therapy_session_db = db.exec(session_stmt).first()
        if not therapy_session_db:
            return JSONResponse(
                status_code=404,
                content={"error": f"Session {therapy_session_id} not found"},
            )
        therapy_session: TherapySession = {
            "id": therapy_session_db.id or 0,
            "summary": TherapySessionSummary.model_validate(
                therapy_session_db.session_data,
            ),
            "timestamp": therapy_session_db.timestamp,
            "scores": [],
        }
        therapy_sessions.append(therapy_session)

    therapy_sessions = sorted(therapy_sessions, key=lambda x: x["timestamp"])

    state: OverallState = {
        "therapy_sessions": therapy_sessions,
    }

    agent = Agent()

    progress_result = cast(OverallState, await agent.compare_sessions(state))

    return {
        "session_dates": [session["timestamp"] for session in therapy_sessions],
        "progress": progress_result.get("progress_assessment", "Unknown"),
        "reason": progress_result.get("progress_assessment_reason", "Unknown"),
    }
