import time
from aiogram import F
from aiogram.filters import Command, CommandStart
from filters import RESTART, PRE_START
from aiogram import Router
from lexicon import *
from config import takers, personal_dict
from logger import std_out_logger
from aiogram.types import ReplyKeyboardRemove
from keyboards import *
from copy import deepcopy
from external_functions import time_counter

# Инициализируем роутер уровня модуля
Comand_router = Router()
yes_no_kb = (keyboard_yes_no, keyboard_yes_no_eng)
@Comand_router.message(CommandStart(), RESTART())
async def process_start_command(message: Message):

    user_name = message.chat.first_name
    start_time = time.monotonic()
    # Логируем старт Бота
    std_out_logger.info(f'\nBOT запущен  \nЮЗЕР -->  {message.chat.first_name}  \nTIME --> {time.ctime()}\n')

    await message.answer(text =
        f'Привет, <b>{message.chat.first_name}</b> !  \U0001F60A\n {start_greeding}',
                         reply_markup=start_clava)
    takers[message.from_user.id] = deepcopy(personal_dict)
    takers[message.from_user.id]['user_name'] = user_name
    takers[message.from_user.id]['start_time'] = start_time

    time.sleep(1)
@Comand_router.message(PRE_START())
async def before_start(message:Message):
    await message.answer(text='Нажми на кнопу <b>start</b> !',
                         reply_markup=pre_start_clava)



@Comand_router.message(F.text.lower().in_(('rus', 'eng', 'de')))
async def set_language(message: Message):
    print('смена языка')
    if message.from_user.id in takers.keys():
        if message.text.lower() == 'rus' or message.text.lower() == 'кгы':
            takers[message.from_user.id]['language'] = 0
            await message.answer('\U0001f1f7\U0001f1fa Игра продолжится на русском языке',
                                 reply_markup=ReplyKeyboardRemove())
        elif message.text.lower() == 'eng' or message.text.lower() == 'утп':
            takers[message.from_user.id]['language'] = 1
            await message.answer('\U0001f1ec\U0001f1e7 The Game is carry on in English',
                                 reply_markup=ReplyKeyboardRemove())
        elif message.text.lower() == 'de' or message.text.lower() == 'ву':
            takers[message.from_user.id]['language'] = 2
            await message.answer('\U0001f1e9\U0001f1ea Das Spiel wird auf Deutsch fortgesetzt',
                                 reply_markup=ReplyKeyboardRemove())
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

start_clava_set = (start_clava, start_clava_eng)
@Comand_router.message(F.text.in_(['Нет, спасибо\nЯ просто посмотреть зашел', '/cancel', 'cancel']))
async def process_cancel_command(message: Message):
    if message.from_user.id in takers.keys():
        std_out_logger.info(f"ЮЗЕР    {takers[message.from_user.id]['user_name']} нажал команду /cancel в  {time.ctime()}")
        if takers[message.from_user.id]['in_game']:
            takers[message.from_user.id]['in_game'] = False
            takers[message.from_user.id]['game_list'] = []
            takers[message.from_user.id]['bot_list'] = []
            takers[message.from_user.id]['game_level'] = 'SOLO'
            takers[message.from_user.id]['secret_kit'] = 'no_data'
            takers[message.from_user.id]['schritt'] = 0
            takers[message.from_user.id]['user_comb'] = 'setting_data'
            takers[message.from_user.id]['bot_kit'] = 'empty'
            takers[message.from_user.id]['set_SET'] = 'NotSet'
            takers[message.from_user.id]['inline_user_kit']=''
            takers[message.from_user.id]["first bot data"] = None
            await message.answer(
                language_dict['exit from game'][takers[message.from_user.id]['language']])
            await message.answer_sticker(sticker_dict['process_cancel_command'],
                                         reply_markup=start_clava_set[takers[message.from_user.id]['language']])
        else:
            await message.answer(text=language_dict['user not in game now'][takers[message.from_user.id]['language']],
                                 reply_markup=yes_no_kb[takers[message.from_user.id]['language']])

    else:
        await message.answer(language_dict['if not start'][takers[message.from_user.id]['language']])


@Comand_router.message(F.text.in_(['Выбрать уровень игры', '/set', 'Select game options', 'Wählen Sie Spieloptionen']))
async def set_game_level(message: Message):

    if message.from_user.id in takers.keys():

        if not takers[message.from_user.id]['in_game']:
            await message.answer(text=f"{language_dict['set game level'][takers[message.from_user.id]['language']]}",
                                reply_markup=keyboard_game_level)
            takers[message.from_user.id]['set_SET'] = 'NotSet'
        else:
            answer = takers[message.from_user.id]['game_level']
            # takers[message.from_user.id]['set_SET'] = 'NotSet'
            await message.answer(language_dict['game level is'][answer][takers[message.from_user.id]['language']] +
                                 takers[message.from_user.id]['game_level'])
    else:
        await message.answer(language_dict['if not start'][takers[message.from_user.id]['language']])


@Comand_router.message(F.text.in_(['/schet','Узнать Счёт', 'VS']))
async def uznatb_schet(message: Message):
    if message.from_user.id in takers.keys():
        time_data = time_counter(takers[message.from_user.id]["start_time"])
        if not takers[message.from_user.id]['in_game']:
            await message.answer(f"<b><i>{takers[message.from_user.id]['user_name']} : {takers[message.from_user.id]['wins']}</i></b>\n"
                                 f'<b><i>BOT : {takers[message.from_user.id]["bot_pobeda"]}</i></b>\n'
                                 f'<b><i>Total Game : {takers[message.from_user.id]["total_games"]}</i></b>\n'
                                 f'{time_data}')
            time.sleep(1)
            await  message.answer(text=language_dict['had a look at scores ?'][takers[message.from_user.id]['language']],
                                  reply_markup=start_clava)
        else:
            await message.answer(
                f"<b><i>{takers[message.from_user.id]['user_name']} : {takers[message.from_user.id]['wins']}</i></b>\n"
                f'<b><i>BOT : {takers[message.from_user.id]["bot_pobeda"]}\n</i></b>'
                f'<b><i>Total Game : {takers[message.from_user.id]["total_games"]}</i></b>\n'
                f'{time_data}')
            time.sleep(1)
            await  message.answer(
                text=language_dict['in game querry'][takers[message.from_user.id]['language']])
    else:
        await message.answer(language_dict['if not start'][takers[message.from_user.id]['language']])























