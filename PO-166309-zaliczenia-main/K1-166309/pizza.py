import math
import sys
from typing import List


class Pizza:
    __price: float
    __toppings: List[str]
    __diameter: float

    def __init__(self, toppings: List[str], diameter: float) -> None:
        self.__toppings = toppings

        if diameter < 20:
            print("bledny promien")
            sys.exit(-10)
        else:
            self.__diameter = diameter
        self.__price = round(0.05 * self.area(self) + len(self.__toppings) * 2, 2)

    @staticmethod
    def area(cls: 'Pizza') -> float:
        area = math.pi * (cls.__diameter / 2) ** 2
        return area

    @property
    def diameter(self) -> float:
        return self.__diameter

    @diameter.getter
    def diameter(self) -> float:
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 20:
            print("Bledna srednica")
            sys.exit(-10)
        else:
            self.__diameter = diameter

    @property
    def price(self) -> float:
        return self.__price

    @property
    def toppings(self) -> List[str]:
        return self.__toppings

    def add_toppings(self, topping: str):
        self.__toppings.append(topping)
        self.__price += 2.0

    def __str__(self) -> str:
        if len(self.__toppings) == 0:
            return f'Pizza: \n' \
                   f'srednica: {self.__diameter}\n' \
                   f'cena: {self.__price}\n'
        else:
            return f'Pizza: \n' \
                   f'srednica: {self.__diameter}\n' \
                   f'dodatki: {self.__toppings}\n' \
                   f'cena: {self.__price}\n'

    def __add__(self, other: 'Pizza') -> 'Pizza':
        srednica = other.diameter
        if self.diameter > other.diameter:
            srednica = other.diameter
        list3 = []
        list3.extend(self.__toppings)
        list3.extend(other.__toppings)
        return Pizza(list3, srednica)
