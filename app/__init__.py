from .handlers import handler
from .keyboard import reply
from aiogram import Bot
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
bot = Bot(os.getenv("TOKEN"))