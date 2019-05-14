# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
def greeting(name, age, city):
    print(name + ' , ' + age + 'год(а), ' + 'проживает в городе ' + city)

name = input("Здравствуйте! Пожалуйста представьтесь: ")
age = input("Пожалуйста укажите ваш возраст: ")
city = input("Пожалуйста укажите ваш город: ")

greeting(name, age, city)


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_numb(user_numb):
    user_max_numb = user_numb.split(',')
    print(max(user_max_numb) + ' максимальное число в вашем списке.')
user_numb = input('Пожалуста впишите числа через запятую без пробелов (пример - 1,2,3): ')
max_numb(user_numb)


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_arg(users_args):
    users_args_dict = users_args.split(',')
    print(max(users_args_dict, key=len))


users_args = input('Введите любые строковые аргументы черз запятую буз пробелов (пример: ааа,яяяя,зз): ')
max_arg(users_args)

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

eployee = ['Vasilii', 'Ivan', 'Ivan', 'Boris', 'Evgeniya', 'Kristina', 'Semen', 'Anatolii', 'Stepan']
salary = ['50000', '89000', '130000', '500000', '12000', '100000', '112222', '234000', '980000']
salary_dict = dict(zip(eployee, salary))

file = open('salary.txt', 'w', encoding='UTF-8')
for key, item in salary_dict.items():
    file.write('{} - {}'.format(key, item) + '\n')
file.close()

file = open('salary.txt', 'r', encoding='UTF-8')

for line in file:
    name, dash, salary = line.split()
    if int(salary) <= 500000:
        normal_salary_tax = int(salary) * 0.87
        print(name.upper(), dash, normal_salary_tax)
    elif int(salary) > 500000:
        big_salary_tax = int(salary) * 0.87
        # print(name.upper(), dash, big_salary_tax) #Таким образом зарплаты свыше 500000 не выдаёт, и в тот же
        # момент всегда можно убрать "хештег"/закомментированность строки и программа выдаст их.
file.close()

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import random

def attack(person1, person2):
    while int(person1.get('health')) > 0 and int(person2.get('health')) > 0:
        person = random.randint(0, 1)
        if person > 0:
            person1 = player
            person2 = enemy
            print('Атакует ' + person2.get('name'))
        elif person < 1:
            person1 = enemy
            person2 = player
            print('Атакует ' + person2.get('name'))
        person2_attack = int(defence(person2, person1))
        person1_health = int(person1.get('health'))
        result_fight = person1_health - person2_attack
        person1.update({'health': str(result_fight)})
        print('Здоровье ' + person1.get('name') + ' составляет: ' + str(result_fight) + ' единиц')
def defence(person1,person2):
    damage = float(person1.get('damage'))
    armor = float(person2.get('armor'))
    result = damage/armor
    return result


user_name = input('Введите имя вашего персонажа: ')

player = {'name': '', 'health': '100', 'damage': '50', 'armor': '1.2'}
player.update({'name': user_name})
with open('{}.txt'.format(player['name']), 'w', encoding='UTF-8') as file:
    for key, value in player.items():
        file.write(key + ' : ' + str(value) + '\n')

enemy = {'name': 'Монстр_1_lvl', 'health': '100', 'damage': '20', 'armor': '1.2'}
with open('{}.txt'.format(enemy['name']), 'w', encoding='UTF-8') as file:
    for key, value in player.items():
        file.write(key + ' : ' + str(value) + '\n')
attack(player, enemy)
# Задание - 2
# Давайте усложним предыдущее задание,df измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


