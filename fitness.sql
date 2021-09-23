DROP TABLE IF EXISTS [Users];
DROP TABLE IF EXISTS [Exercises];
DROP TABLE IF EXISTS [User_workouts];


CREATE TABLE [users]
(
    [user_id] INTEGER PRIMARY KEY NOT NULL,
    [password] TEXT NOT NULL,
    [first_name] TEXT NOT NULL,
    [last_name] TEXT
);

CREATE TABLE [exercises]
(
    [exercise_id] INTEGER PRIMARY KEY NOT NULL,
    [exercise_name] TEXT NOT NULL,
    [description] TEXT NOT NULL
);

CREATE TABLE [user_workouts]
(
    [workout_id] INTEGER PRIMARY KEY NOT NULL,
    [date] DATETIME NOT NULL,
    [user_id] INTEGER NOT NULL,
    [exercise_id] INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (exercise_id) REFERENCES  exercises(exercise_id)
);

INSERT INTO [exercises] (exercise_name, description) VALUES
('bench press', 'place the bar over your chest, keep elbows at a 45 degree angle to the body')
,
('squat', 'place the bar on the shelf your shoulder create, keep body tight and squat down')
,
('deadlift', 'starting with the bar on the floor, place feet shoulder width apart, grab the bar, and lift up')
;