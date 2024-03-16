def count(a, name) -> str:
    """
        a - название файла
        name - название товара
        :param a:
        :return: str
    """
    sp = []
    with open(a, encoding='utf-8-sig') as products:
        products.readline()
        for i in products.readlines():
            sp.append(i.split('|'))
    res_sp = list(filter(lambda x: x[1] == name, sp))
    maxi = [0,0,0,0,0]
    res = 0
    if len(res_sp) >= 1:
        for i in res_sp:
            res = max(maxi, i, key=lambda x: float(x[3]) * float(x[4]))
    if res:
        return f"На складе данного товара осталось {res[4]} единиц на общую стоимость - {float(res[3]) * float(res[4])}"
    else:
        return 'Такого продукта нет на складе'


print(count('products.txt', 'Яйца'))