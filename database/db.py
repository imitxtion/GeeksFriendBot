import sqlite3

from datetime import datetime

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('select * from users where user_id = (?)', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, user_name, first_launch):
        with self.connection:
            self.cursor.execute('insert into users (user_id, user_name, first_launch) values (?,?,?)', 
                                (user_id, user_name, first_launch,))

    def add_task(self, user_id, task_description, task_datetime):
        with self.connection:
            self.cursor.execute('insert into tasks (user_id, description, datetime) values (?, ?, ?)',
                                (user_id, task_description, task_datetime,))
            
    def delete_old_tasks(self):
        with self.connection:
            self.cursor.execute('delete from tasks where datetime <= ?', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))