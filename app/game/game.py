from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from app.__init__ import bot
from app.handlers.game_handlers import choise
import logging
import random

router = Router()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Словарь для хранения состояния игры
game_states = {}

async def game(users_in_game):

    user_one, user_two = users_in_game
    first_player, second_player = random.sample([user_one, user_two], 2)

    await bot.send_message(first_player[0], "❕Ход достается вам, выберите действие", reply_markup=choise)
    await bot.send_message(second_player[0], "❗️Ход достается противнику, ожидайте его действие.")

    # Теперь передаем корректный объект callback


@router.callback_query(F.data == 'Стрелять в себя')
async def shoot_self(callback: CallbackQuery, users_in_game):
    first_player, second_player = users_in_game

    # Определяем, кто стреляет, на основе ID пользователя
    shooter = first_player if callback.from_user.id == first_player[0] else second_player

    if shooter[0] == first_player[0]:
        await process_shooting(first_player, second_player)
    else:
        await process_shooting(second_player, first_player)

async def process_shooting(shooter, opponent):
    if random.randrange(1, 7) == 1:
        await bot.send_message(shooter[0], "💀Приставив ствол револьвера к своему виску и спустив курок, всë кругом резко почернело, вы мертвы.")
        await bot.send_message(opponent[0], "😬Вы видите, как противник спустил курок, держа револьвер у своего виска, и остаётся с дыркой в голове. Противник мёртв.")
        # Здесь можно добавить логику для завершения игры
    else:
        await bot.send_message(shooter[0], "😀Приставив ствол револьвера к своему виску и спустив курок, вы остались живы, ход остаётся у вас.", reply_markup=choise)
        await bot.send_message(opponent[0], "Вы видите, как противник спустил курок, держа револьвер у своего виска, противник остаётся живым, ход по прежнему у него.")