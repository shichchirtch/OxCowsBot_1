sticker_dict = {'process_cancel_command': 'CAACAgIAAxkBAAEEWGVmBURfPi0uMEx284kly0UH2pEhXgAChAwAAsYawEjlC-Xasn6k_zQE',
                                          'negative answer':'CAACAgIAAxkBAAEEXANmBfwlbMwU8jN-9Dj3KDdmv9om_wACGAMAApzW5wq3XwyYm4vFvjQE',
                                        'win 4 bools':'CAACAgIAAxkBAAEEXB1mBgjqPpXFf7EzEFOISlkgVpYcxAACGgMAApzW5wqlfyp90X0oAjQE',
                                                'silly bot':'CAACAgIAAxkBAAEEYf5mB09Q0Qup4Z7uZjY7Q7bJnSNSdAACIQMAApzW5wofM3WHdLVAUzQE',
                                        'rocket bull':'CAACAgIAAxkBAAEEYfpmB08-hfM94jjkGJ00uFhWuMPM1AACFwMAApzW5wrW9EirtTiB2TQE',
                                        'BOT WINS' :'CAACAgIAAxkBAAEEYfxmB09HXs9KAti6ObqUqwjMZeBSgQACEgMAApzW5wocUkO0JHVdKDQE'
                }
positiv_answer = ['да', 'давай', 'сыграем', 'игра', 'yes', 'es', 'нуы',
                  'играть', 'хочу играть', 'OK', 'ok', 'хочу', 'lfdfq',
                  'хорошо', 'ну', 'ладно', 'lf', 'la', 'da', 'jr', '[jxe', 'ja', 'начать игру']

negative_answer = ['нет', 'не', 'не хочу', 'не буду', 'no', 'net', 'yen', 'ytn', 'nein', 'nicht', 'ne', 'nie']

start_greeding = ('Давайте сыграем в "Быков-Коров" ?\n\n'
                  '\U0001f1f7\U0001f1fa По умолчанию используется русский язык.\n'
                  '\U0001f402 Чтобы переключить язык на английский введите eng,\n'
                  '\U0001f404 чтобы переключить на немецкий введите de\n'
                  '\U0001f1ec\U0001f1e7 Change to Eglish - enter eng!\n'
                  '\U0001f1e9\U0001f1ea Wecksel auf Deitsch - geben Sie de ein !\n'
                  'Чтобы получить правила игры и список доступных\n'
                  'команд - отправьте команду /help')

language_dict = {'if not start': ('Для начала работы с ботом введите /start',
                                  'To start interraction with the bot, enter /start',
                                  'Um mit dem Bot zu arbeiten, geben Sie /start ein'),

                 'game rules': ('\U0001f4e2       Правила игры :\n\n'
                                'Из ряда чисел от 0\uFE0F\u20E3 до 9\uFE0F\u20E3 я составляю комбинацию из '
                                '4\uFE0F\u20E3 неповторяющихся чисел, например 4850, '
                                'а Вам нужно её вычислить, чем скорее, тем лучше\n'
                                'Вы можете просто угадывать мою комбинацию или '
                                'выбрать вариант соревнования, тогда мы с Вами будем ходить по очереди.\n'
                                'Для выбора варианта игры нажмите кнопку /set\n'
                                'По умочанию Вы просто отгадываете мою комбинацию.\n'
                                'Если одна из названных Вами цифр есть в моей комбинации, '
                                f'я говорю - COW, то есть Корова \U0001f404  \n'
                                f'А если она ещё стоит на том же самом месте в наборе, '
                                f'где моя - я говорю  - Ох,  то есть Бык \U0001f402'
                                f'\nИгра заканичивается, когда Вы угадаете '
                                f'все цифры из моего набора '
                                f'и расставите их в таком же порядке, как я загадал !!!   \U0001F609'
                                f'\nДругими словами Вам нужно Ox, Ox, Ox, Ox  или  4\uFE0F\u20E3   \U0001f42e'
                                f'\n\nДоступные команды:\n/help - правила '
                                f'игры и список команд\n'
                                f'/cancel - выйти из игры\n'
                                f'/schet - Посмотреть счёт\n', '', ''),

                 'start ?': ('  :  BOT    \U0001f3c1\n\nНачинаем игру ?    \U0001f920 ',
                             "  :  BOT    \U0001f3c1\n\nLet's start the game?    \U0001f920 ",
                             '  :  BOT    \U0001f3c1\n\nLasst uns das Spiel beginnen?     \U0001f920 '),

                 'exit from game': ('Вы вышли из игры. Если захотите сыграть снова - напишите об этом',
                                    'You are out of the game. If you want to play again, write about it',
                                    'Du bist aus dem Spiel. Wenn du noch einmal spielen möchtest, schreib darüber'),

                 'user not in game now': ('А мы итак с вами не играем.\nМожет, сыграем разок?',
                                          "We don't play with you anyway.\nMaybe we can play once?",
                                          'Wir spielen sowieso nicht mit dir.\nVielleicht können wir einmal spielen?'),

                 'game level is': {'SOLO': ("Вы просто отгадываете комбинацию бота ", "You just guess Bot's combination ",
                                            "Sie erraten einfach die Kombination von Bot "),
                                   'WITH SILLY BOT': ('Вы соревнуетесь с начинающим ботом !   \U0001f916\n',
                                                      'You are competing with a beginner bot! \U0001f916\n',
                                                      'Sie konkurrieren mit einem Anfänger-Bot! \U0001f916\n'),

                                   'WITH SMART BOT': (
                                       'Вы соревнуетесь с прокаченым ботом !  \U0001f468\u200D\U0001f680\n',
                                       'You are competing with a smart bot! \U0001f468\u200D\U0001f680\n',
                                       'Sie konkurrieren mit einem intelligenten Bot! \U0001f468\u200D\U0001f680\n')},

                 'set game level': ("Выберите вариант игры :\n"
                                    "Отгадать комбинацию бота - SOLO    \U0001f402   \U0001f42e   \U0001f402   \U0001f42e\n"
                                    "Загадать свою комбинацию Боту и отгадывать с ним поочередно, кто быстрее !\n"
                                    "С Ботом - новичком - WITH SILLY BOT  \U0001f916\n"
                                    "С прокаченым Ботом WITH SMART BOT    \U0001f468\u200D\U0001f680\n", '', " "),

                 'had a look at scores ?': ('Посмотрел счёт ? \n А теперь сыграем ?',
                                            "Have You checked your result ? \nLet's go playing now ?",
                                            'Hast du dir die Rechnung angesehen? \nLass uns jetzt spielen?'),

                 'wrong sent data': (
                     'Мы же сейчас с вами играем. \nПрисылайте, пожалуйста, комбинацию из ЧЕТЫРЁХ чисел от 0 до 9',
                     "We're playing with you now. \nPlease send your combo fron four numbers from 0 to 9",
                     'Wir spielen jetzt mit dir.\nBitte senden Sie Vier Zahlen Combo von 0 bis 9'),

                 'wrong content type': (',  Вы хотите сыграть в игру ?',
                                        ', do you want to play a game?',
                                        'Willst du ein Spiel spielen?'),

                 'choosing level is': ('Вариант игры - ',
                                       'Game level is ',
                                       'Spiel ist '),

                 'give user combo': (
                 'Теперь загадайте число для комбинацию из 4\uFE0F\u20E3  чисел от 0\uFE0F\u20E3 до 9\uFE0F\u20E3  !',
                 'Now guess a four number combo for me from 0\uFE0F\u20E3 to 9\uFE0F\u20E3 !',
                 'Erraten Sie mir jetzt vier Zählen von 0\uFE0F\u20E3 bis 9\uFE0F\u20E3 !'),

                 'game start ?': ("начинаем ?   \U0001f680", "let's go ?    \U0001f680", 'lass uns beginen   \U0001f680'),

                 'silly bot': ('Я довольно ограниченный бот, давайте просто сыграем в игру?',
                               "I'm a pretty limited bot, let's just play a game?",
                               'Ich bin ein ziemlich eingeschränkter Bot, lass uns einfach ein Spiel spielen?'),

                 'restart': ('Нельзя запусть бота дважды !)))',
                             'This is impossible to start BOT twice',
                             'Das ist unmöch den BOT zu restart'),
                 'start chat': ('Для начала работы с ботом введите /start',
                                'To start working with the bot, enter /start',
                                'Um mit dem Bot zu arbeiten, geben Sie /start ein'
                                ),
                 'solo_bot_guessed': ('   Комбинация загадана !                          \U0001f913\nПопробуйте отгадать !',
                                      "    Bot's COMBO is done !                          \U0001f913\nTry to deencrypt it !",
                                      '    Die Kombination ist versteckt!                 \U0001f913\bVersuchen zu erraten!'),

                 'bot_ask_user_combo': ('Комбинация загадана ! \nЗагадайте мне свою !',
                                        "Bot's COMBO is done ! \nGive me yours !",
                                        'Die Kombination ist versteckt! \nGib mir deine Kombo !'),

                 'after_user_zagadal_combo': ('Вы загадали для меня отличное Комбо !\n'
                                              'Ваш ход, начинайте угадывать !',
                                              "You've made a great Combo for me!\n'"
                                              "Your turn, start guessing !",
                                              'Du hast eine gute Combo für mich gemacht!\n'
                                              'Deine Reihe, fang an zu raten!'),

                 'pity': ('Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом \U0001f197 \u2753',
                          "It's a pity :(\n\nIf you want to play, just write about it  \U0001f197 \u2753",
                          'Schade :(\n\nWenn du mitspielen willst, schreib einfach darüber \U0001f197 \u2753'),

                 'wow': ('Ура !!! \U0001f389 ', 'WELL ! SUPER !!! \U0001f389 ', 'Sehr Gut ! \U0001f389 '),

                 'user guessed': (' Вы угадали !\U0001f3c6\nМою Комбинацию ',
                      'You guessed my Combo \U0001f3c6 ',
                      'Du hast meine Combo erraten \U0001f3c6 '),

                 'play new game after user wins': ('\n\nМожет, сыграем еще?', '\n\nMaybe we can play again?',
                      '\n\nVielleicht können wir wieder spielen?'),

                    'next combo do':("Ваша следующая комбинация   \U0001f914",
                                     "Your next combo    \U0001f914"," Deine folgende kombo    \U0001f914"),

                    'in game querry':('Продолжайте угадывать !', 'Go on !', 'Weitermachen Sie bitte !'),

                    'your combo': ( "Ваша Комбинация  ", "Your Combo is  ", "Deine Combo ist"),
                 'press send' : ('Нажмите кнопку send', 'Press send', 'Drucken send'),

                 'not repeat': ('Придумайте для меня комбинацию из чисел от 0 до 9. \n'
                                'Причем цифры НЕ ДОЛЖНЫ повторяться !',
                                'NOT REOEAT DIGITS !',
                                'Nict widerholen nummern Sie bitte !'),

                 'bot ugadal' : ( "Бот угадал  !    \U0001f973\nВаша комбинация была  ",
                                  'BOT WINS  !    \U0001f973\nYOUR  COMBO WAS  ',
                                  'BOT HAT GEWONNEN  !    \U0001f973\nDEINE COMBO WAR  '),

                 'bots COMBO was':('А моя комбинация  ', 'My Combo was ', 'Meine Combo war  ')



                 }
