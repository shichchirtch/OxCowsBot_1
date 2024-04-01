from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
import handlers

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
dp.include_router(handlers.digit_buttons.Digit_router)


async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/set',
                   description='Выбрать вариант игры'),
        BotCommand(command='/schet',
                   description='Узнать счёт'),
        BotCommand(command='/cancel',
                   description='Закончить игру')
    ]

    await bot.set_my_commands(main_menu_commands)
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
dp.startup.register(set_main_menu)

if __name__ == '__main__':
    dp.run_polling(bot)