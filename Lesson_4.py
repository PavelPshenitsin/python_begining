# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
print(list(i**2 for i in ([random.randint(0, 10) for i in range(10)])))


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_1 = ['Манго',"банан", 'Черешня', 'Груша', 'Апельсин', 'Виноград', 'яблоко']
fruit_2 = ["яблоко", 'Апельсин', "банан", "киви", "арбуз", 'Черешня']
random_list = [random.randint(0, 10) for i in range(10)]
print(list(set(fruit_2) & set(fruit_1)))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


print(list(i for i in ([random.randint(-100, 100) for i in range(100)]) if i % 3 == 0 and i > 0 and i % 4 != 0))

# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re
name = input('Пожалуйста введите имя: ')
surname = input('Пожалуйста введите фамилию: ')
email = input('Пожалуйста введите ваш электройнный адрес: ')

email_pattern = '([a-zA-Z_0-9]+@[a-z]+\.(ru|org|com))'
name_surname_pattern = '([A-Z А-Я][а-я a-z]+)'
user_dict = []
def checker(some_str, some_pattern):
    if re.fullmatch(some_pattern, some_str):
       user_dict.append(some_str)

    else:
        print('Ошибка в '+ some_str)


checker(name, name_surname_pattern)
checker(surname, name_surname_pattern)
checker(email, email_pattern)

print('Спасибо! ' + user_dict[0] + ' ' + user_dict[1] + ' ваш электронный адрес: ' + user_dict[2])



# Задача - 2:
# Вам дан текст:



some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче. погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

patter_text = '[\.]{2}'
len_str = str(re.match(patter_text, some_str))
if len(len_str) > 1:
    print('В вашем текст есть места где более двух точек подряд!')
else:
    print('В вашем тексте нет скоплений точек')

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]

def start():
    card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
    card_number = int(card_number)
    pin_code = int(pin_code)
    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            try:
                choice = int(input('Выберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор:'))
                if choice == 3:
                    break
                elif choice > 3:
                    print('Пожалуйста сделайте выбор из предложенных вариантов.')
                process_user_choice(choice, person)
            except ValueError:
                print('Пожалуйста сделайте выбор из предложенных вариантов.')
    else:
        print('Номер карты или пин код введены не верно!')



def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money < 0:
        return 'На вашем счету недостаточно средств!'
    else:
        new_balance = person['money'] - money
        person.update({'money': new_balance})
        return 'Вы сняли {} рублей. Ваш баланс составляет: {} рублей'.format(money, check_account(person))




def process_user_choice(choice, person):
    if choice == 1:
        print('Ваш баланс составляет: {} рублей'.format(check_account(person)))
    elif choice == 2:
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))
    elif choice == 3:
        pass


start()
