from pizza import Pizza
from Slice import Slice

lista = ['lolo', 'gibon']

kokos = []

p_1 = Pizza(lista, 30)
p_2 = Pizza(kokos, 60)

print(p_1)
print(p_2)

p_1.diameter = 35
p_1.add_toppings('szyneczka')
print(p_1)
p_3 = p_1 + p_2
print(p_3)

s_1 = Slice(lista, 10, 8)
print(s_1)
print(s_1.part_price(5))
