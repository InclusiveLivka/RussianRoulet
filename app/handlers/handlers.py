from aiogram import F, Router
from aiogram.types import Message
import app.keyboard.reply as kb

router = Router()


@router.message(F.text == '🔫начать игру🔫')
async def start_game(message: Message):
    await message.answer("🔎Начинается поиск оппонента.")
