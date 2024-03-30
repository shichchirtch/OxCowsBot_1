import os
from environs import Env
from aiogram import Bot, Dispatcher
# import Game_handlers
import handlers.comand_handlers, handlers.game_handlers


env = Env()  # Создаем экземпляр класса Env
env.read_env('D:\data\Ivan\Programming\OxCowsBot\env\.env')  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

bot_token = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную bot_token
admin_id = env.int('ADMIN_ID')  # Получаем и преобразуем значение переменной окружения к типу int,


# Создаем объекты бота и диспетчера
bot = Bot(bot_token)
dp = Dispatcher()
# Регистриуем роутеры в диспетчере
dp.include_router(handlers.comand_handlers.Comand_router)
dp.include_router(handlers.game_handlers.Game_router)

if __name__ == '__main__':
    dp.run_polling(bot)