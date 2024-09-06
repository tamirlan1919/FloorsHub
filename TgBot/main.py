import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from handlers.handlers import router
import os

logging.basicConfig(level=logging.INFO)

# Объект бота

bot = Bot(token= os.getenv('TOKEN'))
# Диспетчер
dp = Dispatcher()

# Подключаем маршрутизатор с хендлерами
dp.include_router(router)

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Добро пожаловать в центр продаж недвижимости "Этажи" ')

def main():
    asyncio.run(dp.start_polling(bot))

if __name__ == '__main__':
    main()
