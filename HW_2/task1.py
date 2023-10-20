"""Условие
На вход подается число n.
Задача
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
"""


def multiplication_tabl(number: int):
    for i in range(1, number + 1):
        for j in range(1, 10):
            print(f'{i} * {j} = {i * j} ')


number = int(input("Введите число "))
multiplication_tabl(number)

"""Код написан в процедурной и в императивной парадигме"""
