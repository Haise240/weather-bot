import requests
import datetime
from config import bot_token, opweth_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


# Beginning command for bot
@dp.message_handler(commands=["start"])
async def start_command(message: types.message):
    await message.reply("Введите название города")


# Explain for user what can do this bot
@dp.message_handler(commands=["help"])
async def start_command(message: types.message):
    await message.reply("Показывает погоду в городе")


# Request from open weather for any city from input
@dp.message_handler()
async def get_weather(message: types.message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={opweth_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Погода в городе: {city}\nТемпература: {cur_weather}С\n"
                            f"Влажность: {humidity}%\nВетер:{wind} м/с\nДавление:{pressure}")
    except:
        await message.reply("Проверьте название города")


if __name__ == '__main__':
    executor.start_polling(dp)
