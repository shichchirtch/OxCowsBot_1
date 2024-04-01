from aiogram.filters import BaseFilter
from aiogram.types import Message
from config.config import takers, level_kit, level_kit_with_bot


class RESTART(BaseFilter):
    async def __call__(self, message: Message):
        if message.from_user.id in takers:
            return False
        return True


class SET_USER_SET(BaseFilter):
    async def __call__(self, message: Message):
        if (message.text in level_kit
                and takers[message.from_user.id]['set_SET'] == 'NotSet'):
            return True
        return False


class BOT_COMB(BaseFilter):
    async def __call__(self, message: Message):
        if takers[message.from_user.id]['secret_kit'] == 'no_data':
            return True
        return False


class DATA_IS_NOT_DIGIT(BaseFilter):
    async def __call__(self, message: Message):
        if not message.text.isdigit():
            return True
        return False


class GAME_STATUS_FALSE(BaseFilter):
    async def __call__(self, message: Message):
        if not takers[message.from_user.id]['in_game']:
            return True
        return False


class GAME_WITH_BOT(BaseFilter):
    async def __call__(self, message: Message):
        if (takers[message.from_user.id]['game_level'] in level_kit_with_bot and
                takers[message.from_user.id]['user_comb'] == 'setting_data'):
            return True
        return False


class DATA_IS_DIGIT(BaseFilter):
    async def __call__(self, message: Message):
        if message.text == 'send':
            temp_combo_set = set(takers[message.from_user.id]['inline_user_kit'])
            if takers[message.from_user.id]['inline_user_kit'].isdigit() and len(temp_combo_set) == 4:
                return True
            return False

        temp_combo_set = set(message.text)
        if message.text.isdigit() and len(temp_combo_set) == 4:
            return True
        return False


class SOLO_GAME_PROCESS(BaseFilter):
    async def __call__(self, message: Message):
        if (takers[message.from_user.id]['game_level'] == "SOLO" and
                takers[message.from_user.id]['user_comb'] == 'setting_data'):
            return True
        return False


class BOT_USER_GAMING(BaseFilter):
    async def __call__(self, message: Message):
        if (takers[message.from_user.id]['game_level'] in level_kit_with_bot and
                takers[message.from_user.id]['user_comb'] != 'setting_data' and
                takers[message.from_user.id]['in_game']):
            return True
        return False


class PRE_START(BaseFilter):
    async def __call__(self, message: Message):
        if message.from_user.id not in takers:
            return True
        return False

class INLINE_FILTER(BaseFilter):
    async def __call__(self, massage:Message):
        if massage.text == 'send':
            return False
        return True

filter_list_for_game_handlers = (SET_USER_SET, BOT_COMB, DATA_IS_NOT_DIGIT, GAME_STATUS_FALSE,
                             DATA_IS_DIGIT, GAME_WITH_BOT, SOLO_GAME_PROCESS, BOT_USER_GAMING)

