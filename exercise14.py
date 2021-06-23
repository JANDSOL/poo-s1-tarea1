"""Diseñe un pseudocódigo para calcular la suma y producto de N números
   enteros, utilizando un bucle controlado por centinela."""

from validation_num import Validation
from random import randint

class Example:
    """Sentinel controller"""
    def __init__(self):
        self.sum = 0
        self.product = 1
        self.number = int
    
    def read_value(self):
        num = vali.validated_int('Ingrese un número: ')
        while_loop.read_default(num)

    def read_default(self, num):
        """Assign presets to make it automatic."""
        if num == '':
            print('-Algoritmo Automático-')
            self.number = randint(-1, 101)
            print('Valor del número:', self.number)
        else: self.number = num

    def calculate(self):
        while self.number != -1:
            self.sum += self.number
            self.product *= self.number
            print('')
            while_loop.read_value()

    def show(self):
        print('Total de la suma es:', self.sum)
        print('Total de producto es:', self.product)


if __name__ == '__main__':
    while_loop = Example()
    vali = Validation()

    while_loop.read_value()
    while_loop.calculate()
    while_loop.show()
