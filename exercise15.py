"""Determinar si un número entero proporcionado por el usuario es primo. Un número
   primo es un entero que no tiene más divisores que él mismo y la unidad."""

from validation_num import Validation
from random import randint

class Example:
    """Sentinel controller"""
    def __init__(self):
        self.prime = True
        self.divider = 2
        self.number = int
        self.answer = int
    
    def read_value(self):
        num = vali.validated_int('Ingrese un número: ')
        while_loop.read_default(num)

    def read_default(self, num):
        """Assign presets to make it automatic."""
        if num == '':
            print('-Algoritmo Automático-')
            self.number = randint(0, 101)
            print('Valor del número:', self.number)
        else: self.number = num

    def calculate(self):
        while self.divider < self.number and self.prime is True:
            self.answer = self.number % self.divider
            if self.answer == 0:
                self.prime = False
            self.divider += 1

    def show(self):
        if self.prime: print('El número', self.number, 'es primo.')
        else: print('El número', self.number, 'no es primo.')


if __name__ == '__main__':
    while_loop = Example()
    vali = Validation()

    while_loop.read_value()
    while_loop.calculate()
    while_loop.show()
