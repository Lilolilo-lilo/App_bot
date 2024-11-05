import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from config import config

# Настраиваем более подробное логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Создаем объекты бота и диспетчера
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# Создаем клавиатуру с веб-приложением
def get_webapp_keyboard():
    try:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text="Открыть прототип", 
                    web_app=WebAppInfo(url=config.WEBAPP_URL)
                )]
            ]
        )
        return keyboard
    except Exception as e:
        logger.error(f"Ошибка при создании клавиатуры: {e}")
        return None

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        keyboard = get_webapp_keyboard()
        if keyboard:
            await message.answer(
                "Привет! Я бот для доступа к прототипу приложения в Figma.\n"
                "Нажмите на кнопку ниже, чтобы открыть прототип:",
                reply_markup=keyboard
            )
        else:
            await message.answer("Извините, произошла ошибка при создании кнопки.")
    except Exception as e:
        logger.error(f"Ошибка в команде start: {e}")
        await message.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")

# Обработчик команды /prototype
@dp.message(Command("prototype"))
async def cmd_prototype(message: types.Message):
    try:
        keyboard = get_webapp_keyboard()
        if keyboard:
            await message.answer(
                "Нажмите на кнопку ниже, чтобы открыть прототип:",
                reply_markup=keyboard
            )
        else:
            await message.answer("Извините, произошла ошибка при создании кнопки.")
    except Exception as e:
        logger.error(f"Ошибка в команде prototype: {e}")
        await message.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")

# Функция запуска бота
async def main():
    try:
        logger.info("Запуск бота...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}") 