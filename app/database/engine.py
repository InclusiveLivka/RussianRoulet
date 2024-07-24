
import sqlite3
import logging
import os
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "data.db")

create_table_query = """

CREATE TABLE IF NOT EXISTS users_info(

    user_id INTEGER PRIMARY KEY,

    user_name TEXT,

    amount_rate INTEGER,

    balance_key INTEGER,

    amount_win INTEGER,

    prefix TEXT,

    ready BOOLEAN

)"""


def intialize_db() -> None:
    """
    Initialize the SQLite database by creating the "users_info" table if it
    doesn't already exist.

    Raises:
        sqlite3.Error: If there is a problem with the database.
        Exception: If there is an unexpected error.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # Create the table if it doesn't already exist
        cursor.execute(create_table_query)
        db.commit()

    # If there is an error, log the error
    except sqlite3.Error as error:
        logger.error(f"Error initializing database: {error}")

    # If there is an unexpected error, log the error
    except Exception as error:
        logger.error(f"Unexpected error initializing database: {error}")

    # Close the database connection
    finally:
        db.close()


def add_user(user_id: int, username: str, amount_rate: int, balance_key: int, amount_win: int, prefix: str, ready: bool) -> None:
    """
    Add a new user to the database with the given information.

    Args:
        user_id (int): The user's ID.
        username (str): The user's name.
        amount_rate (int): The user's amount rate.
        balance_key (int): The user's balance key.
        amount_win (int): The user's amount of wins.
        prefix (str): The user's prefix.
        ready (bool): The user's ready status.

    Raises:
        sqlite3.Error: If there is a problem with the database.
        Exception: If there is an unexpected error.
    """
    try:
        # Initialize the database if it hasn't been initialized yet
        intialize_db()

        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # SQL query to insert user data into the database
        sql = """
        INSERT INTO users_info (user_id, user_name, amount_rate, balance_key, amount_win, prefix, ready)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        # Execute the SQL query with the user data
        cursor.execute(sql, (user_id, username, amount_rate,
                       balance_key, amount_win, prefix, ready))
        db.commit()

    except sqlite3.Error as error:
        # Log any errors that occur during user addition
        logger.error(f"Error adding user: {error}")

    except Exception as error:
        # Log any unexpected errors
        logger.error(f"Unexpected error adding user: {error}")

    finally:
        db.close()


def get_user(user_id: int):
    """
    Retrieve user data from the database by user_id.

    Args:
        user_id (int): The user's ID.

    Returns:
        Union[dict, bool]: A dictionary containing user data if the user exists,
        False otherwise.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # Retrieve user data from the database
        cursor.execute(
            "SELECT * FROM users_info WHERE user_id = ?", (user_id,))

        # Fetch the first row from the database and return it as a dictionary
        result = cursor.fetchone()

        return result

    except sqlite3.Error as error:
        # Log any errors that occur during user retrieval
        logger.error(f"Error retrieving user data: {error}")
        return False

    finally:
        # Close the database connection
        db.close()


def update_user(user_id: int, amount_rate: int, balance_key: int, amount_win: int) -> None:
    """
    Update user data in the database with the given values for amount_rate, balance_key, and amount_win.

    Args:
        user_id (int): The user's ID.
        amount_rate (int): The new value for amount_rate.
        balance_key (int): The new value for balance_key.
        amount_win (int): The new value for amount_win.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()

        # Update the user's data in the database
        cursor.execute(
            # SQL query to update user data
            "UPDATE users_info SET amount_rate = ?, balance_key = ?, amount_win = ? WHERE user_id = ?",
            # Values to be updated
            (amount_rate, balance_key, amount_win, user_id)
        )

        # Commit the changes to the database
        db.commit()

    except sqlite3.Error as error:
        # Log any errors that occur during user update
        logger.error(f"Error updating user data: {error}")
        raise error

    finally:
        # Close the database connection
        db.close()



def ready_tryed(user_id: int) -> None:
    """
    Set the 'ready' status to True for the user with the given user_id.

    Args:
        user_id (int): The ID of the user to update.
    """
    try:
        # Connect to the database
        db = sqlite3.connect(DB_PATH)

        cursor = db.cursor()

        # Update the 'ready' status for the user
        cursor.execute(
            "UPDATE users_info SET ready = ? WHERE user_id = ?", (True, user_id))

        db.commit()

    except sqlite3.Error as error:
        # Log any errors that occur during user update
        logger.error(f"Error tryed user: {error}")

    finally:
        # Close the database connection
        db.close()


def ready_falsed(user_id: int) -> None:

    try:

        # Connect to the database

        db = sqlite3.connect(DB_PATH)

        cursor = db.cursor()

        # Update the 'ready' status for the user

        cursor.execute(
            "UPDATE users_info SET ready = ? WHERE user_id = ?", (False, user_id))

        db.commit()

    except sqlite3.Error as error:

        logger.error(f"Error falsed user: {error}")

    finally:

        db.close()


def get_users_ready() -> list:

    try:

        # Connect to the database

        db = sqlite3.connect(DB_PATH)

        cursor = db.cursor()

        # Retrieve all user_ids where the 'ready' status is True

        cursor.execute(
            "SELECT user_id FROM users_info WHERE ready = ?", (True,))

        # Fetch all rows from the database and return them as a list

        result = cursor.fetchall()

        return result

    except sqlite3.Error as error:

        logger.error(f"Error retrieving users ready: {error}")

        return []

    finally:

        db.close()
