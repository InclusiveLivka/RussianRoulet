import sqlite3
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "data.db")


create_table_query = """CREATE TABLE IF NOT EXISTS users_info(
    user_id        INTEGER,
    user_name      TEXT,
    amount_rate    INTEGER,
    balance_key    INTEGER,
    amount_win     INTEGER,
    prefix         TEXT
)
"""


def intialize_db():
    try:
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        cursor.execute(create_table_query)
        db.commit()

    except sqlite3.Error as error:
        logger.error(f"Error initializing database: {error}")

    except Exception as error:
        logger.error(f"Unexpected error initializing database: {error}")


def add_user(user_id, username, amount_rate, balance_key, amount_win, prefix):
    try:
        intialize_db()
        exam_user(user_id)
        
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        sql = """INSERT INTO users_info
        (user_id, user_name, amount_rate, balance_key, amount_win, prefix)
        VALUES
        (?, ?, ?, ?, ?, ?)
        """

    except sqlite3.Error as error:
        logger.error(f"Error adding user: {error}")
        
    
    except Exception as error:
        logger.error(f"Unexpected error adding user: {error}")
        

    try:
        cursor.execute(sql, (user_id, username, amount_rate,
                       balance_key, amount_win, prefix))
        db.commit()
        
    
    except sqlite3.Error as error:
        logger.error(f"Error adding user: {error}")
        
    
    except Exception as error:
        logger.error(f"Unexpected error adding user: {error}")
        


def exam_user (user_id):
    try:
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users_info WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        if result:
            add_user(*result)
        else:
            return False




    except sqlite3.Error as error:
        logger.error(f"Error adding user: {error}")
        return False