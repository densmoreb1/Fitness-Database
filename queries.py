import sqlite3
from sqlite3.dbapi2 import Cursor, connect
import time

connection = sqlite3.connect('fitness')
cursor = connection.cursor()

# Show all tables
def show_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    for table in range(len(tables)):
        print(f'{tables[table][0]}')
        time.sleep(1)




