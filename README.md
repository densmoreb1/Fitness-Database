# Overview

This is a low-level fitness app. This was a project to help me learn about using python with SQLite.

The program allows the user to tracks the workouts they did. They are able to login, view a workout, and add a workout.

[Fitness App Demo Video](https://youtu.be/ACZWa5jRrYU)

# Relational Database

I went with a simple database I designed. It has three tables, users, user_workouts, and exercises. The user_workouts tables uses forgien keys to relate with the user table and the exercise table.

Everything is local in the code. Once someone downloads the app, the database is local to them and cannot be edited by someone who does not use the same computer

# Development Environment

* python3
* SQLite3

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [SQLite Tutorial](https://www.sqlitetutorial.net)
* [SQLite and Python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

* More error checking
* Security for passwords
* Move to a cloud application