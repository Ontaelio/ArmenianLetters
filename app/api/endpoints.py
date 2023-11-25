from fastapi import FastAPI, Form, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()
router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.post("/process_text")
async def process_text(data: dict):

    if "text" not in data or "options" not in data:
        raise HTTPException(status_code=422, detail="Missing 'text' or 'lesson_option' in data")

    text = data.get("text")
    lesson_options = data.get("options")

    # Проверяем, что lesson_options содержит только допустимые значения
    valid_options = ["Урок 1", "Урок 2", "Урок 3"]  # Добавьте все допустимые значения
    invalid_options = set(lesson_options) - set(valid_options)
    if invalid_options:
        raise HTTPException(status_code=422, detail=f"Invalid 'options' values: {', '.join(invalid_options)}")

    if text is None:
        raise HTTPException(status_code=422, detail="Missing 'text' field")
    processed_text = text[::-1]
    return {"result": processed_text}

