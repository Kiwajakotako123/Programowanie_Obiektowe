lista = [1, 4, 16, 9, 9, 7, 4, 9, 11]

def suma(lista):
    sum = 0
    znak = 1
    for x in lista:
        sum += znak*x
        znak = -znak
    print(sum)


suma(lista)