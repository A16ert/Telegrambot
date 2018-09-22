import sqlite3

DBName = 'Model/db/lessons_db.db'

class SQLighter:
    """class provide access for date base"""

    def __init__(self):
        self.connection = sqlite3.connect(DBName)
        self.cursor = self.connection.cursor()
        pass

    def get_cursor(self):
        with self.connection:
            return self.cursor

    def execute_select(self, sql):
        with self.connection:
            return self.cursor.execute(sql).fetchall()

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
        pass

    pass



