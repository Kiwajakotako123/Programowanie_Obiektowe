#zad2.1
def mult(a):
    wynik=1
    for x in range(0,len(a)):
        wynik*=a[x]
    return wynik
print(mult([3, 5, 7]))

#zad2.2

def mult_ints(a):
    wynik = 1
    for x in range(0, len(a)):
        if type(a[x]) == int:
            wynik *= a[x]
    return wynik
print(mult_ints([3, 3.14, 5, "abc", 7]))
#zad2.3
def multiply(*args):
    wynik=1
    for x in args:
        wynik*=x
    return wynik
print(multiply(3, 5, 7))

#zad2.4

def multiply_ints(*args):
    wynik = 1
    for x in args:
        if type(x) == int:
            wynik *= x
    return wynik
print(multiply_ints(3, 3.14, 5, "abc", 7))

#zad2.5

def make_car(firma, model, **kwargs):
    slownik = kwargs
    slownik["firma"] = firma
    slownik["model"] = model
    return slownik
print(make_car("Kia", "Picanto", kolor = "Kawowy", poj_silnika = 900,))

#zad3.1

def zad31():
    lista = []
    lista.append([x for x in range(1, 11)])
    lista.append([x ** 2 for x in range(1, 11)])
    lista.append([x ** 3 for x in range(1, 11)])
    for i in lista:
        for j in i:
            print(j)
print(zad31())

#zad3.2

def zad32():
    lista = []
    dlugoscListy = 1
    aktualnaLiczba = 1
    for i in range(0, 10):
        lista.append([])
        for j in range(dlugoscListy):
            lista[i].append(aktualnaLiczba)
            aktualnaLiczba += 1
        dlugoscListy += 1

    totalSum = 0
    iterator = 0
    for i in lista:
        arraySum = 0
        for j in i:
            arraySum += j
        totalSum += arraySum
        print(f'Array[{iterator}] sum == {arraySum}')
        iterator += 1
    print(f'Total sum == {totalSum}')

print(zad32())


