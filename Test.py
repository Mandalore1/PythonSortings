from sortings import *
import random
import time


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


ASCENDING = True

l = []
for i in range(0, 1500):
    l.append(random.randint(10, 99))

if ASCENDING:
    cmp = lambda a, b: b >= a
else:
    cmp = lambda a, b: b <= a

current_milli_time = lambda: int(time.time() * 1000)

print(f"l before sort is {l}")
t1 = current_milli_time()

l = selection_sort(l, cmp)

t2 = current_milli_time()
print(f"l after sort is {l}")

if is_sorted(l, ASCENDING):
    print(f"Sorted, it took {t2 - t1} milliseconds")
else:
    print("Not sorted")