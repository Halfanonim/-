# api/dishes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.dishes import Dish

router = APIRouter()

@router.post("/dishes/")
async def create_menu(name: str, db: Session = Depends(SessionLocal)):
    dishes = Dish(name=name)
    db.add(dishes)
    db.commit()
    db.refresh(dishes)
    return dishes
