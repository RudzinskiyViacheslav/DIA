# Рудзинский Вячеслав Викторович ИУ5-53Б
# РК-1 по курсу "Разработка интернет-приложений"
from operator import itemgetter


class Developer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Detail:
    def __init__(self, id, name, weight, id_of_developer):
        self.id = id
        self.name = name
        self.weight = weight
        self.dev_id = id_of_developer


class Detail_Developer:
    def __init__(self, id_of_developer, id_of_detail):
        self.id_of_developer = id_of_developer
        self.id_of_detail = id_of_detail

Developer = [
    Developer(1, 'Aerodisc'),
    Developer(2, 'InstrumentSPB'),
    Developer(3, 'InstrumentsMSc'),
    Developer(33, 'Artengo'),
    Developer(11, 'Shtill'),
    Developer(22, 'AntalyaIns')
]

Detail = [
    Detail(1, 'Алебастр', 5000, 1),
    Detail(2, 'Арматура', 1800, 3),
    Detail(3, 'Напильник', 200, 3),
    Detail(4, 'Электролобзик', 3200, 2),
    Detail(5, 'Болгарка', 6400, 3),
    Detail(6, 'Болгарка', 6100, 2)
]

Detail_Developer = [
    Detail_Developer(1, 1),
    Detail_Developer(2, 2),
    Detail_Developer(3, 3),
    Detail_Developer(3, 4),
    Detail_Developer(5, 5),
    Detail_Developer(6, 6),
    Detail_Developer(11, 1),
    Detail_Developer(22, 2),
    Detail_Developer(33, 3),
    Detail_Developer(33, 4),
    Detail_Developer(33, 5),
    Detail_Developer(11, 6)
]


def main():
    one_to_many = [(b.name, b.weight, a.name)
                   for a in Developer
                   for b in Detail
                   if b.dev_id == a.id]

    many_to_many_temp = [(c.name, d.id_of_developer, d.id_of_detail)
                         for c in Developer
                         for d in Detail_Developer
                         if c.id == d.id_of_developer]

    many_to_many = [(b.name, b.weight, name_of_developer)
                    for name_of_developer, id_of_developer, id_of_detail in many_to_many_temp
                    for b in Detail if b.id == id_of_detail]

    print('Задание В1')

    first_res = {}
    for l in Detail:
        if 'А' == l.name[0]:
            detail = list((filter(lambda i: i[0] == l.name, one_to_many)))
            l_dev_names = [f[2] for f in detail]
            first_res[l.name] = l_dev_names

    print(first_res)

    print('\nЗадание B2')

    second_res_unsort = []
    for d in Developer:

        detail = list(filter(lambda i: i[2] == d.name, one_to_many))

        if len(detail) > 0:
            second_res_unsort.append((d.name, min([a[1] for a in detail])))
    second_res = sorted(second_res_unsort, key=itemgetter(1))
    for row in second_res:
        print(row)

    print('\nЗадание B3')

    third_res = sorted(many_to_many, key=itemgetter(0))
    for row in third_res:
        print(row)

if __name__ == '__main__':
    main()
