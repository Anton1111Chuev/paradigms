"""Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
"""


def quick_sort_imperative(lst: list):
    w_stack = [x for x in range(4 + int(len(lst) / 2))]
    k = 0
    w_stack[0] = 0
    w_stack[1] = len(lst) - 1
    while k >= 0:
        i = quick_sort_pos(lst, w_stack[k], w_stack[k + 1])
        if i != w_stack[k + 1]:
            r_l = i + 1
        else:
            r_l = w_stack[k + 1]
        r_r = w_stack[k + 1]
        l_l = w_stack[k]
        if i != w_stack[k]:
            l_r = i - 1
        else:
            l_r = w_stack[k]

        k -= 2
        if r_l != r_r:
            k += 2
            w_stack[k] = r_l
            w_stack[k + 1] = r_r
        if l_l != l_r:
            k += 2
            w_stack[k] = l_l
            w_stack[k + 1] = l_r


def quick_sort_pos(arr, left, right):
    i = left
    j = right - 1
    while True:
        while arr[i] > arr[right]:
            i += 1
        while arr[j] < arr[right] and j > left:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[right], arr[i] = arr[i], arr[right]
    return i


lst = [8, 9, 10, 7, 4, 4, 5]
print(lst)
quick_sort_imperative(lst)
print(lst)
