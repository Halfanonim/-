# api/submenu.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.submenu import  Submenu

router = APIRouter()

@router.post("/submenus/")
async def create_submenu(name: str, db: Session = Depends(SessionLocal)):
    submenu = Submenu(name=name)
    db.add(submenu)
    db.commit()
    db.refresh(submenu)
    return submenu
