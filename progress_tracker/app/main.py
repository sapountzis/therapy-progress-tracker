from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.dependencies import create_db_and_tables
from app.routes import clients, index, progress, sessions


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    app.include_router(clients.router)
    app.include_router(index.router)
    app.include_router(progress.router)
    app.include_router(sessions.router)
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    yield


app = FastAPI(title="Therapy Progress Tracker API", lifespan=lifespan)
