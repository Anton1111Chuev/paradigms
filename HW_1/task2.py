"""Написать точно такую же процедуру, но в декларативном стиле"""


def quick_sort_declarative(lst: list):
    lst.sort(reverse=True)


lst = [8, 9, 10, 7, 4, 4, 5]
print(lst)
quick_sort_declarative(lst)
print(lst)
