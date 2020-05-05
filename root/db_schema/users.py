CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY NOT NULL,
        username varchar(50) UNIQUE NOT NULL,
        password varchar(50) NOT NULL
    );
'''
