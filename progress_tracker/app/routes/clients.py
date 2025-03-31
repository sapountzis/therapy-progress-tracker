from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.dependencies import get_session
from app.models.db_models import ClientModel, TherapySessionModel

router = APIRouter(prefix="/api")
templates = Jinja2Templates(directory="app/templates")


@router.get("/clients", response_class=JSONResponse)
async def get_clients(db: Annotated[Session, Depends(get_session)]):
    clients = db.exec(select(ClientModel)).all()
    return [{"id": client.id, "name": client.name} for client in clients]


@router.post("/clients", response_class=JSONResponse)
async def create_client(
    client_name: Annotated[str, Form()],
    db: Annotated[Session, Depends(get_session)],
):
    client = ClientModel(name=client_name)
    db.add(client)
    db.commit()
    db.refresh(client)
    return {"id": client.id, "name": client.name}


@router.get("/clients/{client_id}/sessions", response_class=JSONResponse)
async def get_client_sessions(
    client_id: int,
    db: Annotated[Session, Depends(get_session)],
):
    sessions = db.exec(
        select(TherapySessionModel).where(TherapySessionModel.client_id == client_id),
    ).all()
    return [
        {
            "id": session.id,
            "timestamp": session.timestamp.isoformat(),
            "data": session.session_data,
        }
        for session in sessions
    ]
