"""Diseñe un pseudocódigo para calcular la suma y producto de N números
   enteros, utilizando un bucle controlado por el usuario."""

from validation_num import Validation
from random import randint

class Example:
    """User controller"""
    def __init__(self):
        self.sum = 0
        self.product = 1
        self.number = int
        self.answer = str
    
    def read_value(self):
        if self.number == int:
            return input('Ingrese un caracter: ').upper().replace(' ', '')
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
        self.answer = while_loop.read_value()
        while self.answer != 'N' and self.answer != 'n':
            self.number = 0
            while_loop.read_value()
            self.sum += self.number
            self.product *= self.number
            self.number = int
            print('¿Desea continuar (S/N)?\n')
            self.answer = while_loop.read_value()
            if self.answer == 'N': break

    def show(self):
        print('Total de la suma es:', self.sum)
        print('Total de producto es:', self.product)


if __name__ == '__main__':
    while_loop = Example()
    vali = Validation()

    while_loop.calculate()
    while_loop.show()
