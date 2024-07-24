from aiogram import F, Router
from aiogram.types import Message
import logging
import random

from app.database.engine import get_user, ready_tryed, ready_falsed, get_users_ready
from app.game.game import game
router = Router()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_enemy(message: Message) -> tuple:
    """
    Get the enemy player for the current game session.

    Args:
        message (Message): The message containing the user's request.

    Returns:
        tuple: A tuple containing the enemy player's ID and their profile information.
    """
    # Update the ready status of the player
    ready_tryed(message.from_user.id)  # Update the ready status of the player

    # Get the list of ready users
    ready_users = tuple(get_users_ready())  # Get the list of ready users

    # Print the list of ready users for debugging purposes
    print("Готовые пользователи:", ready_users)

    # If there are more than one ready users, select two randomly
    if len(ready_users) > 1:
        users_in_game = random.sample(ready_users, k=2)  # Select two randomly
        # Find the enemy player by excluding the current player
        for user in users_in_game:
            print(user)
            if user[0] != message.from_user.id:
                user_one = user
                print("юзер 1", user_one)
            elif user[0] == message.from_user.id:
                user_two = user
                print("юзер 2", user_two)

        return  user_one, user_two

        


        # # Send the enemy player's profile information to the user
        # message.answer(profile_str)  # Send the profile information to the user

    # Return the enemy player's ID and profile information
