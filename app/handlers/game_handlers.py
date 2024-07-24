from aiogram import F, Router, types
from aiogram.types import Message
import app.keyboard.reply as kb
import sqlite3
import time

from app.database.engine import get_user,ready_falsed


router = Router()


def write_enemy (message: Message, profile):
    message.answer(f"Профиль оппонента:\n🏆Кол-во РР: {profile[2]}\n🔑Кол-во Ключей: {profile[3]}\n🏅Победы: {profile[4]}")