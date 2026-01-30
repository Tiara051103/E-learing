import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "akademik.db")

def get_connection():
    return sqlite3.connect(
        DB_PATH,
        timeout=10,
        check_same_thread=False
    )
