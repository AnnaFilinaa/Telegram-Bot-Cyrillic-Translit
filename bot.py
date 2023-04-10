import os
import logging
from aiogram import Bot,Dispatcher,executor,types
# from config import TOKEN
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('TOKEN')

albhabet_dict = {'А': 'A', 
           'Б': 'B',
           'В': 'V',
           'Г': 'G',
           'Д': 'D',
           'Е': 'E',
           'Ё': 'E',
           'Ж': 'ZH',
           'З': 'Z',
           'И': 'I',
           'Й': 'I',
           'К': 'K',
           'Л': 'L',
           'М': 'M',
           'Н': 'N',
           'О': 'O',
           'П': 'P',
           'Р': 'R',
           'С': 'S',
           'Т': 'T',
            'У': 'U',
            'Ф': 'F',
            'Х': 'KH',
            'Ц': 'TS',
            'Ч': 'CH',
            'Ш': 'SH',
            'Щ': 'SHCH',
            'Ь': '',
            'Ы': 'Y',
            'Ъ': 'IE',
            'Э': 'E',
            'Ю': 'IU',
            'Я': 'IA'}

bot=Bot(token=TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    user_name=message.from_user.full_name
    user_id=message.from_user.id
    greetings=f'Здравствуйте, {user_name}! Введите кириллицей свои ФИО'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, greetings)

@dp.message_handler()
async def send_welcome(message:types.Message):
    user_name=message.from_user.full_name
    user_id=message.from_user.id
    text=message.text
    reply_message = ''    
    for i in text.upper():
        try:
            reply_message += albhabet_dict.get(i, i)
        except:
            reply_message += i
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, reply_message)

if __name__ == '__main__':
    executor.start_polling(dp)