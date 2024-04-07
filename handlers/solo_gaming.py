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

k_af = (keyboard_after_finish, keyboard_after_finish_eng, keyboard_after_finish_de)
digit_keyboards_tuple = (keyboard_digits_Rus, keyboard_digits, keyboard_digits_De)
multi_start_clava =(start_clava, start_clava_eng, start_clava_de)
@Solo_router.message(SOLO_GAME_PROCESS(), DATA_IS_DIGIT(), CHEK_SET_STATUS())
async def solo_gaming(message: Message):
    """В хэндлер попадают комбинации юзера в режиме SOLO"""
    takers[message.from_user.id]['in_game'] = True
    userID = message.from_user.id
    if check_secret_nuber(takers, userID):
        takers[userID]['secret_kit'] = get_secret_kit(tallys_str_bot)
        std_out_logger.info(f'BOTs COMBO  =  {takers[message.from_user.id]["secret_kit"]} ')

    if message.text == button_emoji:
        print('this block works !')
        sending_user_combo = list(takers[userID]['inline_user_kit'])  # Если Юзер ввел комбинацию инлайн клавиатурой
    else:
        sending_user_combo = list(message.text)  # Вот здесь присваиваем значение комбинации введенной юзером

    temp_res = seek_bools(takers[userID]['secret_kit'], sending_user_combo)
    if check_game_list(sending_user_combo, takers[userID]["game_list"]):
        user_attempt_guess_botCombo(takers, userID, sending_user_combo)

        std_out_logger.info(
            f"SOLO {takers[userID]['user_name']} ход {takers[userID]['schritt']}, совпадения = {temp_res}")

        if temp_res != Four_bools:
            if message.text == button_emoji:
                current_data = " ".join(list(takers[userID]['inline_user_kit']))
                stroka = format_f_string(userID, current_data, temp_res)
                await message.reply(stroka, reply_markup=usual_clava)
            else:
                current_data = " ".join(sending_user_combo)
                stroka = format_f_string(userID, current_data, temp_res)
                await message.answer(stroka, reply_markup=usual_clava)

            time.sleep(1)
            await message.answer(language_dict["next combo do"][takers[userID]["language"]],
                                 reply_markup=digit_keyboards_tuple[takers[userID]['language']])

            takers[message.from_user.id]['inline_user_kit'] = ''
        else:
            stroka = (f"{takers[userID]['schritt']}  Ход  <b>{temp_res.count('Ox')}</b> "
                      f"<b>{language_dict['more bulls'][takers[userID]['language']]} "
                      f' \U0001f402  \U0001f402  \U0001f402  \U0001f402   !!!</b> \n')
            takers[message.from_user.id]['wins'] += 1
            pip_print = " ".join(takers[userID]["secret_kit"])
            time.sleep(1)
            await message.answer(stroka)
            await message.answer_sticker(sticker_dict['win 4 bools'])
            await message.answer(language_dict['wow'][takers[userID]['language']] +
                                 '<b>' + takers[message.from_user.id]['user_name'] + '</b>' +
                                 language_dict['user guessed'][takers[userID]['language']] +
                                 '<b>'+(pip_print)+'</b>')
            std_out_logger.info(
                f"SOLO ******************* {takers[message.from_user.id]['user_name']} "
                f"ход {takers[userID]['schritt']}  WINS\n")
            time.sleep(1)

            reset_user_dict_after_finish(takers, userID)  # Здесь происходит перезапись значений в словаре юзера
            await message.answer(text=language_dict['play new game after user wins']
                [takers[message.from_user.id]['language']],
                                 reply_markup=k_af[takers[message.from_user.id]['language']])
    else:
        print(takers[message.from_user.id]['game_list'])
        repeated_att = takers[message.from_user.id]['game_list'].index(sending_user_combo)+1
        repeated_data = " ".join(sending_user_combo)
        stroka = format_f_string(userID, repeated_data, temp_res)
        new_stroka = stroka[:40]
        rest_stroka = stroka[54:]
        await message.answer(text=f"{language_dict['repeat combo 1'][takers[userID]['language']]}  <b>{repeated_att}</b> "
                                  f"{language_dict['repeat combo 2'][takers[userID]['language']]}\n"
                                  f"{new_stroka+rest_stroka}",
                             reply_markup=usual_clava
                             )


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
            await message.answer(text=language_dict['wrong sent data'][takers[message.from_user.id]['language']],
                                 reply_markup=digit_keyboards_tuple[takers[message.from_user.id]['language']])
            await message.answer(text=language_dict['next combo do'][takers[message.from_user.id]['language']],
                                 reply_markup=usual_clava)

    else:
        if message.text == ('/start'):
            await message.answer(language_dict['restart'][takers[message.from_user.id]['language']])
        else:
            await message.answer(language_dict['silly bot'][takers[message.from_user.id]['language']])
            await message.answer_sticker(sticker_dict['silly bot'],
                                         reply_markup=multi_start_clava[takers[message.from_user.id]['language']])
