from aiogram.types import ContentType
from aiogram import Router, F
from logger import logger, std_out_logger, std_err_logger
from lexicon import *
from filters import *
from external_functions import *
from keyboards import *


from config import takers, tallys_str_bot, Four_bools
from aiogram.types import Message, ReplyKeyboardRemove
import time
Game_router = Router()

@Game_router.message(F.content_type != ContentType.TEXT)
async def process_notTEXT_answers(message: Message):
    std_out_logger.info("game handlers block works...")
    if takers[message.from_user.id]['in_game']:
        await message.answer(language_dict['wrong sent data'][takers[message.from_user.id]['language']])
    else:
        await message.answer(text=
                             takers[message.from_user.id]['user_name'] + language_dict['wrong content type'][
                                 takers[message.from_user.id]['language']],
                             reply_markup=keyboard_yes_no)


@Game_router.message(SET_USER_SET())
async def set_user_set(message: Message):  # Здесь юзер устанавливает уровень игры
    std_out_logger.info('set_user_set works')
    if message.text == 'Начать игру':
        takers[message.from_user.id]['game_level'] = 'SOLO'
        takers[message.from_user.id]['Hold_Level'] = 'SOLO'
        takers[message.from_user.id]['set_SET'] = 'SET'
        await message.answer(text=language_dict['choosing level is'][takers[message.from_user.id]['language']] +
                                  takers[message.from_user.id]['game_level'] + " \n" +
                                  language_dict['game start ?'][takers[message.from_user.id]['language']],
                             reply_markup=keyboard_yes_no)
    else:
        if not takers[message.from_user.id]['in_game']:
            takers[message.from_user.id]['game_level'] = message.text
            takers[message.from_user.id]['Hold_Level'] = message.text
            takers[message.from_user.id]['set_SET'] = 'SET'
            await message.answer(text=language_dict['choosing level is'][takers[message.from_user.id]['language']] +
                                      takers[message.from_user.id]['game_level'] + " \n" +
                                      language_dict['game start ?'][takers[message.from_user.id]['language']],
                                 reply_markup=keyboard_yes_no)
        else:
            await message.answer(
                language_dict['game level is'][message.text][takers[message.from_user.id]['language']])


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
@Game_router.message(DATA_IS_NOT_DIGIT(), BOT_COMB(), GAME_STATUS_FALSE(), F.text.lower().in_(positiv_answer))
async def process_positive_answer(message: Message):
    await message.answer_sticker(sticker_dict['rocket bull'])
    takers[message.from_user.id]['in_game'] = True
    if takers[message.from_user.id]['Hold_Level'] == 'SOLO':
        std_out_logger.info(
            f'Юзер {takers[message.from_user.id]["user_name"]} играет {takers[message.from_user.id]["total_games"] + 1} игру')

        takers[message.from_user.id]["secret_kit"] = get_secret_kit(tallys_str_bot)
        std_out_logger.info(f'BOTs COMBO  =  {takers[message.from_user.id]["secret_kit"]} ')
        time.sleep(1)
        await message.answer(language_dict['solo_bot_guessed'][takers[message.from_user.id]['language']],
                             reply_markup=keyboard_digits)
        await message.answer(text=language_dict['press send'][takers[message.from_user.id]['language']],
                             reply_markup=usual_clava)


    elif takers[message.from_user.id]['Hold_Level'] == 'WITH SILLY BOT':

        takers[message.from_user.id]["secret_kit"] = get_secret_kit(tallys_str_bot)
        logger.warning(f'Структура словаря takers =  {takers}')
        std_out_logger.info(f'BOTs NUMBER  =  {takers[message.from_user.id]["secret_kit"]} ')
        await message.answer(language_dict['bot_ask_user_combo'][takers[message.from_user.id]['language']],
                             reply_markup=ReplyKeyboardRemove())

    elif takers[message.from_user.id]['Hold_Level'] == 'WITH SMART BOT':
        takers[message.from_user.id]["secret_kit"] = get_secret_kit(tallys_str_bot)
        logger.warning(f'Структура словаря takers =  {takers}')
        std_out_logger.info(f'BOTs NUMBER  =  {takers[message.from_user.id]["secret_kit"]} ')
        await message.answer(language_dict['bot_ask_user_combo'][takers[message.from_user.id]['language']],
                             reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@Game_router.message(F.text.lower().in_(negative_answer))
async def process_negative_answer(message: Message):
    takers[message.from_user.id]['set_SET'] = 'NotSet'
    std_out_logger.info(f'Юзер {takers[message.from_user.id]["user_name"]} ответил нет !')
    if not takers[message.from_user.id]['in_game']:
        await message.answer(text=language_dict['pity'][takers[message.from_user.id]['language']],
                             reply_markup=ReplyKeyboardRemove())
        await message.answer_sticker(sticker_dict['negative answer'],
                                     reply_markup=keyboard_after_saying_NO)
    elif takers[message.from_user.id]['in_game'] and takers[message.from_user.id]['game_list'] == []:
        std_out_logger.info('Интересно, этот блок когда нибудь сработаeт ?')
        await message.answer(text=language_dict['pity'][takers[message.from_user.id]['language']],
                             reply_markup=ReplyKeyboardRemove())
        await message.answer_sticker(sticker_dict['negative answer'],
                                     reply_markup=keyboard_after_saying_NO)
    else:
        await message.answer(language_dict['wrong sent data'][takers[message.from_user.id]['language']])


@Game_router.message(DATA_IS_DIGIT(), GAME_WITH_BOT(), EMPTY_BOT_LIST())
async def set_user_combo(message: Message):
    """Этот хэндлер срабатывает, только тогда, когда бот тоже  будет отгадывать комбо юзера"""
    print('Этот хэндлер должен срабатывать тольок один раз за игру с ботом !')
    user_combo = list(message.text)
    print(f'print works str 115 user combo {user_combo}')
    takers[message.from_user.id]["user_comb"] = user_combo
    await message.answer(text=language_dict['after_user_zagadal_combo'][takers[message.from_user.id]['language']],
                         reply_markup=keyboard_digits)
    await message.answer(text=language_dict['press send'][takers[message.from_user.id]['language']],
                         reply_markup=usual_clava)


    final_res = takers[message.from_user.id]["bot_list"]  # сюда будем аппендить все комбинации ответов бота
    std_out_logger.info(f'\n NOT PRINT********  {takers[message.from_user.id]["user_name"]}, gaming with BOT! ********')

    # Что мы имеем на старте
    start_kit = user_combo  # Уже введена и отловлена хэндлером ! ! !

    first_bot_data = get_secret_kit(tallys_str_bot)  #  Так бот получает комбинацию, с которой начинает угадывать комбо юзера
    std_err_logger.info(f'first_bot_data =  {first_bot_data}')
    final_res.append(first_bot_data)  # Аппендим первую попытку
    rest_bot_chisla_arr = list(set(tallys_str_bot).symmetric_difference(set(first_bot_data)))  # Это набор оставшихся
                                                                                                    # неиспользованными при построении первой комбинации ботом чисел
    temp_game_arr = seek_bools(start_kit, first_bot_data)

    if not temp_game_arr:  # То есть  ни коров ни быков не попало к боту
        std_err_logger.info('NOT temp_game_arr works')
        bot_data = rest_bot_chisla_arr[:4]  # Новый набор для бота
        final_res.append(bot_data)  # Ну и аппендим сразу вторую попытку бота угадать в список комбинаций
        temp_game_arr = seek_bools(start_kit, bot_data)

        if len(temp_game_arr) == 4:  # если 4 коровы \ быка
            final_res = verify_bools_position(bot_data, start_kit, final_res)

    ########################################################  len(temp_game_arr) == 1 ########################################
    elif len(temp_game_arr) == 1:  # Только одна корова или бык
        std_err_logger.info('temp_game_arr 1 works')
        temp_bot_data = first_bot_data.copy()

        bot_data = rest_bot_chisla_arr[:4]  # Здесь мы перезаписываем значение bot_data на 4 из 6 оставшихся в наборе

        final_res.append(bot_data)  # Ну и аппендим сразу это в список комбинаций
        e, f = rest_bot_chisla_arr[4], rest_bot_chisla_arr[5]
        temp_game_arr = seek_bools(start_kit, bot_data)

        if len(temp_game_arr) == 2:  # Может быть 1, 2 или 3 совпадения
            new_arr = verify_when_two_cows(bot_data, start_kit)
            final_res.append(new_arr)  # Ну и аппендим сразу это в список комбинаций
            final_res = verify_bools_position(new_arr, start_kit, final_res)  # расставляем быков по местам

        elif len(temp_game_arr) == 3:  # Найдём первым делом лишнюю цифру
            last_data = verify_last_data(bot_data, start_kit)
            # Место этой цифры в bot_data
            indx = bot_data.index(last_data)
            # Потом найдём корову из первого набора бота
            last_cow = verify_last_cow(temp_bot_data, start_kit)
            #  Заменим в bot_data лишнюю цифру
            bot_data[indx] = last_cow
            final_res.append(bot_data)  # Ну и аппендим сразу это в список комбинаций
            # Вызовем функцию расставления коров по местам
            std_err_logger.info('temp_game_arr 4 works')
            final_res = verify_bools_position(bot_data, start_kit, final_res)

        elif len(temp_game_arr) == 1:  # Значит оставшиеся 2 цифры точно в нашем наборе !
            # Сначала найдём оставшиеся 2 коровы в 2 наборах бота
            third_cow = verify_last_cow(temp_bot_data, start_kit)
            forth_cow = verify_last_cow(bot_data, start_kit)
            # Дальше собирем их в один спиоск
            fourth_coows_list = [e, f, third_cow, forth_cow]
            final_res.append(fourth_coows_list)  # Ну и аппендим сразу это в список комбинаций
            # Дальше Вызовем функцию расставления коров по местам
            final_res = verify_bools_position(fourth_coows_list, start_kit, final_res)

    elif len(temp_game_arr) == 2:
        std_err_logger.info('temp_game_arr 2 works')
        temp_arr = verify_when_two_cows(first_bot_data, start_kit)
        final_res.append(temp_arr)  # Ну и аппендим сразу это в список комбинаций
        # Дальше Вызовем функцию расставления коров по местам
        final_res = verify_bools_position(temp_arr, start_kit, final_res)

    elif len(temp_game_arr) == 3:
        std_err_logger.info('temp_game_arr 3 works')
        # Находим последнюю корову в остаtке набора цифр
        last_cow = find_one_cow_in_6_numbers(rest_bot_chisla_arr, start_kit)
        print('last_cow = ', last_cow)
        for k, x in enumerate(first_bot_data):
            if x not in start_kit:
                first_bot_data[k] = last_cow
        final_res.append(first_bot_data)  # Ну и аппендим сразу это в список комбинаций
        # Дальше Вызовем функцию расставления коров по местам
        final_res = verify_bools_position(first_bot_data, start_kit, final_res)

    elif len(temp_game_arr) == 4:
        final_res = verify_bools_position(first_bot_data, start_kit, final_res)

    std_err_logger.info(f"Список попыток бота {final_res}")

    final_res = final_res[::-1]  # Делаю реверс списка, чтобы можно было удалять элементы с конца методом рор()
    std_out_logger.info(f'AFTER REWERS 210 user combo = {user_combo}')
    print('reversw попыток бота', final_res, 'att = ', len(final_res))
    if takers[message.from_user.id]["game_level"] == "WITH SMART BOT":
        if len(final_res) > 8:
            final_res = [final_res[0]] + final_res[1:-1:2]
            takers[message.from_user.id]["bot_list"] = final_res[:9]
            std_err_logger.info(f'cutting_fin_res =  {final_res}')
    else:
        takers[message.from_user.id]["bot_list"] = final_res

@Game_router.message(SOLO_GAME_PROCESS(), DATA_IS_DIGIT())
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

    std_out_logger.info(f"{takers[message.from_user.id]['user_name']} temp_res = {temp_res}")

    if temp_res != Four_bools:
        current_data = " ".join(list(takers[message.from_user.id]['inline_user_kit']))
        stroka = (f"{language_dict['your combo'][takers[message.from_user.id]['language']]} {current_data}\n"
                  f"{takers[message.from_user.id]['schritt']} Ход  {temp_res.count('Ox')} Bulls, {temp_res.count('Cow')} Cows")
        await message.reply(stroka)
        time.sleep(1)

        await message.answer(language_dict["next combo do"][takers[message.from_user.id]["language"]],
                             reply_markup=keyboard_digits)
        await message.answer(text=language_dict['press send'][takers[message.from_user.id]['language']],
                             reply_markup=usual_clava)
        takers[message.from_user.id]['inline_user_kit'] = ''
    else:
        stroka = (f"{takers[message.from_user.id]['schritt']}  Ход  {temp_res.count('Ox')} Bools !!! \n")
        takers[message.from_user.id]['wins'] += 1
        pip_print = " ".join(takers[message.from_user.id]["secret_kit"])
        time.sleep(1)
        await message.answer(stroka)
        await message.answer_sticker(sticker_dict['win 4 bools'])
        await message.answer(language_dict['wow'][takers[message.from_user.id]['language']] +
                             takers[message.from_user.id]['user_name'] +
                             language_dict['user guessed'][takers[message.from_user.id]['language']] +
                             str(pip_print))
        time.sleep(1)

        reset_user_dict_after_finish(takers, userID)  # Здесь происходит перезапись значений в словаре юзера
        await message.answer(text=language_dict['play new game after user wins'][
            takers[message.from_user.id]['language']],
                             reply_markup=keyboard_after_finish)


@Game_router.message(BOT_USER_GAMING(), DATA_IS_DIGIT())
async def gaming_with_bot(message: Message):
    """Сюда попадают комбинации, которые вводит юзер"""
    print('test g with bot')
    print('bot_list = ',takers[message.from_user.id]['bot_list'])
    userID = message.from_user.id

    final_res = takers[message.from_user.id]['bot_list']
    processing_combo = final_res.pop()
    temp_game_arr = seek_bools(takers[message.from_user.id]['user_comb'], processing_combo)

    if message.text == 'send':
        temp_res = list(takers[message.from_user.id]['inline_user_kit'])  # Если Юзер ввел комбинацию инлайн клавиатурой
    else:
        temp_res = list(message.text)  # Вот здесь присваиваем значение комбинации введенной юзером
    takers[message.from_user.id]["game_list"].append(temp_res)

    if temp_game_arr != Four_bools:
            # USER PART
        user_attempt_guess_botCombo(takers, userID, message)  # Делаем необходимые преoбразования со словарём игрока
        temp_res = seek_bools(takers[message.from_user.id]['secret_kit'], temp_res)
        if temp_res != Four_bools:
            current_data = " ".join(list(takers[message.from_user.id]['inline_user_kit']))
            stroka = (f"{language_dict['your combo'][takers[message.from_user.id]['language']]} {current_data}\n"
                      f"{takers[message.from_user.id]['schritt']} Ход  {temp_res.count('Ox')} Bulls, {temp_res.count('Cow')} Cows")
            await message.reply(stroka)
            time.sleep(1)

            stroka_bot_attempt_combo = (f"BOT GAMES NEXT !    \U0001f955\n "
                                        f"BOT says  {' '.join(processing_combo)}\n"
                                        f"{temp_game_arr.count('Ox')} Bulls,  {temp_game_arr.count('Cow')} Cows")
            await message.answer(stroka_bot_attempt_combo)
            time.sleep(1)
            await message.answer(language_dict["next combo do"][takers[message.from_user.id]["language"]],
                                 reply_markup=keyboard_digits)
            await message.answer(text=language_dict['press send'][takers[message.from_user.id]['language']],
                                 reply_markup=usual_clava)
            takers[message.from_user.id]['inline_user_kit'] = ''

        else:
            std_out_logger.info(f"{takers[message.from_user.id]['user_name']}  - Выигрыш")
            stroka = (f"{takers[message.from_user.id]['schritt']}  Ход  {temp_res.count('Ox')} Bools !!! \n")
            takers[message.from_user.id]['wins'] += 1

            pip_print = " ".join(takers[message.from_user.id]["secret_kit"])
            time.sleep(1)
            await message.answer(stroka)
            await message.answer_sticker(sticker_dict['win 4 bools'])
            await message.answer(language_dict['wow'][takers[message.from_user.id]['language']] +
                                     takers[message.from_user.id]['user_name'] +
                                     language_dict['user guessed'][takers[message.from_user.id]['language']] +
                                     (pip_print))
            time.sleep(1)
            takers[message.from_user.id]['inline_user_kit'] = '' # обнуляем строку inline_user_kit
            reset_user_dict_after_finish(takers, userID)  # Здесь происходит перезапись значений в словаре юзера
            await message.answer(text=language_dict['play new game after user wins'][
                takers[message.from_user.id]['language']],
                                     reply_markup=keyboard_after_finish)

    else:
        bot_win_stroka = (language_dict['bot ugadal'][takers[message.from_user.id]['language']]+f"{' '.join(processing_combo)}\n"
                          + language_dict['bots COMBO was'][takers[message.from_user.id]['language']]+
                          f"{' '.join(takers[message.from_user.id]['secret_kit'])}\n")
        takers[message.from_user.id]['bot_pobeda'] += 1

        await message.answer(text=bot_win_stroka)
        await message.answer_sticker(sticker_dict['BOT WINS'])
        time.sleep(1)
        takers[message.from_user.id]['inline_user_kit'] = ''
        await message.answer(text=f"Сыграем ещё ?",
                             reply_markup=keyboard_after_finish)
        reset_user_dict_after_finish(takers, userID)

@Game_router.message()
async def process_other_answers(message: Message):
    if not message.from_user.id in takers:
        await message.answer(language_dict['start chat'][takers[message.from_user.id]['language']])
    if takers[message.from_user.id]['in_game']:
        if takers[message.from_user.id]['user_comb']== 'setting_data':
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
