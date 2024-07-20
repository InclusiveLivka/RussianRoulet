import sqlite3


with sqlite3.connect("database.db") as db:
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
    (user_id INTEGER, username TEXT, amount_rate INTEGER, balance_key INTEGER, amount_win INTEGER, prefix TEXT)""")
