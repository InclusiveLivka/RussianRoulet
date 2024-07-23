from aiogram import F, Router, types
from aiogram.types import Message
import app.keyboard.reply as kb
import sqlite3
import time

from app.database.engine import get_user,ready_falsed
from app.game.session import start_session

router = Router()

@router.message(F.text == '🔫начать игру🔫')
async def start_game(message: Message,enemy_profile):
    await message.answer("🔎Начинается поиск оппонента.")
    