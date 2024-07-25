from aiogram import F, Router, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import app.keyboard.reply as kb
import sqlite3
import time

router = Router()


choise = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Стрелять в себя", callback_data="Стрелять в себя")], [
                              InlineKeyboardButton(text="Стрелять во врага", callback_data="Стрелять во врага")], [
    InlineKeyboardButton(text="Крутить обойму револьвера", callback_data="Крутить обойму револьвера")]])
