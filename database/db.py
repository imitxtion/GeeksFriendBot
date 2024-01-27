import sqlite3

class Database:
    def __init__(self, db_file) -> None:
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('select * from users where user_id = (?)', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, user_name):
        with self.connection:
            return self.cursor.execute('insert into users (user_id, user_name) values (?,?)', (user_id, user_name,))
