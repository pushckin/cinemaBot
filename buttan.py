from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


btn_new = ['Новинки фильмы', 'последние 5 фильмы', 'свежие фильмы']
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(*btn_new)

# apps = 'добавить'
# adkd = InlineKeyboardMarkup(resize_key)