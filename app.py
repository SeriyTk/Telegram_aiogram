from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Создаем переменную бота, где Bot(token=Токен вашего бота)
bot = Bot(token='5240125793:AAFoM4dvZ8j1bqA3jN4EqG6w-5-t3ynhliA')

# Создаем диспетчер
dp = Dispatcher(bot)


@dp.message_handler() # Принимает все сообщения
async def get_message(message : types.Message):
    # Получаем айди пользователя:
    #chat_id = types.Message.chat.id # Первый вариант
    #chat_id = messge.chat.id # Второй вариант

    # Отправляем сообщение пользователю.
    # Вариант №1:
    #chat_id = messge.chat.id
    #text = 'Привет Серега.'
    #await bot.send_message(chat_id=chat_id, text=text)

    # Вариант №2:
    text = f'Привет {message.from_user.full_name}.'
    await message.answer(text=text)
    print(message.text)

executor.start_polling(dp)