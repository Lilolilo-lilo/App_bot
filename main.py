import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import load_config
from keyboards.main_kb import get_main_keyboard

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Загружаем конфигурацию
config = load_config()

# Инициализируем бот и диспетчер
bot = Bot(token=config.token)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы открыть прототип.",
        reply_markup=get_main_keyboard()
    )

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 