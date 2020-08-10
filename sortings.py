def bubble_sort(l, cmp):
    """
    :param l: сортируемый список
    :param cmp: возвращает True, если второй аргумент должен стоять в большей позиции, чем первый
    :return: отсортированный список

    Пузырьковая сортировка
    """
    while True:
        sorted = True
        for i in range(1, len(l)):
            if not cmp(l[i - 1], l[i]):
                l[i], l[i - 1] = l[i - 1], l[i]
                sorted = False

        if sorted:
            break

    return l


def shaker_sort(l, cmp):
    """
    :param l: сортируемый список
    :param cmp: возвращает True, если второй аргумент должен стоять в большей позиции, чем первый
    :return: отсортированный список

    Шейкерная сортировка
    """
    while True:
        sorted = True
        for i in range(1, len(l)):
            if not cmp(l[i - 1], l[i]):
                l[i], l[i - 1] = l[i - 1], l[i]
                sorted = False

        for i in range(len(l) - 1, 0, -1):
            if not cmp(l[i - 1], l[i]):
                l[i], l[i - 1] = l[i - 1], l[i]
                sorted = False

        if sorted:
            break

    return l

