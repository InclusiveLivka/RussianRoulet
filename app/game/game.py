from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from app.__init__ import bot
from app.handlers.game_handlers import choise
import logging
import random
import time

router = Router()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def game(users_in_game):
    user_one, user_two = users_in_game
    first_player, second_player = random.sample([user_one, user_two], 2)
    await bot.send_message(first_player[0], "❕Ход достается вам, выберите действие", reply_markup=choise)
    await bot.send_message(second_player[0], "❗️Ход достается противнику, ожидайте его действие. ")

    @router.callback_query(F.data == 'Стрелять в себя')
    async def shoot(callback: types.CallbackQuery):
        if callback.from_user.id == first_player[0]:
            if random.randrange(1, 7) == 1:
                await bot.send_message(first_player[0], "💀Приставив ствол револьвера к своему виску и спустив курок, всë кругом резко почернело, вы мертвы. ")
                await bot.send_message(second_player[0], "😬Вы видите как противник спустил курок револьвера держа револьвер у своего виска, после чего остаётся с дыркой в голове. Противник мёртв. ")
            else:
                await bot.send_message(first_player[0], "😀Приставив ствол револьвера к своему виску и спустив курок, вы остались живы, ход остаётся у вас.", reply_markup=choise)
                await bot.send_message(second_player[0], "Вы видите как противник спустил кунок револьвера держа револьвер у своего виска, противник остаётся живым, ход по прежнему у него. ")
        elif callback.from_user.id == second_player[0]:
            if random.randrange(1, 7) == 1:
                await bot.send_message(second_player[0], "💀Приставив ствол револьвера к своему виску и спустив курок, всë кругом резко почернело, вы мертвы. ")
                await bot.send_message(first_player[0], "😬Вы видите как противник спустил кунок револьвера держа револьвер у своего виска, после чего остаётся с дыркой в голове. Противник мёртв. ")
            else:
                await bot.send_message(second_player[0], "😀Приставив ствол револьвера к своему виску и спустив курок, вы остались живы, ход остаётся у вас.", reply_markup=choise)
                await bot

    
        


        