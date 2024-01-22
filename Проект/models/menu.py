# models/menu.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)

    submenus = relationship("Submenu", back_populates="menu")