import time
from random import sample
from aiogram.types import Message

def time_counter(start_time):
    current_time = time.monotonic()
    secund = (current_time - start_time) % 60
    minut = (current_time - start_time) // 60
    return int(minut), int(secund)

def get_secret_kit(bot_str_tally):
    secret_kit = sample(bot_str_tally, k=4)
    return secret_kit


def check_bools(funk, secret_data, solo_data):
    sample = ["Ox", 'Ox', 'Ox', 'Ox']
    res = funk(secret_data, solo_data)
    print('check bools works res = ', res)
    if res == sample:
        return solo_data
    return False


def seek_bools(bot_tally, user_data): # Сначала то, что угадывается, потом то, что вводится в попытке угадать
    temp_game_arr = []
    for k, num in enumerate(user_data):
        if num not in bot_tally:
            pass
        elif num in bot_tally and num == bot_tally[k]:
            temp_game_arr.append('Ox')
        else:
            temp_game_arr.append('Cow')
    return temp_game_arr

def user_attempt_guess_botCombo(us_dict:dict, userID:int, message: Message):
    us_dict[userID]['schritt'] += 1
    us_dict[userID]['game_list'].append(message.text)
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
    us_dict[userID]['inline_user_kit']=''
    return us_dict

def verify_bools_position(bot_kit: list, secret_kit: list,  bot_test_combination:list):
    a, b, c, d = bot_kit
    super_tup = ([a, b, c, d], [b, c, d, a], [c, d, a, b], [d, a, b, c], [b, a, d, c], [b, c, a, d], [d, b, c, a],
                 [d, c, b, a], [c, a, d, b], [c, b, d, a], [c, a, b, d], [c, d, b, a], [d, c, a, b], [d, b, a, c],
                 [a, c, b, d], [a, d, b, c], [a, c, d, b], [a, d, c, b], [b, d, a, c], [c, b, a, d], [b,a,c,d])
    func_counter = -1
    for spisok in super_tup:
        func_counter += 1
        bot_test_combination.append(spisok)  # Ну и аппендим сразу это в список комбинаций
        # print('spisok into funk ',bot_test_combination)
        if spisok == secret_kit:
            return bot_test_combination
    return "something goes wrong"

def verify_last_cow(bot_data, secret_kit):
    set_bot_data = set(bot_data)
    set_secret_number = set(secret_kit)
    last_cow = set_secret_number.intersection(set_bot_data).pop()
    return last_cow


def verify_when_two_cows(bot_data, secret_kit):
    new_arr = []
    for x in bot_data:
        if x in secret_kit:
            new_arr.append(x)
    for y in secret_kit:
        if y not in new_arr:
            new_arr.append(y)
    return new_arr


def verify_last_data(bot_kit, secret_kit):
    set_bot_kit = set(bot_kit)
    set_secret_number = set(secret_kit)
    last_data = set_bot_kit.difference(set_secret_number).pop()
    return last_data


def find_one_cow_in_6_numbers(rest_arr, secret_kit):
    last_tally = set(rest_arr).intersection(set(secret_kit)).pop()
    return last_tally

