from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv(os.getenv('TOKEN'))

bot = Bot (os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Понедельник').add('Вторник').add('Среда').add('Четверг').add('Пятница').add('Суббота')



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMYZDKf_DzgwiVa2-OYSJx9FlGXQucAAlcYAAKG6ThKVoH7vhsaabIvBA')
    await message.answer(f'{message.from_user.first_name},Привет !!!!!',
                         reply_markup=main)

@dp.message_handler(text='Понедельник')
async def contacts(message: types.Message):
    await message.answer(f'иди нахуй сука')

@dp.message_handler(text='Вторник')
async def contacts(message: types.Message):
    await message.answer(f'я не ебурик')

@dp.message_handler(text='Среда')
async def contacts(message: types.Message):
    await message.answer(f'эщкере')

@dp.message_handler(text='Четверг')
async def contacts(message: types.Message):
    await message.answer(f'мама админа')

@dp.message_handler(text='Пятница')
async def contacts(message: types.Message):
    await message.answer(f'хакбердин')

@dp.message_handler(text='Суббота')
async def contacts(message: types.Message):
    await message.answer(f'каримов')

@dp.message_handler(content_types=['sticker'])
async def check_sticker(message:types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)

@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)









if __name__ == '__main__':
        executor.start_polling(dp)
