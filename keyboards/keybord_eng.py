from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_button_1_eng = KeyboardButton(text='YES')
start_button_2_eng = KeyboardButton(text='NO')

keyboard_yes_no_eng = ReplyKeyboardMarkup(
    keyboard=[[start_button_1_eng, start_button_2_eng]],
    resize_keyboard=True)



start_clava_2_eng = KeyboardButton(text='Select game options')

keyboard_after_finish_eng = ReplyKeyboardMarkup(
    keyboard=[[start_button_1_eng, start_clava_2_eng],
              [start_button_2_eng]],
    resize_keyboard=True)

schet_button_eng = KeyboardButton(text='VS')

keyboard_after_saying_NO_eng = ReplyKeyboardMarkup(
    keyboard=[[start_button_1_eng], [schet_button_eng]],
    resize_keyboard=True)

start_clava_1_eng = KeyboardButton(text='Start game')
start_clava_3_eng = KeyboardButton(text='No, thanks')

start_clava_eng =  ReplyKeyboardMarkup(
    keyboard=[[start_clava_2_eng],[start_clava_1_eng, start_clava_3_eng]],
    resize_keyboard=True,
    input_field_placeholder='SOLO default')


