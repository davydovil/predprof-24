def bubble_sort(alist) -> list:
    """
            Функция сортирует массив
            alist - название массива
            :param alist:
            :return: list
            """
    for i in range(len(alist) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False
        if no_swap:
            return alist


def find_chip(a) -> str:
    """
    Функция обрабатывает файл и находит самый дешевый товар в категории
    a - название файла
    :param a:
    :return: str
    """
    sp = []
    with open(a, encoding='utf-8-sig') as products:
        products.readline()
        for i in products.readlines():
            sp.append(i.split('|'))
    names_cat = bubble_sort(list(map(lambda x: x[0], sp)))[-1]
    f_chip = list(filter(lambda x: x[0] == names_cat, sp))
    chip = ['', '', '','', '10000000000.0']
    for i in f_chip:
        chip = min(chip, i, key=lambda x: float(x[4].strip()))
    return f'В категории: {chip[0]} самый дешевый товар: {chip[1]} его цена за единицу товара составляет {chip[4]}'



print(find_chip('products.txt'))
