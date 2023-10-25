"""Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве."""


def binary_search(sorted_list: list[int], target: int):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        position = (low + high) // 2
        guess = sorted_list[position]

        if target > guess:
            low = position + 1
        elif target < guess:
            high = position - 1
        else:
            return position
    else:
        return -1
