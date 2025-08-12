import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from app.handlers import router  # Импортируем роутер с хендлерами
from app.motivsender import send_motivational_quote
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import TOKEN

# Инициализация бота и хранилища
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # Создаем диспетчер с хранилищем

async def on_startup(dp: Dispatcher):
    # Регистрация хендлеров
    dp.include_router(router)  # Включаем роутер с хендлерами

    # Запуск задач для регулярной рассылки
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_motivational_quote, 'interval', minutes=2, args=[bot])
    scheduler.start()

async def main():
    await on_startup(dp)  # Запуск инициализации
    await dp.start_polling(bot)  # Передаем бота в start_polling

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
