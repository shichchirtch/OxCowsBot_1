from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# создаю конструктор клавиатур
kb_builder = ReplyKeyboardBuilder()
#Создаю кнопки
start_button_1 = KeyboardButton(text='ДА')
start_button_2 = KeyboardButton(text='НЕТ')
set_button = KeyboardButton(text='Выбрать уровень игры')
schet_button = KeyboardButton(text='Узнать Счёт')

start_clava_1 = KeyboardButton(text='Начать игру')
start_clava_2 = KeyboardButton(text='Выбрать уровень игры')
start_clava_3 = KeyboardButton(text='Нет, спасибо\nЯ просто посмотреть зашел')

start_clava =  ReplyKeyboardMarkup(
    keyboard=[[start_clava_2],[start_clava_1,start_clava_3]],
    resize_keyboard=True,
    input_field_placeholder='SOLO default')

#  Создаю клавиатуру на согласие играть
keyboard_yes_no = ReplyKeyboardMarkup(
    keyboard=[[start_button_1, start_button_2]],
    resize_keyboard=True)

set_level_button_1 = KeyboardButton(text='SOLO')
set_level_button_2 = KeyboardButton(text='WITH SILLY BOT')
set_level_button_3 = KeyboardButton(text='WITH SMART BOT')

#  Создаю клавиатуру для выбора уровня
keyboard_game_level = ReplyKeyboardMarkup(
    keyboard=[[set_level_button_1],
              [set_level_button_2, set_level_button_3]],
    resize_keyboard=True)

keyboard_after_saying_NO = ReplyKeyboardMarkup(
    keyboard=[[start_button_1], [schet_button]],
    resize_keyboard=True)

keyboard_after_finish = ReplyKeyboardMarkup(
    keyboard=[[start_button_1, start_clava_2 ],
              [start_button_2]],
    resize_keyboard=True)

ib0 = InlineKeyboardButton(text='0',callback_data='0_pressed')
ib1 = InlineKeyboardButton(text='1',callback_data='1_pressed')
ib2 = InlineKeyboardButton(text='2',callback_data='2_pressed')
ib3 = InlineKeyboardButton(text='3',callback_data='3_pressed')
ib4 = InlineKeyboardButton(text='4',callback_data='4_pressed')
ib5 = InlineKeyboardButton(text='5',callback_data='5_pressed')
ib6 = InlineKeyboardButton(text='6',callback_data='6_pressed')
ib7 = InlineKeyboardButton(text='7',callback_data='7_pressed')
ib8 = InlineKeyboardButton(text='8',callback_data='8_pressed')
ib9 = InlineKeyboardButton(text='9',callback_data='9_pressed')



keyboard_digit_buttons =[[ib0, ib1, ib2, ib3, ib4,], [ib5, ib6, ib7, ib8, ib9]]

keyboard_digits = InlineKeyboardMarkup(
    inline_keyboard=keyboard_digit_buttons,
    resize_keyboard=True,
    input_field_placeholder='Жми на кнопки с цифрами !')



pre_start_button = KeyboardButton(text='/start')

pre_start_clava = ReplyKeyboardMarkup(
    keyboard=[[pre_start_button]],
    resize_keyboard=True,
    input_field_placeholder='Жми на кнопку !'
)


usual_button = KeyboardButton(text='send')
usual_clava = ReplyKeyboardMarkup(
        keyboard=[[usual_button]],
        resize_keyboard=True,
        input_field_placeholder='Жми на кнопку !')

