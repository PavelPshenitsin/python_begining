# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

array = ['Манго', 'Черешня', 'Груша', 'Апельсин', 'Виноград']
for i, fruit in enumerate(array):
    print(i + 1, fruit.rjust(10, ' '))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = [2,3,5,7]
set1 = set(list1)
set2 = set(list2)
list3 = set1 - set2
print (list3)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = ['11', '32', '34', '65', '78', '98', '33', '21', '20', '11', '12', '69', '98', '81', '78']
multiplicationResult =[]
divisionResult =[]
i = 0
while i < len(numbers):
    if int(numbers[i])%2==0:
        correctNumb = int(numbers[i])/4
        multiplicationResult.append(correctNumb)
        i+= 1
    elif int(numbers[i])%2!=0:
        ancorrectNumb = int(numbers[i])*2
        divisionResult.append(ancorrectNumb)
        i+=1
print(multiplicationResult)
print(divisionResult)



# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

from math import sqrt

arrayNumbers = [2, -5, 8, 9, -25, 25, 4]
correctArrayNumb = []
i = 0
for arrayNumbers[i] in arrayNumbers:
    if arrayNumbers[i] > 0 and (sqrt(arrayNumbers[i]) - int(sqrt(arrayNumbers[i])) == 0):
        correctArrayNumb.append(int(sqrt(arrayNumbers[i])))
        i += 1
print(correctArrayNumb)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


days = {
    '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
    '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
    '11': 'одинадцатое', '12': 'двинадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
    '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
    '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
    '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
    '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое',
    '31': 'тридцать первое'
}

months = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
    '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
}

data = '02.11.2013'
form = data.split('.')
print('{} {} {}'.format(days[form[0]], months[form[1]], form[2]+' года'))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

from random import randint
randArray= [randint(-100, 100) for i in range(20)]
print(randArray)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

#A
randomList = [randint(1, 10) for i in range(10)]
unRandomList = list(set(randomList))
print(randomList)
print(unRandomList)
#Б
theLastList = []
for item in randomList:
    if randomList.count(item) == 1:
        theLastList.append(item)
print(theLastList)