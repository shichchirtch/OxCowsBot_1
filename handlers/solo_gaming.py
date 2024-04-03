from aiogram import Router
from logger import std_out_logger
from lexicon import *
from filters import *
from external_functions import *
from keyboards import *
from config import takers, Four_bools
from aiogram.types import Message
import time

Solo_router = Router()

@Solo_router.message(SOLO_GAME_PROCESS(), DATA_IS_DIGIT())
async def solo_gaming(message: Message):
    """В хэндлер попадают комбинации юзера в режиме SOLO"""
    userID = message.from_user.id
    std_out_logger.info(f'\n ********  {takers[message.from_user.id]["user_name"]}, gaming! ********')
    user_attempt_guess_botCombo(takers, userID, message)
    if message.text == 'send':
        sending_user_combo = list(takers[message.from_user.id]['inline_user_kit'])  # Если Юзер ввел комбинацию инлайн клавиатурой
    else:
        sending_user_combo = list(message.text)  # Вот здесь присваиваем значение комбинации введенной юзером

    takers[message.from_user.id]["game_list"].append(sending_user_combo)
    temp_res = seek_bools(takers[message.from_user.id]['secret_kit'], sending_user_combo)

    std_out_logger.info(f"{takers[message.from_user.id]['user_name']} ход {takers[message.from_user.id]['schritt']}, совпадения = {temp_res}")

    if temp_res != Four_bools:
        current_data = " ".join(list(takers[message.from_user.id]['inline_user_kit']))
        stroka = (f"{language_dict['your combo'][takers[message.from_user.id]['language']]} <b>{current_data}</b>\n"
                  f"<b>{takers[message.from_user.id]['schritt']}</b> Ход  "
                  f"<b>{temp_res.count('Ox')}</b> Bulls, <b>{temp_res.count('Cow')}</b> Cows")
        await message.reply(stroka)
        time.sleep(1)

        await message.answer(language_dict["next combo do"][takers[message.from_user.id]["language"]],
                             reply_markup=keyboard_digits)
        await message.answer(text=language_dict['press send'][takers[message.from_user.id]['language']],
                             reply_markup=usual_clava)
        takers[message.from_user.id]['inline_user_kit'] = ''
    else:
        stroka = (f"{takers[message.from_user.id]['schritt']}  Ход  <b>{temp_res.count('Ox')} Bools !!!</b> \n")
        takers[message.from_user.id]['wins'] += 1
        pip_print = " ".join(takers[message.from_user.id]["secret_kit"])
        time.sleep(1)
        await message.answer(stroka)
        await message.answer_sticker(sticker_dict['win 4 bools'])
        await message.answer(language_dict['wow'][takers[message.from_user.id]['language']] +
                             '<b>'+takers[message.from_user.id]['user_name']+'</b>' +
                             language_dict['user guessed'][takers[message.from_user.id]['language']] +
                             str(pip_print))
        time.sleep(1)

        reset_user_dict_after_finish(takers, userID)  # Здесь происходит перезапись значений в словаре юзера
        await message.answer(text=language_dict['play new game after user wins'][
            takers[message.from_user.id]['language']],
                             reply_markup=keyboard_after_finish)


@Solo_router.message()
async def process_other_answers(message: Message):
    if not message.from_user.id in takers:
        await message.answer(language_dict['start chat'][takers[message.from_user.id]['language']])
    if takers[message.from_user.id]['in_game']:
        if takers[message.from_user.id]['user_comb'] == 'setting_data':
            if takers[message.from_user.id]['game_level'] == "SOLO":
                await message.answer(text=language_dict['in bot combo'][takers[message.from_user.id]['language']])
            else:
                await message.answer(text=language_dict['not repeat'][takers[message.from_user.id]['language']])
        else:
            takers[message.from_user.id]['inline_user_kit'] = ''
            await message.answer(text=language_dict['wrong sent data'][takers[message.from_user.id]['language']])
            await message.answer(text=language_dict['next combo do'][takers[message.from_user.id]['language']],
                                reply_markup=keyboard_digits)
            await message.answer(text=language_dict['press send'][takers[message.from_user.id]['language']],
                                 reply_markup=usual_clava)

    else:
        if message.text == ('/start'):
            await message.answer(language_dict['restart'][takers[message.from_user.id]['language']])
        else:
            await message.answer(language_dict['silly bot'][takers[message.from_user.id]['language']])
            await message.answer_sticker(sticker_dict['silly bot'],
                                         reply_markup=start_clava)
