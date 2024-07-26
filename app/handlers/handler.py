from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
import app.keyboard.reply as kb
import sqlite3
import time
import random
from app.handlers.game_handlers import choise
from time import monotonic

from app.__init__ import bot
from app.keyboard import inline
from app.database.engine import get_user, ready_falsed
from app.game.session import get_enemy
from app.game.game import shoot_self, game


router = Router()

@router.message(F.text == '🔫начать игру🔫')
async def start_game(message: Message):
    """
    Handles the "/start_game" command. 
    Sends a message to start the game and initiates the search for an opponent.

    Args:
        message (Message): The Telegram message object.
    """
    # Send a message to the user indicating that the search for an opponent has begun
    search = await message.answer("🔎 Начинается поиск оппонента.")

    # Initiate the search for an opponent
    enemy_players = get_enemy(message)  # Функция должна возвращать список из 2 игроков
    if enemy_players is None or len(enemy_players) < 2:
        await message.answer("❌ Не удалось найти оппонента. Попробуйте позже.")
        return

    user_one, user_two = enemy_players

    # Display the opponent's profile information
    hideBoard = types.ReplyKeyboardRemove()
    
    # Получаем профили игроков
    profile_one = get_user(user_one[0])
    profile_two = get_user(user_two[0])
    
    profile_one_str = (
        f"👤 Профиль: {profile_one[1]}\n"
        f"🏆 Кол-во РР: {profile_one[2]}\n"
        f"🏅 Победы: {profile_one[4]}\n"
        f"Префикс: {profile_one[5]}\n"
    )

    profile_two_str = (
        f"👤 Профиль: {profile_two[1]}\n"
        f"🏆 Кол-во РР: {profile_two[2]}\n"
        f"🏅 Победы: {profile_two[4]}\n"
        f"Префикс: {profile_two[5]}\n"
    )

    # Уведомляем игроков о завершении поиска
    await bot.send_message(user_one[0], "✅ Поиск оппонента завершен.", reply_markup=hideBoard)
    await bot.send_message(user_one[0], profile_two_str)

    await bot.send_message(user_two[0], "✅ Поиск оппонента завершен.", reply_markup=hideBoard)
    await bot.send_message(user_two[0], profile_one_str)

    # Запускаем игру с двумя игроками
    user_one, user_two = enemy_players
    await game(enemy_players)  # Убедитесь, что game принимает список игроков


@router.message(F.text == '🔫начать игру🔫')
async def start_game(message: Message,):
    """
    Handles the "/start_game" command. 
    Sends a message to start the game and initiates the search for an opponent.

    Args:
        message (Message): The Telegram message object.
    """
    # Send a message to the user indicating that the search for an opponent has begun
    await message.answer("🔎Начинается поиск оппонента.")


@router.message(F.text == '🔘профиль🔘')
async def profile(message: Message):
    """
    Handles the "/profile" command. 
    Sends a message with the user's profile information.

    Args:
        message (Message): The Telegram message object.
    """
    # Get the user's profile information from the database
    user_profile = get_user(message.from_user.id)

    # Format the profile information into a string
    profile_str = (
        f"👤Ваш профиль:\n"
        f"🏆Кол-во РР: {user_profile[2]}\n"
        f"🔑Кол-во Ключей: {user_profile[3]}\n"
        f"🏅Победы: {user_profile[4]}"
    )

    # Send the profile information as a message
    await message.answer(profile_str)


@router.callback_query(F.data == 'cancel')
async def cancel(callback: types.CallbackQuery):
    """
    Handles the callback query when the user cancels the search.

    Args:
        callback (types.CallbackQuery): The Telegram callback query object.
    """
    # Cancel the search and delete the message
    await callback.answer("Поиск отменен",)
    await callback.message.delete()

    # Mark the user as not ready for the game
    ready_falsed(callback.from_user.id)



