from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(
    keyboard=[KeyboardButton(text="Начать игру"), KeyboardButton(
        text="Профиль"), KeyboardButton(text="Настройки"),[KeyboardButton(text="Рейтинг"),KeyboardButton(text="Магазин ключей")],KeyboardButton(text="Кейсы")],
    
    resize_keyboard=True,
    input_field_placeholder="..."
)
