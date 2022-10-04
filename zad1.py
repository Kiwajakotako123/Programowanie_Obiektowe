#zad1
#a)
lista = [x for x in range(1,11)]
print(lista)
#b)
lista2 = [x for x in range(0,21,2)]
print(lista2)
#c)
lista3 = [0 for x in range(1,11)]
print(lista3)
#c)
lista4 = [x**2 for x in range(1,11)]
print(lista4)
#d)
lista5 = [x%2 for x in range(10)]
print(lista5)
#e)
lista6 = [x%5 for x in range(10)]
print(lista6)

#zad2
print("---------------------------------")
#a)
lista7 = []
i = 1
while len(lista7) < 10:
    lista7.append(i)
    i = i + 1
print(lista7)
#b)
lista8 = []
i = 0
while len(lista8) < 11:
    lista8.append(i)
    i = i + 2
print(lista8)
#c)
lista9 = []
i = 1
while len(lista9) < 10:
    lista9.append(i**2)
    i = i + 1
print(lista9)
#d)
lista10 = []
i = 1
while len(lista10) < 10:
    lista10.append(0)
    i = i + 1
print(lista10)
#d)
lista11 = []
i = 1
while len(lista11) < 10:
    lista11.append(i%2)
    i = i + 1
print(lista11)
#d)
lista12 = []
i = 1
while len(lista12) < 10:
    lista12.append(i%5)
    i = i + 1
print(lista12)
print("---------------------------------")
