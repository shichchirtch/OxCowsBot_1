from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


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
ibDel = InlineKeyboardButton(text='delete',callback_data='del_pressed')
ibClear = InlineKeyboardButton(text='clear field',callback_data='clear_pressed')
ibSend = InlineKeyboardButton(text='press button  \U0001f680   \u2B07\uFE0F',callback_data='send_pressed')


ibDelRus = InlineKeyboardButton(text='удалить',callback_data='del_pressed')
ibClearRus = InlineKeyboardButton(text='очистить поле',callback_data='clear_pressed')
ibDel_De = InlineKeyboardButton(text='löschen',callback_data='del_pressed')
ibClear_De = InlineKeyboardButton(text='klares Feld',callback_data='clear_pressed')
ibSendRus = InlineKeyboardButton(text='Нажмите на кнопку c  \U0001f680    \u2B07\uFE0F',callback_data='send_pressed')
ibSend_De = InlineKeyboardButton(text='Drucken   \U0001f680   \u2B07\uFE0F',callback_data='send_pressed')





keyboard_digit_buttons =[[ ib1, ib2, ib3, ib4, ib5 ], [ib6, ib7, ib8, ib9,ib0],
                         [ibClear, ibDel],
                         [ibSend]]

keyboard_digit_buttons_Rus= [[ ib1, ib2, ib3, ib4, ib5 ], [ib6, ib7, ib8, ib9,ib0],
                         [ibClearRus, ibDelRus],
                             [ibSendRus]]

keyboard_digit_buttons_De= [[ ib1, ib2, ib3, ib4, ib5 ], [ib6, ib7, ib8, ib9,ib0],
                         [ibClear_De, ibDel_De],
                            [ibSend_De]]


keyboard_digits_Rus = InlineKeyboardMarkup(
    inline_keyboard=keyboard_digit_buttons_Rus,
    resize_keyboard=True,
    input_field_placeholder='Воспользуйся цифровой клавиатурой !')

keyboard_digits = InlineKeyboardMarkup(
    inline_keyboard=keyboard_digit_buttons,
    resize_keyboard=True,
    input_field_placeholder='Use digit deck !')

keyboard_digits_De = InlineKeyboardMarkup(
    inline_keyboard=keyboard_digit_buttons_De,
    resize_keyboard=True,
    input_field_placeholder='Benutzen Sie den Ziffernblock!')