from aiogram.types import CallbackQuery
from lexicon import language_dict
from aiogram import Router, F
from config import takers
from external_functions import format_string


Digit_router = Router()

@Digit_router.callback_query(F.data == '1_pressed')
async def button_1_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 1':
        takers[callback.from_user.id]['inline_user_kit']+='1'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text= '\U0001f928'+' '*19+f'Вы ввели  <b>{pattern}</b>'+' '*19+'\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 1 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '2_pressed')
async def button_2_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата  2':
        takers[callback.from_user.id]['inline_user_kit']+='2'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 2 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '3_pressed')
async def button_3_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата  3':
        takers[callback.from_user.id]['inline_user_kit']+='3'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 3 = ',takers[callback.from_user.id]['inline_user_kit'])


@Digit_router.callback_query(F.data == '4_pressed')
async def button_4_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 4':
        takers[callback.from_user.id]['inline_user_kit']+='4'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 1 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '5_pressed')
async def button_5_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 5':
        takers[callback.from_user.id]['inline_user_kit']+='5'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 5 = ',takers[callback.from_user.id]['inline_user_kit'])


@Digit_router.callback_query(F.data == '6_pressed')
async def button_6_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 6':
        takers[callback.from_user.id]['inline_user_kit']+='6'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 6 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '7_pressed')
async def button_7_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 7':
        takers[callback.from_user.id]['inline_user_kit']+='7'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 7 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '8_pressed')
async def button_8_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 8':
        takers[callback.from_user.id]['inline_user_kit']+='8'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 8 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '9_pressed')
async def button_9_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 9':
        takers[callback.from_user.id]['inline_user_kit']+='9'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 9 = ',takers[callback.from_user.id]['inline_user_kit'])

@Digit_router.callback_query(F.data == '0_pressed')
async def button_0_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Была нажата 0':
        takers[callback.from_user.id]['inline_user_kit']+='0'
        pattern = format_string(takers[callback.from_user.id]["inline_user_kit"])
        await callback.message.edit_text(
            text='\U0001f928' + ' ' * 19 + f'Вы ввели  <b>{pattern}</b>' + ' ' * 19 + '\u27A1\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('us data 0 = ',takers[callback.from_user.id]['inline_user_kit'])


@Digit_router.callback_query(F.data == 'del_pressed')
async def button_del_press(callback: CallbackQuery):
    await callback.answer()
    if callback.message.text != 'Удалить предыдущий символ':
        if len(takers[callback.from_user.id]['inline_user_kit'])>1:
            takers[callback.from_user.id]['inline_user_kit']=takers[callback.from_user.id]['inline_user_kit'][:-1]
            await callback.message.edit_text(
                text=f"\u27A1\uFE0F           Введите  ваше комбо   {takers[callback.from_user.id]['inline_user_kit']}      \U0001f535",
                reply_markup=callback.message.reply_markup)
        elif len(takers[callback.from_user.id]['inline_user_kit']) == 1:
            takers[callback.from_user.id]['inline_user_kit']=''
            await callback.message.edit_text(
                text=f"\u27A1\uFE0F         Введите  комбо  заново   <b>{takers[callback.from_user.id]['inline_user_kit']}</b>    \U0001f535",
                reply_markup=callback.message.reply_markup)
        elif len(takers[callback.from_user.id]['inline_user_kit'])==0:
            await callback.message.edit_text(
                text=f'\u21AA\uFE0F                   Удалять нечего)))            \U0001f937\u200D\u2642\uFE0F',
                reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('inline_user_kit last tilly del = ',takers[callback.from_user.id]['inline_user_kit'])


@Digit_router.callback_query(F.data == 'clear_pressed')
async def button_clear_press(callback: CallbackQuery):
    await callback.answer('clear')
    if len(takers[callback.from_user.id]['inline_user_kit']) > 0:
        if callback.message.text != 'Начать заново':
            takers[callback.from_user.id]['inline_user_kit'] = ''
            await callback.message.edit_text(
                text=f"{language_dict['not repeat'][takers[callback.from_user.id]['language']]}",
                reply_markup=callback.message.reply_markup)
    else:
        await callback.message.edit_text(
            text=f'\u21AA\uFE0F                  Удалять нечего)))            \U0001f937\u200D\u2642\uFE0F',
            reply_markup=callback.message.reply_markup)
    await callback.answer('*****')

    # print('inline_user_kit cleared ')
