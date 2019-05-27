
"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html"""


import random
import sys



COUNT_NUMBERS = 90
PLAYER = 15
PC = 15
numbers = random.sample(range(90), 90)
game_numbers = random.sample(range(90), 30)
PLAYER_card = random.sample(game_numbers, 15)
PC_card = [i for i in game_numbers if i not in PLAYER_card]
PLAYER_field = [PLAYER_card[:5], PLAYER_card[5:10], PLAYER_card[10:]]
PC_field = [PC_card[:5], PC_card[5:10], PC_card[10:]]
for PLAYER_line in PLAYER_field:
    PLAYER_line.sort()
    PLAYER_line.insert(random.randint(0, 4), ' ')
    PLAYER_line.insert(random.randint(0, 5), ' ')
    PLAYER_line.insert(random.randint(0, 6), ' ')
    PLAYER_line.insert(random.randint(0, 7), ' ')
for PC_line in PC_field:
    PC_line.sort()
    PC_line.insert(random.randint(0, 4), ' ')
    PC_line.insert(random.randint(0, 5), ' ')
    PC_line.insert(random.randint(0, 6), ' ')
    PC_line.insert(random.randint(0, 7), ' ')



def field(i):
    if i == 0:
        print('•••••••••Ваша карточка•••••••••')
        for line in PLAYER_field:
            for a in line:
                print('{0:>2}'.format(a), end=' ')
            print()

    if i == 1:
        print('•••••Карточка компьютера•••••')
        for line_pc in PC_field:
            for b in line_pc:
                print('{0:>2}'.format(b), end=' ')
            print()

def player_step():
    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y':
        if number in PLAYER_card:
            for i in PLAYER_field:
                try:
                    i.insert(i.index(number), 'X')
                    i.pop(i.index(number))
                except ValueError:
                    continue
            print('\nПринял')
            return 1
        else:
            print('\nВы проиграли.')
            sys.exit()
    if a == 'n':
        if number in PLAYER_card:
            print('\nВы проиграли')
            sys.exit()
        else:
            print('\nПринял')
    if a != 'y' and a != 'n':
        print('\nУказана не известная переменная. Вы проиграли.')
        sys.exit()
def pc_step():
    if number in PC_card:
        for i in PC_field:
            try:
                i.insert(i.index(number), 'X')
                i.pop(i.index(number))
            except ValueError:
                continue
        return 1

for number in numbers:
    COUNT_NUMBERS -= 1
    print('\nНовый бочонок: {} (осталось: {})\n'.format(number, COUNT_NUMBERS))
    field(0)
    field(1)
    if player_step() == 1:
        PLAYER -= 1
    if pc_step() == 1:
        PC -= 1
    if PLAYER == 0:
        print('\nВы победили')
        sys.exit()
    if PC == 0:
        print('\nВы проиграли')
        sys.exit()
    if COUNT_NUMBERS == 0:
        print('Бочонки закончились. Результат:\n'
              'у компьютера осталось {} чисел,\n'
              'у вас осталось {} чисел.'
              .format(PC, PLAYER))

        sys.exit()