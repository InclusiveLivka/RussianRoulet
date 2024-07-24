from aiogram import Dispatcher

from .game_handlers import router as game_router
from .handler import router as handler_router
from .start import router as start_router

def setup_routers (dp : Dispatcher) -> None:
    dp.include_router(handler_router)
    dp.include_router(start_router)
    dp.include_router(game_router)