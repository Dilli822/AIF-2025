# app/main.py
from fastapi import FastAPI
from app.config import settings
from app.routes import monitor

app = FastAPI(title=settings.app_name)

app.include_router(monitor.router)
