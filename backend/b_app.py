from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from parser import get_info_product
from database.db import Database
from fastapi.templating import Jinja2Templates

app = FastAPI()
db = Database() # Создаём экземпляр класса Database
templates = Jinja2Templates(directory="frontend")  # Создаем объект для работы с шаблонами


@app.get("/")
async def read_root():
    db.clear_data()  # Вызываем метод clear_data, для удаления данных из базы данных
    get_info_product()  #  Вызываем метод get_ingo_product для парсинга информации о товарах

    #  При завершении парсинг выводим сообщение в виде JSON строки
    return JSONResponse(content={"message": "Парсинг данных успешно завершился, все данные добавлены в базу данных."})



