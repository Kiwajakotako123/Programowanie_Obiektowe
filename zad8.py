# zad 8

def zadanie8():
    lista = [x for x in range(2, 10000 + 1)]
    iterator = 0
    for i in lista:
        for base in range(2, 100 + 1):
            if i != base and i % base == 0:
                del lista[iterator]
                continue
        iterator += 1

    for x in lista:
        print(x)


