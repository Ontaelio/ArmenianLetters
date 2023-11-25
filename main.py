from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы от любого источника (замените на свой список)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP-методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# Ссылка на статические файлы (CSS, JS, изображения)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Статические файлы (фронтенд)
app.mount("/front", StaticFiles(directory="app/frontend", html=True), name="frontend")


# Подключение файлов обработки API-запросов
from app.api.endpoints import router as api_router

app.include_router(api_router, prefix="/api", tags=["api"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)