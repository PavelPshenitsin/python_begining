import os
import shutil
import sys


def make_dir(i):
    os.mkdir('{}'.format(i))
def remove_dir(i):
    os.rmdir('{}'.format(i))
def ch_dir(i):
    os.chdir(i)
# for r in range(9):
#     make_dir('dir_{}'.format(r+1))
#
# for r in range(9):
#     remove_dir('dir_{}'.format(r+1))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(main_path):
    for i in os.listdir(main_path):
        if os.path.isdir(i) == True:
            print(i)

# main_path = os.getcwd()
#
# list_dir(main_path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)

# first_file = sys.argv[0]
# backup_file = first_file + '.backup'
# copy_file(first_file,backup_file)

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания легко,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import easy as lib

exitos = 'a'
while exitos != '0':
    print('Перейти в папку - выбрать 1')
    print('Просмотреть содержимое текущей папки - выбрать 2')
    print('Удалить папку - выбрать 3')
    print('Создать папку - выбрать 4')
    print('для выхода - выбрать 0')
    exitos = input('Выбрать: ')
    if exitos == '1':
        try:
            dir_name = input('наберите полный путь папки: ')
            lib.ch_dir(dir_name)
        except AttributeError:
            print('Не верный путь.')
        except FileNotFoundError:
            print('Не верный путь.')
    elif exitos == '2':
        dir_name = os.getcwd()
        lib.list_dir(dir_name)
    elif exitos == '3':
        try:
            dir_name = input('наберите полный путь папки: ')
            lib.remove_dir(dir_name)
        except FileNotFoundError:
            print('Папка не была найдена.')
    elif exitos == '4':
        try:
            dir_name = input('наберите полный путь папки: ')
            lib.make_dir(dir_name)
        except FileNotFoundError:
            print('Не верный формат')
    elif exitos == '0':
        pass
    else:
        print('Такого пункта меню нет')


