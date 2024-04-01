from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Router, F
from config import takers


Digit_router = Router()

@Digit_router.callback_query(F.data == '1_pressed')
async def button_1_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 1':
        takers[callback.from_user.id]['inline_user_kit']+='1'
        await callback.message.edit_text(
            text=f'Вы ввели  {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 1 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '2_pressed')
async def button_2_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата  2':
        takers[callback.from_user.id]['inline_user_kit']+='2'
        await callback.message.edit_text(
            text=f'Вы ввели {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 2 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '3_pressed')
async def button_3_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата  3':
        takers[callback.from_user.id]['inline_user_kit']+='3'
        await callback.message.edit_text(
            text=f'Вы ввели {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 3 = ',takers[callback.from_user.id]['inline_user_kit'])


@Digit_router.callback_query(F.data == '4_pressed')
async def button_4_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 4':
        takers[callback.from_user.id]['inline_user_kit']+='4'
        await callback.message.edit_text(
            text=f'Вы ввели  {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 1 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '5_pressed')
async def button_5_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 5':
        takers[callback.from_user.id]['inline_user_kit']+='5'
        await callback.message.edit_text(
            text=f'Вы ввели  {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 5 = ',takers[callback.from_user.id]['inline_user_kit'])


@Digit_router.callback_query(F.data == '6_pressed')
async def button_6_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 6':
        takers[callback.from_user.id]['inline_user_kit']+='6'
        await callback.message.edit_text(
            text=f'Вы ввели  {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 6 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '7_pressed')
async def button_7_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 7':
        takers[callback.from_user.id]['inline_user_kit']+='7'
        await callback.message.edit_text(
            text=f'Вы ввели {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 7 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '8_pressed')
async def button_8_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 8':
        takers[callback.from_user.id]['inline_user_kit']+='8'
        await callback.message.edit_text(
            text=f'Вы ввели  {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 8 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '9_pressed')
async def button_9_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 9':
        takers[callback.from_user.id]['inline_user_kit']+='9'
        await callback.message.edit_text(
            text=f'Вы ввели  {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 9 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '0_pressed')
async def button_0_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 0':
        takers[callback.from_user.id]['inline_user_kit']+='0'
        await callback.message.edit_text(
            text=f'Вы ввели {takers[callback.from_user.id]["inline_user_kit"]}',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    print('us data 0 = ',takers[callback.from_user.id]['inline_user_kit'])
