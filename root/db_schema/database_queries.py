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
VALUES ("Kalin Petrov", "2a13d86ffeba54a4c5f04f1112e0068818e32812a27cb6bbd7934f60c64fd650"),
("Ivan Ivanov", "8b2b146e58694903084e0a510e7ce302fee3cef6b9defbd87100777d76d278b7"),
("Georgi Budov", "281807ba64ef115395e9980211f069690b5422a78459ef31f15142a41b826ade"),
("Petar Dimitrov", "868a7dc455e3bcab3a8e66eb16e04c16fef756d043b183b2a07eda0dda6185c5");
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
