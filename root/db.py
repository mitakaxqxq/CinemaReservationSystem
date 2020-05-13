import sqlite3

from root.settings import DB_NAME


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def create_connection(self):
        self.connection = sqlite3.connect(DB_NAME)

    def connect_cursor(self):
        self.cursor = self.connection.cursor()
