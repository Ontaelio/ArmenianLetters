from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Ссылка на статические файлы (CSS, JS, изображения)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключение файлов обработки API-запросов
from app.api import endpoints

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)