import pars
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
# bot = Bot(token="5537907184:AAHQGIH2QhZilN4PEBTeHMGnzJJiPMygB6E", proxy="http://proxy.server:3128")
bot = Bot(token="5537907184:AAHQGIH2QhZilN4PEBTeHMGnzJJiPMygB6E")
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Здесь просто аниме фото (возможно невсегда)")


@dp.message_handler(commands='chan')
async def chan(message):
    kbPhoto = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Дай тян')
    bt2 = types.KeyboardButton('Выйти')
    kbPhoto.add(bt1, bt2)
    await message.answer('Нажмите на любую кнопку ниже.', reply_markup=kbPhoto)


@dp.message_handler(content_types='text')
async def func_chan(message: types.Message):
    if message.text.lower() == 'дай тян':
        markup = types.InlineKeyboardMarkup()
        butt_mess = types.InlineKeyboardButton('Улучшить качество', url='https://waifu2x.udp.jp/')
        markup.add(butt_mess)
        photo = pars.photo()
        await bot.send_photo(message.chat.id, photo=photo, reply_markup=markup)

    elif message.text.lower() == 'выйти':
        await message.answer('Без вопросов вышел.', reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

