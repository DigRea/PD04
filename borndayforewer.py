"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

# Год рождения А.С. Пушкина - 1799
# День рождения А.С. Пушкина - 6 июня

def bornday(year, day=None):
    if year == 1799:
        while day != '6 июня':
            day = input('Введите день рождения А.С. Пушкина: ')
        print('Верно')

year = None
while year != 1799:
    year = int(input('Введите год рождения А.С. Пушкина: '))
    bornday(year)
