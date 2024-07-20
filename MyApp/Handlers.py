from aiogram import F, Router
from aiogram.types import Message
from MyApp import Keyboard

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer("Русская рулетка", reply_markup=)