from fastapi import FastAPI
from fastapi.responses import JSONResponse
from parser import create_db, get_info_product

app = FastAPI()


@app.get("/")
async def read_root():
    create_db()
    get_info_product()
    return JSONResponse(content={"message": "Парсинг данных успешно завершился, все данные добавлены в базу данных."})
