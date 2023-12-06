import sqlite3 as sq
from dbutils.pooled_db import PooledDB


class Database:
    def __init__(self):
        self.pool = PooledDB(sq, maxconnections=8, database='products.db')

    def get_connection(self):
        return self.pool.connection()


def create_db():
    with sq.connect('products.db') as con:
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        img_url BLOB,
        product_type TEXT,
        price TEXT,
        description TEXT,
        product_link TEXT
        )''')