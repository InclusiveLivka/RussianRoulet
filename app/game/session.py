from aiogram import F, Router
from aiogram.types import Message
import logging
import random

from app.database.engine import get_user, ready_tryed, ready_falsed, get_users_ready
from app.game.game import game
router = Router()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_enemy(message: Message):
    ready_tryed(message.from_user.id)
    ready_users = get_users_ready()
    if len(ready_users) > 1:
        users_in_game = random.choices (ready_users(), k=2)
        enemy = users_in_game[1][0]
        return enemy



