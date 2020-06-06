# Cinema Reservation System

This is a project from HackBulgaria's "Programming with Python 101" course that combines three techniques: OOP, MVC and SQL

# Setup

Download the repository and run the program with ```python main.py```

# The database

Our database consists of the following tables:

### Movies

| id  | name                            | rating |
| --- | :------------------------------ | :----: |
| 1   | The Hunger Games: Catching Fire |  7.9   |
| 2   | Wreck-It Ralph                  |  7.8   |
| 3   | Her                             |  8.3   |

### Projections

| id  | movie_id | type |    date    | time  |
| --- | -------- | :--: | :--------: | :---: |
| 1   | 1        |  3D  | 2020-04-01 | 19:10 |
| 2   | 1        |  2D  | 2020-04-01 | 19:00 |
| 3   | 1        | 4DX  | 2020-04-02 | 21:00 |
| 4   | 3        |  2D  | 2020-04-05 | 20:20 |
| 5   | 2        |  3D  | 2020-04-02 | 22:00 |
| 6   | 2        |  2D  | 2020-04-02 | 19:30 |

### Users

| id  | username          |   password   |
| --- | ----------------- | :----------: |
| 1   | Martin Angelov    | **\*\*\*\*** |
| 2   | Ivo Donchev       | **\*\*\*\*** |
| 3   | Radoslav Georgiev | **\*\*\*\*** |
| 4   | Rositza Zlateva   | **\*\*\*\*** |


### Reservations

| id  | user_id | projection_id | row | col |
| --- | ------- | ------------- | :-: | :-: |
| 1   | 3       | 1             |  2  |  1  |
| 2   | 3       | 1             |  3  |  5  |
| 3   | 3       | 1             |  7  |  8  |
| 4   | 2       | 3             |  1  |  1  |
| 5   | 2       | 3             |  1  |  2  |
| 6   | 5       | 5             |  2  |  3  |
| 7   | 6       | 5             |  2  |  4  |


## The CLI (Command-Line Interface)

Our cinema reservation system is very simple. We use the console for user interactions. When started you will see list of commands. If you are having trouble with the commands use the command ```help``` to get an explanation.
