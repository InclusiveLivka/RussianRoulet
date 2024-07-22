from aiogram import F, Router, types
from aiogram.types import Message
import app.keyboard.reply as kb
import sqlite3

from app.database.engine import get_user
from app.game.session import start_session

router = Router()


@router.message(F.text == '🔫начать игру🔫')
async def start_game(message: Message):
    await message.answer("🔎Начинается поиск оппонента.")
    start_session(message)


@router.message(F.text == '🔘профиль🔘')
async def profile(message: Message):
    await message.answer(f"👤Ваш профиль: {get_user(message.from_user.id)[1]}\n🏆Кол-во РР: {get_user(message.from_user.id)[2]}\n🔑Кол-во Ключей: {get_user(message.from_user.id)[3]}\n🏅Победы: {get_user(message.from_user.id)[4]}")
