# app/routes/monitor.py
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "OK"}
