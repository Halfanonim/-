from fastapi import FastAPI
from api.menu import router as menu_router
from api.submenu import router as submenu_router
from api.dishes import router as dish_router
from database.database import SessionLocal, engine

app = FastAPI()

# Инициализация базы данных (если нужно)
# MenuBase.metadata.create_all(bind=engine)
# SubmenuBase.metadata.create_all(bind=engine)
# DishBase.metadata.create_all(bind=engine)

# Внедрение зависимости для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Подключение маршрутов
app.include_router(menu_router, prefix="/menu", tags=["menu"])
app.include_router(submenu_router, prefix="/submenu", tags=["submenu"])
app.include_router(dish_router, prefix="/dish", tags=["dish"])

# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)




    



