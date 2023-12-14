from backend.b_app import app

if __name__ == "__main__":
    import uvicorn
    from database.db import Database

    # Создаем таблицу при запуске приложения
    Database().create_table()

    # Запуск сервера с использованием библиотеки uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
