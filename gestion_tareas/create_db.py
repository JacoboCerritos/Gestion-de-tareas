import sqlite3

connection = sqlite3.connect('tasks.db')

with connection:
    connection.execute('''
        CREATE TABLE task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    ''')

connection.close()
