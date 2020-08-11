def bubble_sort(l: list, cmp):
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


def shaker_sort(l: list, cmp):
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


def comb_sort(l: list, cmp):
    """
    :param l: сортируемый список
    :param cmp: возвращает True, если второй аргумент должен стоять в большей позиции, чем первый
    :return: отсортированный список

    Сортировка расческой
    """

    length = len(l)
    k = 1.2473309
    step = length - 1
    while step > 1:
        for i in range(0, length):
            if i + step >= length:
                break

            if not cmp(l[i], l[i + step]):
                l[i + step], l[i] = l[i], l[i + step]

        step = int(step / k)

    while True:
        sorted = True
        for i in range(1, len(l)):
            if not cmp(l[i - 1], l[i]):
                l[i], l[i - 1] = l[i - 1], l[i]
                sorted = False

        if sorted:
            break

    return l


def insertion_sort(l: list, cmp):
    """
    :param l: сортируемый список
    :param cmp: возвращает True, если второй аргумент должен стоять в большей позиции, чем первый
    :return: отсортированный список

    Сортировка вставками
    """

    for i in range(0, len(l)):
        for j in range(i, 0, -1):
            if not cmp(l[j - 1], l[j]):
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break

    return l



