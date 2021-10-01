from io import DEFAULT_BUFFER_SIZE
from os import close
import sqlite3
from sqlite3.dbapi2 import Cursor, connect

class user():
    def __init__(self):
        self.connection = sqlite3.connect('fitness')
        self.cursor = self.connection.cursor()
        self.username = None
        self.password = None

    def get_credentials(self):
        """ This function gets the username and password from the fitness database and returns them """
        values = (self.username,)
        self.cursor.execute('SELECT user_name FROM users WHERE user_name = (?)', values)
        db_user = self.cursor.fetchall()
        if db_user[0][0] == self.username:
            return True
        else:
            print('invalid credentials')
            
    
    def login(self):
        """ When run, the user will login in with their password and user name"""
        choice = None
        while choice != 'q':
            choice = input('welcome to fitness db \nlogin(l), create user(c), or quit(q) ')
            choice.lower()
            if choice == 'l':
                count = 0
                while count <= 3:
                    self.username = input('username: ')
                    self.password = input('password: ')
                    if self.get_credentials():
                        print(f'welcome back {self.username}')
                        self.main_menu()
                    elif count == 3:
                        username = input('username: ')
                        password = input('password: ')
                        first_name = input('first name: ')
                        last_name = input('last name: ')
                        
                        values1 = (username, password, first_name, last_name)
                        self.cursor.execute('INSERT INTO users(user_name, password, first_name, last_name) VALUES (?, ?, ?, ?)', values1)
                        self.connection.commit()
                        self.main_menu()
                    else:
                        print('try again\n')
                        count += 1

            elif choice == 'c':
                print('create new user')
                username = input('username: ')
                password = input('password: ')
                first_name = input('first name: ')
                last_name = input('last name: ')
                
                values1 = (username, password, first_name, last_name)
                self.cursor.execute('INSERT INTO users(user_name, password, first_name, last_name) VALUES (?, ?, ?, ?)', values1)
                self.connection.commit()
                self.main_menu()
            elif choice == 'q':
                choice = 'q'
            else:
                print('incorrect response\n')

    def add_workout(self):
        choice = None
        while choice != 'n':
            choice = input('did you workout today?(y or n) ')
            choice.lower()
            if choice == 'y':
                exercise = input('exercise: ')
                sets = input('sets: ')
                reps = input('reps: ')
                weight = input('weight: ')
                value_exer = (exercise, )
                self.cursor.execute("SELECT exercise_name FROM exercises WHERE exercise_name = ?", value_exer)
                if self.cursor.fetchall():
                        values = (self.username, exercise, sets, reps, weight)
                        self.cursor.execute('''
                        INSERT INTO user_workouts(date, user_id, exercise_id, sets, reps, weight) VALUES 
                            (
                                (SELECT DATE()), 
                                (SELECT user_id FROM users WHERE user_name = ?), 
                                (SELECT exercise_id FROM exercises WHERE exercise_name = ?),
                                ?,
                                ?,
                                ?
                            )''', values)
                        self.connection.commit()
                        choice = input('another exercise? ')
                        choice.lower()
                else:
                    print('the exercise does not exist')
                    self.add_exercise()    
        if choice == 'n':
            print('you are lazy')
            # choice = 'n'

    def add_exercise(self):
        choice = input('add an exercise? ')
        choice.lower()
        if choice == 'y':
            exercise = input('what is the name of the exercise? ')
            descri = input('enter a description: ')
            values = exercise, descri
            self.cursor.execute('INSERT INTO exercises (exercise_name, description) VALUES (?, ?)', values)
            print('the exercise was added to the database ')
            self.connection.commit()
        else:
            ('returning to main menu')

    def view_workout(self):
        # view exercise_name, sets, reps, weight where the username = 
        date = input('enter the date of the workout you would like to see (YYYY-MM-DD) ' )
        values = (self.username, date)
        self.cursor.execute('''SELECT exercise_name, sets, reps, weight 
            FROM user_workouts 
                JOIN exercises
                    ON user_workouts.exercise_id = exercises.exercise_id
                JOIN users
                    ON users.user_id = exercises.exercise_id
            WHERE users.user_id =  ? and date = ?
            ''', values)
        results = self.cursor.fetchall()
        print(results)

    def main_menu(self):
        # option of viewing, adding workout or exercise
        choice = None
        while choice != 'q':
            choice = input('what would you like to do?: view workout(v), add workout(w), add exercise(e), or quit(q) ')
            if choice == 'v':
                self.view_workout()
            elif choice == 'w':
                self.add_workout()
            elif choice == 'e':
                self.add_exercise()
            elif choice == 'q':
                quit()
            else:
                print('must choose v, w, e, or q')

