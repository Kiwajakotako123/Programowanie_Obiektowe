# zad 9



def zad9a(listttt):
    temp = listttt[-1]
    listttt[-1] = listttt[0]
    listttt[0] = temp


def zad9b(listtttt):
    ostatniaLiczba = listtttt[-1]
    iterator = len(listtttt) - 1
    while iterator > 0:
        listtttt[iterator] = listtttt[iterator - 1]
        iterator -= 1
    listtttt[0] = ostatniaLiczba


def zad9c(listttt):
    for i in range(0, len(listttt)):
        if listttt[i] % 2 == 0:
            listttt[i] = 0


def zad9e(listttt):
    dlugosc = len(listttt)
    if dlugosc % 2 == 1:
        del listttt[int((dlugosc - 1) / 2)]
    else:
        print(dlugosc)
        del listttt[int(dlugosc / 2)]
        del listttt[int((dlugosc / 2)) - 1]


def wiekszy(i, j):
    if i > j:
        return i
    return j


def zad9d(listttt):
    for x in range(1, len(listttt) - 1):
        listttt[x] = wiekszy(listttt[x - 1], listttt[x + 1])


def swap(listttt, i, j):
    temp = listttt[i]
    listttt[i] = listttt[j]
    listttt[j] = temp


def sortDown(listttt, downIndex, upIndex):
    x = upIndex
    while x > downIndex:
        swap(listttt, x, x - 1)
        x -= 1


def zad9f(listttt):
    aktualnyPierwszyElement = 0
    for i in range(0, len(listttt)):
        if listttt[i] % 2 == 0:
            sortDown(listttt, aktualnyPierwszyElement, i)
            aktualnyPierwszyElement += 1



def zad9g(listttt):
    najwiekszaWartosc = float('-inf')
    najwiekszyIndex = -1
    najwiekszyIndexDrugi = -1

    for x in range(0, len(listttt)):
        if listttt[x] > najwiekszaWartosc:
            najwiekszaWartosc = listttt[x]
            najwiekszyIndex = x

    najwiekszaWartosc = float('-inf')

    for x in range(0, len(listttt)):
        if listttt[x] > najwiekszaWartosc and x != najwiekszyIndex:
            najwiekszaWartosc = listttt[x]
            najwiekszyIndexDrugi = x

    return najwiekszyIndexDrugi


def zad9h(listttt):
    for x in range(0, len(listttt) - 1):
        if listttt[x] >= listttt[x + 1]:
            return False
    return True


def zad9i(listttt):
    for x in range(0, len(listttt) - 1):
        if listttt[x] == listttt[x + 1]:
            return True
    return False



def zad9j(listttt):
    for i in range(0, len(listttt) - 1):
        for j in range(0, len(listttt) - 1):
            if i == j:
                continue
            if listttt[i] == listttt[j]:
                return True
    return False


lista = [x ** 2 % 25 for x in range(1, 10)]
lista2 = [x ** 2 % 24 for x in range(1, 10)]
# for x in lista:
#     print(x)
# print("-------------------------------------")
# print(zad9g(lista))
# for x in lista:
#     print(x)



def mujEquals(lista1, lista2):
    iterator = 0
    length = len(lista1)

    if len(lista2) != length:
        return False

    while iterator < length:
        if lista1[iterator] != lista2[iterator]:
            return False
        iterator += 1

    return True

print(mujEquals(lista, lista2))