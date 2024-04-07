import time
from random import sample
from aiogram.types import Message
from lexicon import language_dict
from config import *


def time_counter(start_time):
    current_time = time.monotonic()
    secund = (current_time - start_time) % 60
    minut = (current_time - start_time) // 60
    return int(minut), int(secund)


def get_secret_kit(bot_str_tally):
    secret_kit = sample(bot_str_tally, k=4)
    return secret_kit

def seek_bools(bot_tally, user_data):  # Сначала то, что угадывается, потом то, что вводится в попытке угадать
    temp_game_arr = []
    for k, num in enumerate(user_data):
        if num not in bot_tally:
            pass
        elif num in bot_tally and num == bot_tally[k]:
            temp_game_arr.append('Ox')
        else:
            temp_game_arr.append('Cow')
    return temp_game_arr


def user_attempt_guess_botCombo(us_dict: dict, userID: int, new_user_combo:list):
    us_dict[userID]['schritt'] += 1
    us_dict[userID]['game_list'].append(new_user_combo)
    return us_dict


def reset_user_dict_after_finish(us_dict: dict, userID: int) -> dict:
    us_dict[userID]['bot_win'] = False
    us_dict[userID]['in_game'] = False
    us_dict[userID]['bot_list'] = []
    us_dict[userID]['game_list'] = []
    us_dict[userID]['total_games'] += 1
    us_dict[userID]['schritt'] = 0
    us_dict[userID]['user_comb'] = 'setting_data'
    us_dict[userID]['game_level'] = us_dict[userID]['Hold_Level']
    us_dict[userID]['secret_kit'] = 'no_data'
    us_dict[userID]['inline_user_kit'] = ''
    us_dict[userID]["first bot data"] = None
    return us_dict


def verify_bools_position(bot_kit: list, secret_kit: list, bot_test_combination: list):
    a, b, c, d = bot_kit
    super_tup = ([a, b, c, d], [a, d, b, c], [a, c, d, b], [a, c, b, d], [a, d, c, b], [a, b, d, c],
                 [b, c, d, a], [b, a, c, d], [b, d, a, c], [b, a, d, c], [b, c, a, d], [b, d, c, a],
                 [c, d, a, b], [c, a, d, b], [c, b, d, a], [c, b, a, d], [c, d, b, a], [c, a, b, d],
                 [d, b, a, c], [d, c, b, a], [d, a, b, c], [d, c, a, b], [d, b, c, a], [d, a, c, b])
    for spisok in super_tup:
        if spisok not in bot_test_combination:
            bot_test_combination.append(spisok)  # Ну и аппендим сразу это в список комбинаций, если его там ещё нет
        if spisok == secret_kit:
            print('bot_test_combination = ', bot_test_combination)
            return bot_test_combination

    return "something goes wrong"


def verify_when_two_cows(bot_data, secret_kit):
    new_arr = []
    for x in bot_data:
        if x in secret_kit:
            new_arr.append(x)
    for y in secret_kit:
        if y not in new_arr:
            new_arr.append(y)
    return new_arr



def format_string(inline: str) -> str:
    empty_space = 4
    dlina_inline = len(inline)
    empty_space = empty_space - dlina_inline
    returned_stroka = inline + "*" * empty_space
    return returned_stroka


def append_kit(bot_kit: list, bot_test_combinations: list):
    if bot_kit not in bot_test_combinations:
        bot_test_combinations.append(bot_kit)
        return bot_test_combinations
    return bot_test_combinations


def check_len_inline_combo(data:str)->bool:
    if len(data)<4:
        return True
    return False


def check_game_list(user_combo:list, game_list:list):
    if user_combo not in game_list:
        return True
    return False


def format_f_string(user_Id: int, user_combo: str, temp_res: list) -> str:
    responce = (f"{language_dict['your combo'][takers[user_Id]['language']]} <b>{user_combo}</b>\n"
                f"<b>{takers[user_Id]['schritt']}</b> {language_dict['Xod'][takers[user_Id]['language']]}")

    if temp_res.count('Ox') == 0:
        if temp_res.count('Cow') == 0:
            string = (responce + f"  {language_dict['no cows'][takers[user_Id]['language']]}   \U0001f937")
            return string
        elif temp_res.count('Cow') == 1:
            string = (responce + f"  <b>1</b>  {language_dict['1 cow'][takers[user_Id]['language']]}     \U0001f42e")
            return string
        else:
            cow_str = " "
            for cow in range(temp_res.count('Cow')):
                cow_str += "\U0001f42e" + "  "
            string = (
                        responce + f"  <b>{temp_res.count('Cow')}</b>  {language_dict['more cows'][takers[user_Id]['language']]}     {cow_str}")
            return string
    elif temp_res.count("Ox") == 1:
        if temp_res.count('Cow') == 0:
            string = (responce + f"  <b>1</b>  {language_dict['1 bull'][takers[user_Id]['language']]}     \U0001f402")
            return string
        elif temp_res.count('Cow') == 1:
            string = (responce + f"  <b>1</b>  {language_dict['1 bull'][takers[user_Id]['language']]}  "
                                 f"  <b>1</b>  {language_dict['1 cow'][takers[user_Id]['language']]}   \U0001f402    \U0001f42e")
            return string
        else:
            cow_str = " "
            for cow in range(temp_res.count('Cow')):
                cow_str += "\U0001f42e" + "  "
            string = (responce + f"  <b>1</b>  {language_dict['1 bull'][takers[user_Id]['language']]}  "
                                 f"  <b>{temp_res.count('Cow')}</b>  {language_dict['more cows'][takers[user_Id]['language']]}   \U0001f402  {cow_str}")
            return string
    elif temp_res.count("Ox") > 1:
        ox_str = " "
        for ox in range(temp_res.count('Ox')):
            ox_str += "\U0001f402" + "  "
        if temp_res.count('Cow') == 0:
            string = (
                        responce + f"  <b>{temp_res.count('Ox')}</b>  {language_dict['more bulls'][takers[user_Id]['language']]}   {ox_str}")
            return string
        if temp_res.count('Cow') == 1:
            string = (
                        responce + f"  <b>{temp_res.count('Ox')}</b>  {language_dict['more bulls'][takers[user_Id]['language']]}  "
                                   f"  <b>1</b>  {language_dict['1 cow'][takers[user_Id]['language']]}   {ox_str} \U0001f42e")
            return string
        else:
            cow_str = " "
            for cow in range(temp_res.count('Cow')):
                cow_str += "\U0001f42e" + "  "

            string = (
                        responce + f"  <b>{temp_res.count('Ox')}</b>  {language_dict['more bulls'][takers[user_Id]['language']]}"
                                   f"  <b>{temp_res.count('Cow')}</b>  {language_dict['more cows'][takers[user_Id]['language']]}  {ox_str} {cow_str}")
            return string


def format_bot_response(user_Id: int, bot_att: str, temp_res: list):
    bot_responce = f"{language_dict['bot says'][takers[user_Id]['language']]} <b>{bot_att}</b>\n"
    if temp_res.count('Ox') == 0:
        if temp_res.count('Cow') == 0:
            string = (bot_responce + f"  {language_dict['no cows'][takers[user_Id]['language']]}   \U0001f937")
            return string
        elif temp_res.count('Cow') == 1:
            string = (
                        bot_responce + f"  <b>1</b>  {language_dict['1 cow'][takers[user_Id]['language']]}     \U0001f42e")
            return string
        else:
            cow_str = " "
            for cow in range(temp_res.count('Cow')):
                cow_str += "\U0001f42e" + "  "
            string = (
                        bot_responce + f"  <b>{temp_res.count('Cow')}</b>  {language_dict['more cows'][takers[user_Id]['language']]}     {cow_str}")
            return string
    elif temp_res.count("Ox") == 1:
        if temp_res.count('Cow') == 0:
            string = (
                        bot_responce + f"  <b>1</b>  {language_dict['1 bull'][takers[user_Id]['language']]}     \U0001f402")
            return string
        elif temp_res.count('Cow') == 1:
            string = (bot_responce + f"  <b>1</b>  {language_dict['1 bull'][takers[user_Id]['language']]}  "
                                     f"  <b>1</b>  {language_dict['1 cow'][takers[user_Id]['language']]}   \U0001f402    \U0001f42e")
            return string
        else:
            cow_str = " "
            for cow in range(temp_res.count('Cow')):
                cow_str += "\U0001f42e" + "  "
            string = (bot_responce + f"  <b>1</b>  {language_dict['1 bull'][takers[user_Id]['language']]}  "
                                     f"  <b>{temp_res.count('Cow')}</b>  {language_dict['more cows'][takers[user_Id]['language']]}   \U0001f402  {cow_str}")
            return string
    elif temp_res.count("Ox") > 1:
        ox_str = " "
        for ox in range(temp_res.count('Ox')):
            ox_str += "\U0001f402" + "  "
        if temp_res.count('Cow') == 0:
            string = (
                        bot_responce + f"  <b>{temp_res.count('Ox')}</b>  {language_dict['more bulls'][takers[user_Id]['language']]}   {ox_str}")
            return string
        if temp_res.count('Cow') == 1:
            string = (
                        bot_responce + f"  <b>{temp_res.count('Ox')}</b>  {language_dict['more bulls'][takers[user_Id]['language']]}  "
                                       f"  <b>1</b>  {language_dict['1 cow'][takers[user_Id]['language']]}   {ox_str} \U0001f42e")
            return string
        else:
            cow_str = " "
            for cow in range(temp_res.count('Cow')):
                cow_str += "\U0001f42e" + "  "

            string = (
                        bot_responce + f"  <b>{temp_res.count('Ox')}</b>  {language_dict['more bulls'][takers[user_Id]['language']]}"
                                       f"  <b>{temp_res.count('Cow')}</b>  {language_dict['more cows'][takers[user_Id]['language']]}  {ox_str} {cow_str}")
            return string

