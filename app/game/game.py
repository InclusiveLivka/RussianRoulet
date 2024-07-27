from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from app.__init__ import bot
import app.keyboard.reply as kb
import logging
import random

router = Router()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Словарь для хранения состояния игры
game_states = {}

# Создаем клавиатуру для действий
def create_action_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Стрелять в себя", callback_data="shoot_self")],
        [InlineKeyboardButton(text="Стрелять во врага", callback_data="shoot_enemy")],
        [InlineKeyboardButton(text="Крутить обойму", callback_data="spin_revolver")]
    ])

# Создаем клавиатуру для основного меню
def create_main_menu_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать новую игру", callback_data="start_new_game")]
    ])

async def start_game(users_in_game, chamber_count=6):
    game_id = f"{users_in_game[0][0]}_{users_in_game[1][0]}"
    game_states[game_id] = {
        "users": users_in_game,
        "shooter_count": {user[0]: 0 for user in users_in_game},
        "revolver_position": random.randint(1, chamber_count),  # Инициализация позиции пули
        "max_turns": 5  # Максимальное количество ходов
    }

    first_player, second_player = random.sample(users_in_game, 2)

    await bot.send_message(first_player[0], "❕Ход достается вам, выберите действие.", reply_markup=create_action_keyboard())
    await bot.send_message(second_player[0], "❗️Ход достается противнику, ожидайте его действие.")

    return game_id

@router.callback_query(F.data.in_(["shoot_self", "shoot_enemy", "spin_revolver"]))
async def handle_action(callback: CallbackQuery):
    action_type = callback.data.split('_')[-1]  # Получаем тип действия
    await perform_action(callback, action_type)

async def perform_action(callback: CallbackQuery, action_type: str):
    user_id = callback.from_user.id
    game_id = next((gid for gid, users in game_states.items() if user_id in [user[0] for user in users["users"]]), None)

    if game_id is None:
        await bot.send_message(user_id, "❌ Вы не участвуете в игре.")
        return

    users_in_game = game_states[game_id]["users"]
    shooter, opponent = (users_in_game[0], users_in_game[1]) if user_id == users_in_game[0][0] else (users_in_game[1], users_in_game[0])

    # Увеличиваем счетчик спусков
    game_states[game_id]["shooter_count"][shooter[0]] += 1

    # Проверяем, достигли ли мы максимального количества ходов
    if game_states[game_id]["shooter_count"][shooter[0]] > game_states[game_id]["max_turns"]:
        await declare_result(opponent, shooter, game_id, "lose")  # Противник выигрывает
        return

    await callback.message.edit_reply_markup(reply_markup=None)

    if action_type == "self":
        await process_self_shooting(shooter, opponent, game_id)
    elif action_type == "enemy":
        await process_enemy_shooting(shooter, opponent, game_id)
    elif action_type == "spin_revolver":
        game_states[game_id]["revolver_position"] = random.randint(1, 6)  # Изменение позиции пули
        await bot.send_message(shooter[0], "😐После прокручивания обоймы револьвера, позиция ячейки с патроном поменялась, ход передаётся противнику.")
        await bot.send_message(opponent[0], "🤫Противник поменял место ячейки с патроном в револьвере, ход достается вам.", reply_markup=create_action_keyboard())

async def process_self_shooting(shooter, opponent, game_id):
    if game_states[game_id]["revolver_position"] == 1:  # Проверка, попал ли shooter
        await declare_result(shooter, opponent, game_id, "lose")
    else:
        await bot.send_message(shooter[0], "😀Приставив ствол револьвера к своему виску и спустив курок, вы остались живы, ход остаётся у вас.", reply_markup=create_action_keyboard())
        await bot.send_message(opponent[0], "😮‍💨Вы видите как противник спустил курок револьвера держа револьвер у своего виска, противник остаётся живым, ход по прежнему у него.")

async def process_enemy_shooting(shooter, opponent, game_id):
    if game_states[game_id]["revolver_position"] == 1:  # Проверка, попал ли opponent
        await declare_result(opponent, shooter, game_id, "lose")
    else:
        await bot.send_message(opponent[0], "😅Вы видите как противник навёл ствол револьвера на вашу голову и спустил курок, но выстрела не произошло, ход достается вам.", reply_markup=create_action_keyboard())
        await bot.send_message(shooter[0], "😶Наведя ствол револьвера на противника и спустив курок, противник остаётся живым. Теперь ход принадлежит ему.")

async def declare_result(loser, winner, game_id, result_type):
    winner_shots = game_states[game_id]["shooter_count"][winner[0]]
    loser_shots = game_states[game_id]["shooter_count"][loser[0]]

    result_message = (
        f"🏅 {'Поражение' if result_type == 'lose' else 'Победа'} 🏅\n"
        f"Враг спустил курок: {winner_shots} раз.\n"
        f"Вы спустили курок: {loser_shots} раз.\n"
        f"{'Потеря: -250 РР' if result_type == 'lose' else 'Награда: +500 РР'}"
    )

    await bot.send_message(loser[0], result_message)
    await bot.send_message(winner[0], result_message)

    if result_type == "lose":
        await bot.send_message(loser[0], "💀 Приставив ствол револьвера к своему виску и спустив курок, всë кругом резко почернело, вы мертвы.")
        await bot.send_message(winner[0], "😬 Вы видите как противник спустил курок револьвера держа револьвер у своего виска, после чего остаётся с дыркой в голове. Противник мёртв.")
    else:
        await bot.send_message(loser[0], "🏆 Вы победили! Игра окончена.")
        await bot.send_message(winner[0], "💀 Противник навёл ствол револьвера на вашу голову и спустил курок, всë резко потемнело. Вы мертвы.")

    del game_states[game_id]  # Удаляем игру после завершения
    await bot.send_message(loser[0], "🔄 Игра окончена. Выберите действие:", reply_markup=kb.main)
    await bot.send_message(winner[0], "🔄 Игра окончена. Выберите действие:", reply_markup=kb.main)

# Обработчик для начала новой игры
