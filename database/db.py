import sqlite3 as sq
from contextlib import contextmanager


class Database:
    # Инициализация объекта базы данных с указанием пути к файлу базы данных
    def __init__(self, db_path='products.db'):
        self.db_path = db_path

    def get_products(self):
        with self.get_connection() as con:
            cur = con.cursor()
            # Выполнение SQL-запроса для получения всех записей из таблицы "products"
            cur.execute("SELECT * FROM products")
            # Возвращение всех записей в виде списка кортежей
            return cur.fetchall()

    def create_table(self):
        with self.get_connection() as con:
            cur = con.cursor()
            # Выполнение SQL-запроса для создания таблицы "products", если она не существует
            cur.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT,
                img_url BLOB,
                product_type TEXT,
                price TEXT,
                description TEXT,
                product_link TEXT
            )''')

    @contextmanager
    def get_connection(self):
        # Создание соединения с базой данных и использование контекстного менеджера
        con = sq.connect(self.db_path)
        try:
            yield con
        finally:
            con.close()

    def clear_data(self):
        with self.get_connection() as con:
            # Выполнение SQL-запросов для удаления данных из таблицы "products" и сброса счетчика AUTOINCREMENT
            cur = con.cursor()
            cur.execute("DELETE FROM products")
            cur.execute("DELETE FROM sqlite_sequence WHERE name='products'")
            con.commit()

    def has_data(self):
        with self.get_connection() as con:
            cur = con.cursor()
            # Выполнение SQL-запроса для подсчета количества записей в таблице "products"
            cur.execute("SELECT COUNT(*) FROM products")
            # Возвращение True, если количество записей больше 0, иначе False
            return cur.fetchone()[0] > 0

