import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hcode, hunderline, hlink
from aiogram.dispatcher.filters import Text
from config import api_t, user_id
from pars import check_film_updet
import json
from buttan import kb

bot = Bot(token=api_t, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_buttn(message: types.Message):
    await message.answer('Кино и Сериалы', reply_markup=kb )

@dp.message_handler(Text(equals="Новинки фильмы"))
async def get_all_films(message: types.Message):
    with open("new_dict.json", encoding="utf-8") as file:
        new_dict = json.load(file)

    for k, v in sorted(new_dict.items()):
        news = f"{hlink(v['title'], v['link'])}\n"
               # f"{hunderline(v['title'])}\n"



        await message.answer(news)


@dp.message_handler(Text(equals='последние 5 фильмы'))
async def get_last_films(message: types.Message):
    with open("new_dict.json", encoding="utf-8") as file:
        new_dict = json.load(file)

    for k, v in sorted(new_dict.items())[-5:]:
        news = f"{hlink(v['title'], v['link'])}\n"

        await message.answer(news)

@dp.message_handler(Text(equals='свежие фильмы'))
async def get_fresh_films(message: types.Message):
    fresh_films = check_film_updet()

    if len(fresh_films) >= 1:
        for k, v in sorted(fresh_films.items()):
            news = f"{hlink(v['title'], v['link'])}\n"

            await message.answer(news)
    else:
        await message.answer("Пока нет новинок")

async def news_films_min():
    while True:
        fresh_films = check_film_updet()

        if len(fresh_films) >= 1:
            for k, v in sorted(fresh_films.items()):
                news = f"{hlink(v['title'], v['link'])}\n"

                await bot.send_message(user_id, news)

        await asyncio.sleep(3600)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_films_min())
    executor.start_polling(dp, skip_updates=True)