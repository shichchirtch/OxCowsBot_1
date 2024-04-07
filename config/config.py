from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


path = 'D:\data\Ivan\Programming\OxCowsBot\env\.env'


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env('D:\data\Ivan\Programming\OxCowsBot\env\.env')
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


takers = {}

user_name = 'empty'

level_kit = ["SOLO", "WITH SILLY BOT", "WITH SMART BOT", 'Начать игру']

level_kit_with_bot = ["WITH SILLY BOT", "WITH SMART BOT"]

Four_bools = ["Ox", 'Ox', 'Ox', 'Ox']

personal_dict = {
    'user_name': user_name,
    'in_game': False,
    'secret_kit': 'no_data',
    'total_games': 0,
    'wins': 0,
    'game_list': [],
    'bot_list': [],
    'user_comb': 'setting_data',
    'bot_kit': 'empty',
    'bot_win': False,
    'bot_pobeda': 0,
    'language': 0,
    'start_time': None,
    'schritt': 0,
    'first bot data':None,

    'set_SET': 'NotSet',

    'Hold_Level': 'SOLO',
    'game_level': 'SOLO',

    'inline_user_kit': ''}

tallys_str_bot = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

win_arr = ["Ox", 'Ox', 'Ox', 'Ox']
