from sortings import *


def is_sorted(l: list, ascending=True):
    """Проверяет, отсортирован ли список"""
    if len(l) <= 1:
        return True

    if ascending:
        cmp = lambda a, b: b >= a
    else:
        cmp = lambda a, b: b <= a

    for i in range(1, len(l)):
        if not cmp(l[i - 1], l[i]):
            return False

    return True


l = [3, 2, 1, 5, 5]
l = bubble_sort(l, lambda a, b: b <= a)
print(l)
