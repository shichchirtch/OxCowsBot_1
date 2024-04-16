from aiogram.types import ContentType
from aiogram import Router, F, html
from logger import logger, std_out_logger, std_err_logger
from lexicon import *
from filters import *
from external_functions import *
from keyboards import *
from config import takers, tallys_str_bot, Four_bools
from aiogram.types import Message, ReplyKeyboardRemove
import time
from aiogram.enums.parse_mode import ParseMode


Game_router = Router()

digit_keyboards_tuple = (keyboard_digits_Rus, keyboard_digits, keyboard_digits_De)
lang_set = (keyboard_after_saying_NO, keyboard_after_saying_NO_eng, keyboard_after_saying_NO_de)
yes_no_kb = (keyboard_yes_no, keyboard_yes_no_eng, keyboard_yes_no_de)
keyafter_finish =(keyboard_after_finish, keyboard_after_finish_eng, keyboard_after_finish_de)
@Game_router.message(F.content_type != ContentType.TEXT)
async def process_notTEXT_answers(message: Message):
    std_err_logger.info(f"{takers[message.from_user.id]['user_name']}   notTEXT works...")
    if takers[message.from_user.id]['in_game']:
        await message.answer(language_dict['wrong sent data'][takers[message.from_user.id]['language']])
    else:
        await message.answer(text=
                             takers[message.from_user.id]['user_name'] + language_dict['wrong content type'][
                                 takers[message.from_user.id]['language']],
                             reply_markup=keyboard_yes_no)


@Game_router.message(SET_USER_SET())
async def set_user_set(message: Message):  # Здесь юзер устанавливает уровень игры

    if message.text == 'Начать игру':
        takers[message.from_user.id]['game_level'] = 'SOLO'
        takers[message.from_user.id]['Hold_Level'] = 'SOLO'
        takers[message.from_user.id]['set_SET'] = 'SET'
        await message.answer(text=f"{language_dict['choosing level is'][takers[message.from_user.id]['language']]}"
                                  f"<b>{takers[message.from_user.id]['game_level']}</b>   \n"
                                  f"{language_dict['game start ?'][takers[message.from_user.id]['language']]}",
                             reply_markup=yes_no_kb[takers[message.from_user.id]['language']])
    else:
        if not takers[message.from_user.id]['in_game']:
            takers[message.from_user.id]['game_level'] = message.text
            takers[message.from_user.id]['Hold_Level'] = message.text
            takers[message.from_user.id]['set_SET'] = 'SET'
            await message.answer(text=f"{language_dict['choosing level is'][takers[message.from_user.id]['language']]}"
                                      f"<b>{takers[message.from_user.id]['game_level']}</b>  \n"
                                      f"{language_dict['game start ?'][takers[message.from_user.id]['language']]}",
                                 reply_markup=yes_no_kb[takers[message.from_user.id]['language']])
        else:
            await message.answer(
                language_dict['game level is'][message.text][takers[message.from_user.id]['language']])


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
@Game_router.message(DATA_IS_NOT_DIGIT(), BOT_COMB(), GAME_STATUS_FALSE(), F.text.lower().in_(positiv_answer))
async def process_positive_answer(message: Message):
    await message.answer_sticker(sticker_dict['rocket bull'],
                                 reply_markup=usual_clava)
    takers[message.from_user.id]['in_game'] = True
    if takers[message.from_user.id]['Hold_Level'] == 'SOLO':
        std_err_logger.info(
            f'\nЮзер {takers[message.from_user.id]["user_name"]} играет {takers[message.from_user.id]["total_games"] + 1} игру')

        takers[message.from_user.id]["secret_kit"] = get_secret_kit(tallys_str_bot)
        std_out_logger.info(f'BOTs COMBO  =  {takers[message.from_user.id]["secret_kit"]} ')
        time.sleep(1)
        await message.answer(language_dict['solo_bot_guessed'][takers[message.from_user.id]['language']],
                             reply_markup=digit_keyboards_tuple[takers[message.from_user.id]['language']])


    elif takers[message.from_user.id]['Hold_Level'] == 'WITH SILLY BOT':

        takers[message.from_user.id]["secret_kit"] = get_secret_kit(tallys_str_bot)
        logger.warning(f'Структура словаря takers =  {takers}')
        std_out_logger.info(f'BOTs NUMBER  =  {takers[message.from_user.id]["secret_kit"]} ')
        await message.answer(language_dict['bot_ask_user_combo'][takers[message.from_user.id]['language']],
                             reply_markup=usual_clava)

    elif takers[message.from_user.id]['Hold_Level'] == 'WITH SMART BOT':
        takers[message.from_user.id]["secret_kit"] = get_secret_kit(tallys_str_bot)
        std_out_logger.info(f'BOTs NUMBER  =  {takers[message.from_user.id]["secret_kit"]} ')
        await message.answer(language_dict['bot_ask_user_combo'][takers[message.from_user.id]['language']],
                             reply_markup=usual_clava)


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@Game_router.message(F.text.lower().in_(negative_answer))
async def process_negative_answer(message: Message):

    takers[message.from_user.id]['set_SET'] = 'NotSet' # Эта натсройка не позволит продолжить игру просто вводом комбинаций

    std_out_logger.info(f'Юзер {takers[message.from_user.id]["user_name"]} ответил нет !')
    if not takers[message.from_user.id]['in_game']:
        await message.answer(text=language_dict['pity'][takers[message.from_user.id]['language']],
                             reply_markup=ReplyKeyboardRemove())
        await message.answer_sticker(sticker_dict['negative answer'],
                                     reply_markup=lang_set[takers[message.from_user.id]['language']])
    elif takers[message.from_user.id]['in_game'] and takers[message.from_user.id]['game_list'] == []:
        std_err_logger.info('User  сказал нет до введения первой комбинации')
        await message.answer(text=language_dict['pity'][takers[message.from_user.id]['language']],
                             reply_markup=ReplyKeyboardRemove())
        await message.answer_sticker(sticker_dict['negative answer'],
                                     reply_markup=lang_set[takers[message.from_user.id]['language']])
    else:
        await message.answer(language_dict['wrong sent data'][takers[message.from_user.id]['language']])


@Game_router.message(DATA_IS_DIGIT(), GAME_WITH_BOT(), EMPTY_BOT_LIST(),
                     NOT_USER_COMBO(), INLINE_FILTER(), CHEK_SET_STATUS())
async def set_user_combo(message: Message):
    """Этот хэндлер срабатывает, только тогда, когда бот   Т О Ж Е     будет отгадывать комбо юзера
        Этот хэндлер должен срабатывать только один раз за игру с ботом !"""
    takers[message.from_user.id]['in_game'] = True

    if check_secret_nuber(takers, message.from_user.id):
        takers[message.from_user.id]['secret_kit'] = get_secret_kit(tallys_str_bot)
        std_out_logger.info(f'BOTs COMBO  =  {takers[message.from_user.id]["secret_kit"]} ')
        await message.answer(language_dict['bot_ask_user_combo'][takers[message.from_user.id]['language']],
                             reply_markup=usual_clava)

    user_combo = list(message.text)
    std_out_logger.info(f'{takers[message.from_user.id]["user_name"]}  zagadal combo   {user_combo}')
    takers[message.from_user.id]["user_comb"] = user_combo

    await message.answer(text=language_dict['after_user_zagadal_combo'][takers[message.from_user.id]['language']],
                         reply_markup=digit_keyboards_tuple[takers[message.from_user.id]['language']])

    final_res = takers[message.from_user.id]["bot_list"]  # сюда будем аппендить все комбинации ответов бота

    #  Что мы имеем на старте
    start_kit = user_combo  # Уже введена и отловлена хэндлером ! ! !

    first_bot_data = get_secret_kit(tallys_str_bot)  # Так бот получает комбинацию, с которой начинает угадывать комбо юзера
    takers[message.from_user.id]["first bot data"]= first_bot_data
    final_res.append(first_bot_data)  # Аппендим первую попытку

    std_out_logger.info(
        f'\n ********  FIRST BOT attempt {takers[message.from_user.id]["bot_list"]}  for  {takers[message.from_user.id]["user_name"]}  ********')

    rest_bot_chisla_arr = list(set(tallys_str_bot).symmetric_difference(set(first_bot_data)))  # Это набор оставшихся
                                                                                                  # неиспользованными при построении первой комбинации ботом чисел

    temp_game_arr = seek_bools(start_kit, first_bot_data)


    if not temp_game_arr:  # То есть  ни коров ни быков не попало к боту
        std_err_logger.info('NOT temp_game_arr works')    # Раскомментируовать логгер, при необходимости !
        bot_data = rest_bot_chisla_arr[:4]  # Новый набор для бота
        final_res = append_kit(bot_data, final_res)  # Ну и аппендим сразу вторую попытку бота угадать в список комбинаций
        first_bot_data = bot_data
        temp_game_arr = seek_bools(start_kit, bot_data)

    ########################################################  len(temp_game_arr) == 1 ########################################
    if len(temp_game_arr) == 1:  # Только одна корова или бык
        std_err_logger.info('temp_game_arr 1 works')  # Раскомментируовать логгер, при необходимости !

        bot_data = rest_bot_chisla_arr[:4]  # Здесь мы перезаписываем значение bot_data на 4 из 6 оставшихся в наборе
        final_res.append(bot_data)  # Ну и аппендим сразу это в список комбинаций
        e, f = rest_bot_chisla_arr[4], rest_bot_chisla_arr[5]
        temp_game_arr = seek_bools(start_kit, bot_data)
        first_bot_data = bot_data
        if len(temp_game_arr) == 1:
            new_bot_data = [bot_data[0], bot_data[1], e, f]
            first_bot_data = new_bot_data
            temp_game_arr = seek_bools(start_kit, new_bot_data)

    if len(temp_game_arr) == 2:
        std_err_logger.info('temp_game_arr 2 works')  #  Раскомментируовать логгер, при необходимости !
        temp_arr = verify_when_two_cows(first_bot_data, start_kit)
        final_res = append_kit(temp_arr, final_res)  # Ну и аппендим сразу это в список комбинаций
        # Дальше Вызовем функцию расставления коров по местам
        final_res = verify_bools_position(temp_arr, start_kit, final_res)


    if len(temp_game_arr) == 3:
        # std_err_logger.info('temp_game_arr 3 works, first bot data = ', first_bot_data)  # Раскомментируовать логгер, при необходимости !
        # Находим последнюю корову в остаtке набора цифр
        last_tally = set(start_kit).difference(set(first_bot_data)).pop()
        right_num = list(set(start_kit).intersection(set(first_bot_data)))
        verifying_arr = right_num + [last_tally]

        final_res = append_kit(verifying_arr, final_res)  # Ну и аппендим сразу это в список комбинаций
        # Дальше Вызовем функцию расставления коров по местам
        final_res = verify_bools_position(verifying_arr, start_kit, final_res)

    if len(temp_game_arr) == 4:
        # std_err_logger.info('temp_game_arr 4 works')  # Раскомментируовать логгер, при необходимости !
        final_res = verify_bools_position(first_bot_data, start_kit, final_res)


    final_res = final_res[::-1]  # Делаю реверс списка, чтобы можно было удалять элементы с конца методом рор()


    if takers[message.from_user.id]["game_level"] == "WITH SMART BOT":
        if len(final_res) > 8:
            first_data = final_res[0]
            final_res = final_res[1:-1:2]
            final_res = final_res[:7]
            arr = [first_data, *final_res,takers[message.from_user.id]["first bot data"]]
            takers[message.from_user.id]["bot_list"] = arr
        else:
            arr = [*final_res, takers[message.from_user.id]["first bot data"]]
            takers[message.from_user.id]["bot_list"] = arr
    else:
        final_res = final_res[:-1]
        takers[message.from_user.id]["bot_list"] = [*final_res, takers[message.from_user.id]["first bot data"]]

    std_err_logger.info(f'Список Бота - {takers[message.from_user.id]["bot_list"]}')



@Game_router.message(BOT_USER_GAMING(), DATA_IS_DIGIT(), CHEK_SET_STATUS())
async def gaming_with_bot(message: Message):
    """Сюда попадают комбинации, которые вводит юзер"""

    userID = message.from_user.id

    if message.text == button_emoji:
        temp_res = list(takers[message.from_user.id]['inline_user_kit'])  # Если Юзер ввел комбинацию инлайн клавиатурой
    else:
        temp_res = list(message.text)  # Вот здесь присваиваем значение комбинации введенной юзером


    if check_game_list(temp_res, takers[userID]["game_list"]):
        final_res = takers[message.from_user.id]['bot_list']
        processing_combo = final_res.pop()  # Последний элемент из списка алгоритма бота
        temp_game_arr = seek_bools(takers[message.from_user.id]['user_comb'], processing_combo)

        std_err_logger.info(
            f'for {takers[message.from_user.id]["user_name"]}   AttemtCOMBO  =  {temp_res} , '
            f'список комбининаций бота : att = {len(takers[message.from_user.id]["bot_list"])},  '
            f'{takers[message.from_user.id]["bot_list"]}')
        if temp_game_arr != Four_bools:
            # USER PART
            user_attempt_guess_botCombo(takers, userID, temp_res)  # Делаем необходимые преoбразования со словарём игрока

            temp_res = seek_bools(takers[message.from_user.id]['secret_kit'], temp_res) # Переводим tem_res в состояние ["Ox", "Cow" ]

            if temp_res != Four_bools:
                if message.text == button_emoji:
                    current_data = " ".join(list(takers[userID]['inline_user_kit']))
                    stroka = format_f_string(userID, current_data, temp_res)
                    await message.reply(stroka, reply_markup=usual_clava)
                else:
                    current_data = " ".join(temp_res)
                    stroka = format_f_string(userID, current_data, temp_res)
                    await message.answer(stroka, reply_markup=usual_clava)
                time.sleep(1)

                bot_test_combo = ' '.join(processing_combo)
                stroka_bot_attempt_combo = format_bot_response(userID, bot_test_combo, temp_game_arr)

                await message.answer(stroka_bot_attempt_combo)
                time.sleep(1)
                await message.answer(language_dict["next combo do"][takers[message.from_user.id]["language"]],
                                     reply_markup=digit_keyboards_tuple[takers[message.from_user.id]['language']])

                takers[message.from_user.id]['inline_user_kit'] = ''

            else:
                std_out_logger.info(f"{takers[message.from_user.id]['user_name']}  - Выигрыш\n")
                stroka = (f"{takers[message.from_user.id]['schritt']}  Ход  <b>{temp_res.count('Ox')} "
                          f"{language_dict['more bulls'][takers[userID]['language']]} "
                          f"  \U0001f402  \U0001f402  \U0001f402  \U0001f402   !!!</b>!!! \n")

                takers[message.from_user.id]['wins'] += 1

                pip_print = " ".join(takers[message.from_user.id]["secret_kit"])
                time.sleep(1)
                await message.answer(stroka)
                await message.answer_sticker(sticker_dict['win 4 bools'])
                await message.answer(f"{language_dict['wow'][takers[userID]['language']]}"
                                 f"{html.bold(html.quote(message.chat.first_name))}"
                                 f"{language_dict['user guessed'][takers[userID]['language']]}"
                                 f"<b>{pip_print}</b>",
                                 parse_mode=ParseMode.HTML)
                time.sleep(1)
                takers[message.from_user.id]['inline_user_kit'] = ''  # обнуляем строку inline_user_kit
                reset_user_dict_after_finish(takers, userID)  # Здесь происходит перезапись значений в словаре юзера
                await message.answer(text=language_dict['play new game after user wins'][
                    takers[message.from_user.id]['language']],
                                     reply_markup=keyafter_finish[takers[message.from_user.id]['language']])

        else:
            bot_win_stroka = (language_dict['bot ugadal'][
                                  takers[message.from_user.id]['language']] + f"<b>{' '.join(processing_combo)}</b>\n"
                              + language_dict['bots COMBO was'][takers[message.from_user.id]['language']] +
                              f"<b>{' '.join(takers[message.from_user.id]['secret_kit'])}</b>\n")
            takers[message.from_user.id]['bot_pobeda'] += 1

            await message.answer(text=bot_win_stroka)
            await message.answer_sticker(sticker_dict['BOT WINS'])
            time.sleep(1)
            takers[message.from_user.id]['inline_user_kit'] = ''
            await message.answer(text=f"Сыграем ещё ?",
                                 reply_markup=keyboard_after_finish)
            reset_user_dict_after_finish(takers, userID)
    else:
        print(' game_handlers  game list =',takers[message.from_user.id]['game_list'])
        repeated_att = takers[message.from_user.id]['game_list'].index(temp_res)+1
        repeated_data = " ".join(temp_res)
        stroka = format_f_string(userID, repeated_data, temp_res)
        new_stroka = stroka[:40]
        rest_stroka = stroka[54:]
        await message.answer(text=f"{language_dict['repeat combo 1'][takers[userID]['language']]}  <b>{repeated_att}</b> "
                                  f"{language_dict['repeat combo 2'][takers[userID]['language']]}\n"
                                  f"{new_stroka+rest_stroka}",
                             reply_markup=usual_clava
                             )


