from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from bs4 import BeautifulSoup
import random


with open('C:/Users/artem/hw10/token.txt') as token:
    secret_token = token.readline()

bot = Bot(token=secret_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hi!\nI'm NEPictureBot!\nI can do Google Image searches for your text")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('I can search images by text in Google) Just send me what request you want to fulfill.')

@dp.message_handler()
async def echo(message: types.Message):
    url = 'https://www.google.ru/search?q=' + message.text + '&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    await bot.send_photo(chat_id=message.from_user.id, photo=random.choice(images[1:]))


if __name__ == '__main__':
    executor.start_polling(dp)