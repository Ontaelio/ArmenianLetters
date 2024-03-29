import json
import io
from typing import List

from fastapi import FastAPI, APIRouter, HTTPException, UploadFile, Form, File
from fastapi.responses import StreamingResponse

from data.sets import SETS, SetResponse, BookResponse
from utils.convert import ru_to_arm
from utils.epub_engine import get_ebook_from_memory, convert_epub, put_ebook_in_memory, epub2txt
from utils.get_sets import get_set_by_id, get_sets_for_frontend, get_sets_list, get_sets_full

app = FastAPI()
router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.get("/sets")
async def read_sets():
    return get_sets_list()


@router.get("/sets_full", response_model=List[BookResponse])
async def read_sets_full():
    return get_sets_full()


@router.get("/sets_front")
async def read_sets_front():
    return get_sets_for_frontend()


@router.get("/set/{set_id}", response_model=List[SetResponse])
async def read_one_set(set_id: int):
    return get_set_by_id(set_id)


@router.post("/process_text")
async def process_text(data: dict):
    if "text" not in data or "options" not in data:
        raise HTTPException(status_code=422, detail="Missing 'text' or 'options' in data")

    text = data.get("text")
    lesson_options = data.get("options")

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
    contents = await file.read()
    # logging.error(str(options))

    file_mime_type = file.content_type
    options_list = json.loads(options)
    valid_options = SETS.keys()
    invalid_options = set(options_list) - set(valid_options)
    if invalid_options:
        raise HTTPException(status_code=422, detail=f"Invalid 'options' values: {', '.join(invalid_options)}")

    sets = {}
    for _ in options_list:
        sets |= SETS[_]

    if file_mime_type.startswith('text'):
        processed_contents = ru_to_arm(contents.decode('utf-8'), sets)
        processed_file = io.BytesIO(processed_contents.encode('utf-8'))
        return StreamingResponse(processed_file, media_type="text/plain",
                                 headers={"Content-Disposition": "attachment; filename=processed_file.txt"})

    elif file_mime_type == "application/epub+zip":
        book = await get_ebook_from_memory(contents)
        processed_book = await put_ebook_in_memory(convert_epub(book, sets))
        processed_file = io.BytesIO(processed_book)
        return StreamingResponse(processed_file, media_type="text/plain",
                                 headers={"Content-Disposition": "attachment; filename=processed_book.epub"})

    else:
        return {'error': 'unknown file type'}


@router.post("/get_text_from_epub")
async def process_file(file: UploadFile = File(...)):
    contents = await file.read()
    file_mime_type = file.content_type
    if file_mime_type != "application/epub+zip":
        return {'error': 'unknown file type'}

    book = await get_ebook_from_memory(contents)
    book_text = epub2txt(book)
    return {'result': book_text}



