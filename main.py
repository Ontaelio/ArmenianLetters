from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import starlette.status as status

from app.api.endpoints import router as api_router

app = FastAPI(
    title="Letters converter Ru -> Arm",
    description="A tool to convert certain letters in a Russian text or epub into Armenian ones. "
                "For great justice!"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы от любого источника (замените на свой список)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP-методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, prefix="/api", tags=["api"])

app.mount("/armletters", StaticFiles(directory="app/frontend", html=True), name="frontend")


@app.get("/")
def index():
    return RedirectResponse(url="/armletters", status_code=status.HTTP_302_FOUND)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
