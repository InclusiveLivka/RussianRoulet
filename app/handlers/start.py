from aiogram import F, Router
from aiogram.types import Message
import app.keyboard.reply as kb

from app.database.engine import add_user

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer("Привет, я бот русская рулетка, давай играть?", reply_markup=kb.main)
    add_user(message.from_user.id, message.from_user.username, 0, 0, 0, '') 