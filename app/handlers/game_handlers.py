from aiogram import F, Router, types
from aiogram.types import Message
import app.keyboard.reply as kb
import sqlite3
import time

from app.database.engine import get_user,ready_falsed


router = Router()


