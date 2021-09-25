from io import DEFAULT_BUFFER_SIZE
import sqlite3
from sqlite3.dbapi2 import Cursor, connect

class user():
    def __init__(self):
        self.connection = sqlite3.connect('fitness')
        self.cursor = self.connection.cursor()
        self.username = None
        self.password = None

    def get_credentials(self, values):
        """ This function gets the username and password from the fitness database and returns them """
        self.cursor.execute('SELECT user_name FROM users WHERE user_name = (?)', values)
        db_user = self.cursor.fetchall()
        self.cursor.execute('SELECT password FROM users WHERE user_name = (?)', values)
        db_pass = self.cursor.fetchall()
        return db_user[0][0], db_pass[0][0]
    
    def login(self):
        """ When run, the user will login in with their password and user name"""
    
        choice = input('login or create user ')
        choice.lower()
        if choice == 'login':
            self.username = input('username: ')
            self.password = input('password: ')

            values = (self.username,)
            db_user, db_pass = self.get_credentials(values)
            
            if db_user == self.username and db_pass == self.password:
                print(f'welcome back {self.username}')
                self.add_workout()
            else:
                print('incorrect credentials')

        elif choice == 'create':
            username = input('username: ')
            password = input('password: ')
            first_name = input('first name: ')
            last_name = input('last name: ')
            
            values1 = (username, password, first_name, last_name)
            self.cursor.execute('INSERT INTO users(user_name, password, first_name, last_name) VALUES (?, ?, ?, ?)', values1)
            self.connection.commit()
            # self.connection.close()
            self.add_workout()

    
    def add_workout(self):
        choice = input('did you workout today? ')
        choice.lower()
        while choice != 'n':
            if choice == 'y':
                exercise = input('exercise: ')
                sets = input('sets: ')
                reps = input('reps: ')
                weight = input('weight: ')
                values = (self.username, exercise, sets, reps, weight)
                self.cursor.execute('''
                INSERT INTO user_workouts(date, user_id, exercise_id, sets, reps, weight) VALUES 
                (
                    (SELECT DATETIME())
                ,   (SELECT user_id FROM users WHERE user_name = 'densmoreb')
                ,   (SELECT exercise_id FROM exercises WHERE exercise_name = 'bench press')
                ,   ?
                ,   ?
                ,   ?
                );''', values)
                choice = input('another exercise? ')
                choice.lower()
        if choice == 'n':
            print('you are lazy')
