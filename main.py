import asyncio
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hcode, hunderline, hlink
from aiogram.dispatcher.filters import Text
from config import api_t, user_id, chat_id
from pars import check_film_updet, hd_rezka
import json
from buttan import kb

bot = Bot(token=api_t, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_buttn(message: types.Message):
    if message.from_user.id == user_id or message.from_user.role == "admin":
        await message.answer('Кино и Сериалы', reply_markup=kb )
    else:
        await message.answer("Access denied")


@dp.message_handler(Text(equals="Новинки фильмы"))
async def get_all_films(message: types.Message):
    with open("new_dict.json", encoding="utf-8") as file:
        new_dict = json.load(file)

    for k, v in sorted(new_dict.items()):
        news = f"{hlink(v['title'], v['link']), v['movie_img']}\n"
               # f"{hunderline(v['title'])}\n"

        await bot.send_message(chat_id, news)
        await message.answer(news)


@dp.message_handler(Text(equals='последние 5 фильмы'))
async def get_last_films(message: types.Message):
    with open("new_dict.json", encoding="utf-8") as file:
        new_dict = json.load(file)

    for k, v in sorted(new_dict.items())[-5:]:
        news = f"{hlink(v['title'], v['link']), v['movie_img']}\n"

        await message.answer(news)
        await bot.send_message(chat_id, news)

@dp.message_handler(Text(equals='свежие фильмы'))
async def get_fresh_films(message: types.Message):
    fresh_films = check_film_updet()

    if len(fresh_films) >= 1:
        for k, v in sorted(fresh_films.items()):
            news = f"{hlink(v['title'], v['link']), v['movie_img']}\n"

            await message.answer(news)
            await bot.send_message(chat_id, news)
    else:
        await message.answer("Пока нет новинок")
        # await bot.send_message(chat_id, "Пока нет новинок")

async def news_films_min():
    while True:
        fresh_film = check_film_updet()

        if len(fresh_film) >= 1:
            for k, v in sorted(fresh_film.items()):
                news = f"{hlink(v['title'], v['link']), v['movie_img']}\n"

                await bot.send_message(chat_id, news)
                await bot.send_message(user_id, news)
        else:
            None
        #     await bot.send_message(chat_id=chat_id, text="Пока нет свежих новостей...",)

        await asyncio.sleep(120)
        # await asyncio.sleep(20)

if __name__ == '__main__':
    # check_film_updet()
    # hd_rezka()
    loop = asyncio.get_event_loop()
    loop.create_task(news_films_min())
    executor.start_polling(dp, skip_updates=True)