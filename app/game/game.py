from aiogram import F, Router
from aiogram.types import Message
from app.__init__ import bot
from app.handlers.game_handlers import choise
import logging
import random
import time

router = Router()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def game (users_in_game):
    user_one, user_two = users_in_game
    if random.randrange(1,3) == 1:
        await bot.send_message(user_one[0], "❕Ход достается вам, выберите действие", reply_markup=choise)
        await bot.send_message(user_two[0], "❗️Ход достается противнику, ожидайте его действие. ")
    else:
        await bot.send_message(user_two[0], "❕Ход достается вам, выберите действие", reply_markup=choise)
        await bot.send_message(user_one[0], "❗️Ход достается противнику, ожидайте его действие. ")


    
        


        