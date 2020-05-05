insert_into_movies = '''
INSERT INTO movies(name, rating)
VALUES ("The Hunger Games: Catching Fire", 7.9),
("Wreck-It Ralph", 7.8),
("Her", 8.3);
'''

insert_into_projections = '''
INSERT INTO projections(movie_id, type, date_p, time_p)
VALUES (1, "3D", "2020-04-01", "19:10"),
(1, "2D", "2020-04-01", "19:00"),
(1, "4DX", "2020-04-02", "21:00"),
(3, "2D", "2020-04-05", "20:20"),
(2, "3D", "2020-04-02", "22:00"),
(2, "2D", "2020-04-02", "19:30");
'''

insert_into_users = '''
INSERT INTO users(username, password)
VALUES ("Martin Angelov", "****"),
("Ivo Donchev", "****"),
("Radoslav Georgiev", "****"),
("Rositza Zlateva", "****");
'''

insert_into_reservations = '''
INSERT INTO reservations(user_id, projection_id, row, col)
VALUES (3, 1, 2, 1),
(3, 1, 3, 5),
(3, 1, 7, 8),
(2, 3, 1, 1),
(2, 3, 1, 2),
(5, 5, 2, 3),
(6, 5, 2, 4);
'''