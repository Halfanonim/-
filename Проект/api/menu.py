# api/menu.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal

router = APIRouter()


@router.get("/menu/")
async def read_menu(db: Session = Depends(SessionLocal)):
    # Ваш код для обработки запроса
    pass
