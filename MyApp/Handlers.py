from aiogram import F, Router
from aiogram.types import Message
import MyApp.Keyboard as kb

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer("Русская рулетка", reply_markup=kb.main)