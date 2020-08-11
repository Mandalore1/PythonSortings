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


def shell_sort(l: list, cmp):
    """
    :param l: сортируемый список
    :param cmp: возвращает True, если второй аргумент должен стоять в большей позиции, чем первый
    :return: отсортированный список

    Сортировка Шелла
    """

    length = len(l)
    step = length // 2
    while step >= 1:
        for i in range(step, len(l)):
            for j in range(i, step - 1, -step):
                if not cmp(l[j - step], l[j]):
                    l[j], l[j - step] = l[j - step], l[j]
                else:
                    break
        step //= 2

    return l


def selection_sort(l: list, cmp):
    """
    :param l: сортируемый список
    :param cmp: возвращает True, если второй аргумент должен стоять в большей позиции, чем первый
    :return: отсортированный список

    Сортировка выбором
    """

    for i in range(0, len(l)):
        m, mi = l[i], i
        for j in range(i + 1, len(l)):
            if not cmp(m, l[j]):
                m, mi = l[j], j

        l[i], l[mi] = l[mi], l[i]

    return l
