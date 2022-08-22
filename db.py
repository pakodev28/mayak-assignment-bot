import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("data.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS data_from_users_xls(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                url TEXT NOT NULL,
                xpath TEXT NOT NULL
                )"""
        )
