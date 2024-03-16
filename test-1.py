import csv


def main(a) -> None:
    """
    Функция обрабатывает файл и создает файл со сводкеой по категориям продуктов
    a - название файла
    :param a:
    :return: None
    """
    sp = []
    with open(a, encoding='utf-8-sig') as products:
        products.readline()
        for i in products.readlines():
            sp.append(i.split('|'))
    sl = {}
    for i in sp:
        if i[1] not in sl.keys():
            sl[i[1]] = int(i[4])
        else:
            sl[i[1]] += int(i[4])
    res_sp = []
    for i in sl.keys():
        res_sp.append({
            'Category': i,
            'countProduct': sl[i]
        })
    with open("products_new.csv", mode="w", encoding='utf-8-sig') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(res_sp[0].keys()), delimiter="|",
                                quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in res_sp:
            writer.writerow(d)


def find(a) -> str:
    """
    a - название категории
    :param a:
    :return: str
    """
    with open("products_new.csv", mode="r", encoding='utf-8-sig') as output_file:
        reader = csv.reader(output_file, delimiter="|")
        for i in reader:
            if i:
                if i[0] == a:
                    count = i[1]
                    break
    return f'В категории {a} находится {count} единиц товара'


main('products.txt')
fn = input()
print(find(fn))
