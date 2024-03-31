import time
from aiogram import F
from aiogram.filters import Command, CommandStart
from filters.filters import RESTART, SET_USER_SET
from aiogram import Router
from lexicon import *
from config import takers, personal_dict
from logger import std_out_logger
from aiogram.types import Message
from keyboards import start_clava, keyboard_game_level
from copy import deepcopy
from external_functions import time_counter

# Инициализируем роутер уровня модуля
Comand_router = Router()

@Comand_router.message(CommandStart(), RESTART())
async def process_start_command(message: Message):

    user_name = message.chat.first_name
    start_time = time.monotonic()
    # Логируем старт Бота
    std_out_logger.info(f'BOT запущен message = {message.chat.first_name}  time {start_time}')
    await message.answer(text =
        f'Привет, {message.chat.first_name} !  \U0001F60A\n {start_greeding}',
                         reply_markup=start_clava)
    takers[message.from_user.id] = deepcopy(personal_dict)
    takers[message.from_user.id]['user_name'] = user_name
    takers[message.from_user.id]['start_time'] = start_time

    time.sleep(1)

@Comand_router.message(F.text.lower().in_(('rus', 'eng', 'de')))
async def set_language(message: Message):
    print('смена языка')
    if message.from_user.id in takers.keys():
        if message.text == 'rus' or message.text == 'кгы':
            takers[message.from_user.id]['language'] = 0
            await message.answer('\U0001f1f7\U0001f1fa Игра продолжится на русском языке')
        elif message.text == 'eng' or message.text == 'утп':
            takers[message.from_user.id]['language'] = 1
            await message.answer('\U0001f1ec\U0001f1e7 The Game is carry on in English')
        elif message.text == 'de' or message.text == 'ву':
            takers[message.from_user.id]['language'] = 2
            await message.answer('\U0001f1e9\U0001f1ea Das Spiel wird auf Deutsch fortgesetzt')
    else:
        await message.answer(language_dict['start chat'][takers[message.from_user.id]['language']])


@Comand_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    if message.from_user.id in takers.keys():
        if not takers[message.from_user.id]['in_game']:
            await message.answer(text=language_dict['game rules'][takers[message.from_user.id]['language']] + \
                                 takers[message.from_user.id]['user_name'] + \
                                 language_dict['start ?'][takers[message.from_user.id]['language']],
                                 reply_markup=keyboard_game_level)
        else:
            await message.answer(text=language_dict['game rules'][takers[message.from_user.id]['language']] + \
                                      takers[message.from_user.id]['user_name'] + \
                                      language_dict['start ?'][takers[message.from_user.id]['language']])
            await message.answer(text=language_dict['in game querry'][takers[message.from_user.id]['language']])

    else:
        await message.answer('Для начала работы с ботом введите /start')


@Comand_router.message(F.text.in_(['Нет, спасибо\nЯ просто посмотреть зашел', '/cancel', 'cancel']))
async def process_cancel_command(message: Message):
    if message.from_user.id in takers.keys():
        if takers[message.from_user.id]['in_game']:
            takers[message.from_user.id]['in_game'] = False
            takers[message.from_user.id]['game_list'] = []
            takers[message.from_user.id]['game_level'] = 'SOLO'
            takers[message.from_user.id]['secret_kit'] = 'no_data'
            await message.answer(
                language_dict['exit from game'][takers[message.from_user.id]['language']])
            await message.answer_sticker(sticker_dict['process_cancel_command'],
                                         reply_markup=start_clava)
        else:
            await message.answer(text=language_dict['user not in game now'][takers[message.from_user.id]['language']])
                                 #reply_markup=keyboard1)
    else:
        await message.answer(language_dict['if not start'][takers[message.from_user.id]['language']])


@Comand_router.message(F.text.in_(['Выбрать уровень игры', '/set']))
async def set_game_level(message: Message):
    print(f'message = {message.text}')
    if message.from_user.id in takers.keys():
        print(takers)
        if not takers[message.from_user.id]['in_game']:
            await message.answer(text=language_dict['set game level'][takers[message.from_user.id]['language']],
                                reply_markup=keyboard_game_level)
            takers[message.from_user.id]['set_SET'] = 'NotSet'
        else:
            answer = takers[message.from_user.id]['game_level']
            takers[message.from_user.id]['set_attempts'] = 'NotSet'
            await message.answer(language_dict['game level is'][answer][takers[message.from_user.id]['language']] +
                                 takers[message.from_user.id]['game_level'])
    else:
        await message.answer(language_dict['if not start'][takers[message.from_user.id]['language']])


@Comand_router.message(F.text.in_(['/schet','Узнать Счёт']))
async def uznatb_schet(message: Message):
    if message.from_user.id in takers.keys():
        minut, secund = time_counter(takers[message.from_user.id]["start_time"])
        if not takers[message.from_user.id]['in_game']:
            await message.answer(f"{takers[message.from_user.id]['user_name']} : {takers[message.from_user.id]['wins']}\n"
                                 f'BOT : {takers[message.from_user.id]["bot_pobeda"]}\n'
                                 f'Total Game : {takers[message.from_user.id]["total_games"]}'
                                 f'\nGameTiming : {minut} min, {secund} sec.')
            time.sleep(1)
            await  message.answer(text=language_dict['had a look at scores ?'][takers[message.from_user.id]['language']],
                                  reply_markup=start_clava)
        else:
            await message.answer(
                f"{takers[message.from_user.id]['user_name']} : {takers[message.from_user.id]['wins']}\n"
                f'BOT : {takers[message.from_user.id]["bot_pobeda"]}\n'
                f'Total Game : {takers[message.from_user.id]["total_games"]}'
                f'\nGameTiming : {minut} min, {secund} sec.')
            time.sleep(1)
            await  message.answer(
                text=language_dict['in game querry'][takers[message.from_user.id]['language']])
    else:
        await message.answer(language_dict['if not start'][takers[message.from_user.id]['language']])























