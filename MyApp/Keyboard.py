from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔫начать игру🔫"), KeyboardButton(text="🔘профиль🔘"), KeyboardButton(text="⚙️Настройки⚙️")], [
            KeyboardButton(text="🏆рейтинг🏆"), KeyboardButton(text="🔑магазин ключей🔑"), KeyboardButton(text="💼кейсы💼")]],

    resize_keyboard=True,
    input_field_placeholder="Выбирай действие..."
)
