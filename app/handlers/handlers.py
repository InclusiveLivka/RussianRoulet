from aiogram import F, Router, types 
from aiogram.types import Message,CallbackQuery
import app.keyboard.reply as kb
import sqlite3
import time

from app.keyboard import inline
from app.database.engine import get_user, ready_falsed
from app.game.session import get_enemy

router = Router()


@router.message(F.text == '🔫начать игру🔫')
async def start_game(message: Message,):
    await message.answer("🔎Начинается поиск оппонента.", reply_markup=inline.cancel)
    enemy = get_enemy(message)
    print(enemy)
    # message.answer(f"👤Ваш профиль:\n🏆Кол-во РР: {get_user(enemy)[2]}\n🔑Кол-во Ключей: {get_user(enemy)[3]}\n🏅Победы: {get_user(enemy)[4]}")


@router.message(F.text == '🔘профиль🔘')
async def profile(message: Message):
    await message.answer(f"👤Ваш профиль:\n🏆Кол-во РР: {get_user(message.from_user.id)[2]}\n🔑Кол-во Ключей: {get_user(message.from_user.id)[3]}\n🏅Победы: {get_user(message.from_user.id)[4]}")


@router.callback_query(F.data == 'cancel')
async def cancel(callback: types.CallbackQuery):
    await callback.answer("Поиск отменен",)
    await callback.message.delete()
    ready_falsed(callback.from_user.id)
