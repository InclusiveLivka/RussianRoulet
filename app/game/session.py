from aiogram import F, Router
from aiogram.types import Message
import logging


from app.database.engine import get_user,ready_tryed

router = Router()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start_session(message: Message):
    ready_tryed(message.from_user.id)
    print(get_user(message.from_user.id)[-1])
