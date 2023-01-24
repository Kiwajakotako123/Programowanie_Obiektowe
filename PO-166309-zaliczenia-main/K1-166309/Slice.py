from pizza import *
import sys
from typing import List


class Slice(Pizza):
    __how_many_slices: int

    def __init__(self, toppings: List[str], diameter: float, how_many_slices: int) -> None:
        super().__init__(toppings, diameter)
        if 4 < how_many_slices < 12:
            self.__how_many_slices = how_many_slices
        else:
            print("bledna ilosc kawalkow")
            sys.exit(-10)

    @property
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    @how_many_slices.getter
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, how_many_slices):
        if 4 < how_many_slices < 12:
            self.__how_many_slices = how_many_slices
        else:
            print("bledna ilosc kawalkow")
            sys.exit(-10)

    def part_price(self, ordered_slices):
        if 0 < ordered_slices < self.__how_many_slices:
            ilosc = ordered_slices / self.__how_many_slices
            return round(self.price * ilosc, 2)
        else:
            print("Zamawiasz zla ilosc kawalkow")
            sys.exit(-10)

    def __str__(self) -> str:
        if len(self.toppings) == 0:
            return super().__str__() + f'kawalki: {self.how_many_slices}\n' \
                                       f'Cena za kawalek: {self.price / self.__how_many_slices}'

        else:
            return super().__str__() + f'kawalki: {self.how_many_slices}\n' \
                                       f'Cena za kawalek: {self.price / self.__how_many_slices}'
