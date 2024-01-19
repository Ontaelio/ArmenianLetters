from fastapi import FastAPI, APIRouter, HTTPException
from data.letters import *
from convert import ru_to_arm

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
    valid_options = SETS.keys()
    invalid_options = set(lesson_options) - set(valid_options)
    if invalid_options:
        raise HTTPException(status_code=422, detail=f"Invalid 'options' values: {', '.join(invalid_options)}")

    if text is None:
        raise HTTPException(status_code=422, detail="Missing 'text' field")

    sets = {}
    for _ in lesson_options:
        sets |= SETS[_]

    processed_text = ru_to_arm(text, sets)
    return {"result": processed_text}

