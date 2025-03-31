from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.dependencies import get_session
from app.models.db_models import ClientModel

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Annotated[Session, Depends(get_session)]):
    clients = db.exec(select(ClientModel)).all()
    return templates.TemplateResponse(
        "page_content.html",
        {
            "request": request,
            "clients": clients,
        },
    )
