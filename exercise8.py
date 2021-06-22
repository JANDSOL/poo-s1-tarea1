"""Leer tres números enteros diferentes entre sí
   y determinar el número mayor de los tres."""

from validation_num import Validation
from random import randint  # Random Numbers Integer

class Example:
    """Greater than 3 numbers."""
    def __init__(self):
        self.number1 = int
        self.number2 = int
        self.number3 = int
        self.bigger_num = int

    def read(self):
        """Read three numbers."""
        n1 = vali.validated_int('Ingrese el 1er número: ')
        n2 = vali.validated_int('Ingrese el 2do número: ')
        n3 = vali.validated_int('Ingrese el 3er número: ')
        bigger_number.read_default(n1, n2, n3)

    def read_default(self, n1, n2, n3):
        """Assign presets to make it automatic."""
        if n1 == '' or n2 == '' or n3 == '': print('-Algoritmo Automático-')
        if n1 == '':
            self.number1 = randint(0, 50)
            print('Valor 1:', self.number1)
        else: self.number1 = n1
        if n2 == '':
            self.number2 = randint(0, 50)
            print('Valor 2:', self.number2)
        else: self.number2 = n2
        if n3 == '':
            self.number3 = randint(0, 50)
            print('Valor 3:', self.number3)
        else: self.number3 = n3

    def calculate_major(self):
        """Calculate the bigger number."""
        if self.number1 > self.number2 and self.number1 > self.number3:
            self.bigger_num = self.number1
        elif self.number2 > self.number3:
            self.bigger_num = self.number2
        else:
            self.bigger_num = self.number3

    def show(self):
        print('El número mayor es:', self.bigger_num)


if __name__ == '__main__':
    bigger_number = Example()
    vali = Validation()

    bigger_number.read()
    bigger_number.calculate_major()
    bigger_number.show()
