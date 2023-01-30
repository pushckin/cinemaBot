from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

btn_new = ['Новинки фильмы', 'последние 5 фильмы', 'свежие фильмы']
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(*btn_new)