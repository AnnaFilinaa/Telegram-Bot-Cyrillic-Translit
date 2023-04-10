import os
import logging
from aiogram import Bot,Dispatcher,executor,types
# from config import TOKEN
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('TOKEN')

albhabet_dict = {'а': 'a', 
           'б': 'b',
           'в': 'v',
           'г': 'g',
           'д': 'd',
           'е': 'e',
           'ё': 'e',
           'ж': 'zh',
           'з': 'z',
           'и': 'i',
           'й': 'i',
           'к': 'k',
           'л': 'l',
           'м': 'm',
           'н': 'n',
           'о': 'o',
           'п': 'p',
           'р': 'r',
           'с': 's',
           'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'kh',
            'ц': 'ts',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'shch',
            'ь': '',
            'ы': 'y',
            'ъ': 'ie',
            'э': 'e',
            'ю': 'iu',
            'я': 'ia'}

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
    for i in text:
            if i.islower():
                reply_message += albhabet_dict.get(i, i)
            elif i.isupper():
                reply_message += (albhabet_dict.get((i.lower()), i)).upper()
            else:
                reply_message += i
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, reply_message)

if __name__ == '__main__':
    executor.start_polling(dp)