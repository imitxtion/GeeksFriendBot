import sqlite3

from datetime import datetime
from utils import text

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

    def get_formated_tasks(self, user_id):
        with self.connection:
            tasks = self.cursor.execute('select * from tasks where user_id = ?', (user_id,)).fetchall()
            if not tasks:
                return text.task_list_empty
            else:
                counter = 1
                formated_result = f'{text.browse_todos}'
            
                for task in tasks:
                    formated_task = f'\n<b>Task {counter}</b>\n<b>Description:</b> {task[2]}\n<b>Time:</b> {task[3]}\n'
                    counter += 1
                    formated_result += formated_task

                return formated_result