#zad3
lista = [10, -3, 6, -9, -54]
def ile_ujemnych(zad):
    ujemne = 0
    for num in zad:
        if num < 0:
            ujemne += 1

    print(ujemne)

ile_ujemnych(lista)