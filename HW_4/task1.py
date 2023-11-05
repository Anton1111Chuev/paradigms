"""Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь."""


def correlation(lst_x: [float], lst_y: [float]):
    if not len(lst_x)  or len(lst_x) != len(lst_y):
        raise ValueError("incorrect data")
    avr_x = sum(lst_x) / len(lst_x)
    avr_y = sum(lst_y) / len(lst_y)

    return sum(map(lambda x, y: (x - avr_x) * (y - avr_y), lst_x, lst_y)) / (
                sum(map(lambda x: (x - avr_x) ** 2, lst_x)) ** 0.5 * sum(map(lambda y: (y - avr_y) ** 2, lst_y)) ** 0.5)



print(correlation([0, 30], [30, 0]))
