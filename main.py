import asyncio
import logging
from aiogram import Bot, Dispatcher


from MyApp import Handlers


# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Создание экземпляра бота
async def main():
    bot = Bot(token="7051918347:AAFBwpX3URN-A8XqNREESwg9QvefdGqGT80")
    db = Dispatcher()
    db.include_router(Handlers.router)

    try:
        await db.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
