import sqlite3

def create_db(sql_file, database_name):
    sql_script = open(sql_file)
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    script_file = sql_script.read()

    cursor.executescript(script_file)

    connection.commit()
    connection.close()