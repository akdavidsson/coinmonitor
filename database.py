import sqlite3
import datetime
from coins_monitored import COINS;

class DataBase():

    def __init__(self):
        self.conn = sqlite3.connect('local.db')
        self.create_table()
        self.populate_coin()

    def create_table(self):
        c = self.conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS coin (
                    name TEXT PRIMARY KEY,
                    created_at TEXT
                );''')

        c.execute('''CREATE TABLE IF NOT EXISTS coin_entries (
                name TEXT,
                value TEXT,
                created_at TEXT,
                FOREIGN KEY(name) REFERENCES coin(name)
            );''')

        self.conn.commit()
    
    def populate_coin(self):
        c = self.conn.cursor()

        c.execute("SELECT * from coin")
        if c.fetchone() is None:
            sql = "INSERT INTO coin (name, created_at) VALUES(?, ?)"
            for coin in COINS:
                c.execute(sql, (coin, (datetime.datetime.utcnow())))
        self.conn.commit()
    
    def persist_coin_entries(self, entries):
        c = self.conn.cursor()
        for entry in entries:
            entry.append(datetime.datetime.utcnow())
        sql = "INSERT INTO coin_entries VALUES(?, ?, ?)"
        c.executemany(sql, entries)
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()


if __name__ == "__main__": 
    db = DataBase()

