from io import DEFAULT_BUFFER_SIZE
import sqlite3
from sqlite3.dbapi2 import Cursor, connect

connection = sqlite3.connect('fitness')
cursor = connection.cursor()

class user():
    def __init__(self, username, password):
        self.username = username
        self.password = password


def get_credentials(values):
    """ This function gets the username and password from the fitness database and returns them """
    cursor.execute('SELECT user_name FROM users WHERE user_name = (?)', values)
    db_user = cursor.fetchall()
    cursor.execute('SELECT password FROM users WHERE user_name = (?)', values)
    db_pass = cursor.fetchall()
    return db_user[0][0], db_pass[0][0]


# prompt for login
def login():
    """ When run, the user will login in with their password and user name"""
    
    choice = input('login or create user ')
    choice.lower()
    if choice == 'login':
        username = input('username: ')
        password = input('password: ')

        values = (username,)
        db_user, db_pass = get_credentials(values)
        
        if db_user == username and db_pass == password:
            print(f'welcome back {username}')
            user(db_user, db_pass)
            add_workout()
        else:
            print('incorrect credentials')

    elif choice == 'create':
        username = input('username: ')
        password = input('password: ')
        first_name = input('first name: ')
        last_name = input('last name: ')
        
        values1 = (username, password, first_name, last_name)
        cursor.execute('INSERT INTO users(user_name, password, first_name, last_name) VALUES (?, ?, ?, ?)', values1)
        connection.commit()
        connection.close()
        add_workout()

def add_workout():
    choice = input('did you workout today? ')
    choice.lower()
    while choice != 'n':
        if choice == 'y':
            exercise = input('exercise: ')
            sets = input('sets: ')
            reps = input('reps: ')
            weight = input('weight: ')
            values = None
            cursor.execute('''
            INSERT INTO user_workouts(date, user_id, exercise_id, sets, reps, weight) VALUES 
            (
                SELECT DATETIME(),
                SELECT user_id FROM users WHERE username = (?),
                SELECT exercise_id FROM exercises WHERE exercise_name = (?),
                ?,
                ?,
                ?
            )''')
            choice = input('another exercise? ')
            choice.lower()
    if choice == 'n':
        print('you are lazy')