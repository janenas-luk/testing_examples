import sqlite3
from sqlite3 import Error

class loggerCon:

    __connection = None

    def open_log(self, db):
        if not db:
            db = "/home/janenaslu/logger.db"
        conn = None
        try:
            conn = sqlite3.connect(db)
            self.__connection = conn
            self.__create_table()
        except Error as e:
            print(e)

    def __create_table(self):
        tableQuery = """ CREATE TABLE IF NOT EXISTS logger (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    level text NOT NULL,
                    message text NOT NULL,
                    time text NOT NULL
                    ); """
        try:
            cursor = self.__connection.cursor()
            cursor.execute(tableQuery)
        except Error as e:
            print(e)

    def close_log(self):
        if self.__connection:
            self.__connection.close()
        
    def write_to_log(self, level, message, timestamp):
        query = '''INSERT INTO logger (level, message, time) VALUES(?,?,?)'''
        data = (level, message, timestamp)
        cursor = self.__connection.cursor()
        cursor.execute(query, data)
        self.__connection.commit()
        