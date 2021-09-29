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
                self.main_menu()
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
            self.main_menu()

    
    def add_workout(self):
        choice = input('did you workout today? ')
        choice.lower()
        while choice != 'n':
            if choice == 'y':
                exercise = input('exercise: ')
                sets = input('sets: ')
                reps = input('reps: ')
                weight = input('weight: ')
                self.cursor.execute("SELECT exercise_name FROM exercises WHERE exercise_name = (?)", exercise)
                if self.cursor.fetchall():
                        values = (self.username, exercise, sets, reps, weight)
                        self.cursor.execute('''
                        INSERT INTO user_workouts(date, user_id, exercise_id, sets, reps, weight) VALUES 
                        (
                            (SELECT DATETIME())
                        ,   (SELECT user_id FROM users WHERE user_name = ?)
                        ,   (SELECT exercise_id FROM exercises WHERE exercise_name = ?)
                        ,   ?
                        ,   ?
                        ,   ?
                        )''', values)
                        self.connection.commit()
                        choice = input('another exercise? ')
                        choice.lower()
                else:
                    print('the exercise does not exist')
                    self.add_exercise()    
        if choice == 'n':
            print('you are lazy')


    def add_exercise(self):
        choice = input('add an exercise? ')
        choice.lower()
        if choice == 'y':
            exercise = input('what is the name of the exercise? ')
            descri = input('enter a description: ')
            values = exercise, descri
            self.cursor.execute('INSERT INTO exercises (exercise_name, description) VALUES ?, ?', values)
            self.connection.commit()
        else:
            self.main_menu()


    def view_workout(self):
        # view exercise_name, sets, reps, weight where the username = 
        date = input('enter the date of the workout you would like to see' )
        self.cursor.execute('''SELECT exercise_name, sets, reps, weight 
            FROM user_workouts 
                JOIN exercises
                    ON user_workouts.exercise_id = exercises.exercise_id
                JOIN users
                    ON users.user_id = exercises.exercise_id
            WHERE users.user_id =  ?
            ''', self.username)
        print(self.cursor.fetchall())

    def main_menu(self):
        # option of viewing, adding workout or exercise
        choice = input('what would you like to do?: view workout(v), add workout(w), add exercise(e), or quit(q)')
        while choice != 'q':
            if choice == 'v':
                self.view_workout()
            elif choice == 'w':
                self.add_workout()
            elif choice == 'e':
                self.add_exercise()
            elif choice == 'q':
                break
            else:
                print('must choose v, w, e, or q')



