from aiogram import Dispatcher

from .handlers import router as handler_router
from .start import router as start_router

def setup_routers (dp : Dispatcher) -> None:
    dp.include_router(handler_router)
    dp.include_router(start_router)