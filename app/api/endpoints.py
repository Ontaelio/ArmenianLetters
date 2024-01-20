import json
import logging

from fastapi import FastAPI, APIRouter, HTTPException, UploadFile, Form, File
from fastapi.responses import StreamingResponse
import io
from data.letters import *
from app.utils.convert import ru_to_arm

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


@router.post("/process_file")
async def process_file(file: UploadFile = File(...), options: str = Form(...)):
    # Считайте содержимое файла
    contents = await file.read()
    logging.error(str(options))

    options_list = json.loads(options)
    valid_options = SETS.keys()
    invalid_options = set(options_list) - set(valid_options)
    if invalid_options:
        raise HTTPException(status_code=422, detail=f"Invalid 'options' values: {', '.join(invalid_options)}")

    sets = {}
    for _ in options_list:
        sets |= SETS[_]

    # Выполните какие-то операции с содержимым файла
    # В данном случае, просто обратим его содержимое
    processed_contents = ru_to_arm(contents.decode('utf-8'), sets)

    # Создайте новый файл в памяти
    processed_file = io.BytesIO(processed_contents.encode('utf-8'))

    # Верните новый файл в теле ответа
    return StreamingResponse(processed_file, media_type="text/plain",
                             headers={"Content-Disposition": "attachment; filename=processed_file.txt"})

