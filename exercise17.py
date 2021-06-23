"""Calcular el factorial de N números enteros leídos de teclado. El problema
   consistirá en realizar una estructura de N iteraciones aplicando el
   factorial de un número."""

from validation_num import Validation
from random import randint

class Example:
    """Factorial of numbers."""
    def __init__(self):
        self.turns = int
        self.number = int
        self.factorial = int
    
    def read_value(self, operation='noTurns'):
        if operation == 'turns':
            num = vali.validated_int('Ingrese el número de vueltas: ')
            factorial_number.read_default(num, 'turns')

        else:
            num = vali.validated_int('Ingrese un número: ')
            factorial_number.read_default(num)

    def read_default(self, num, operation='noTurns'):
        """Assign presets to make it automatic."""
        if num == '' and operation == 'turns':
            print('-Algoritmo Automático-')
            if operation == 'turns':
                self.turns = randint(0, 100)
                print('Valor del número:', self.turns)
        else: self.turns = num

        if num == '' and operation == 'noTurns':
            print('-Algoritmo Automático-')
            if operation == 'noTurns':
                self.number = randint(0, 100)
                print('Valor del número:', self.number)
        else: self.number = num

    def calculate(self):
        for _ in range(1, self.turns+1):
            factorial_number.read_value()
            self.factorial = 1

            for i in range(1, self.number+1):
                self.factorial *= i
            factorial_number.show()

    def show(self):
        print('El factorial del número', self.number, 'es', self.factorial, '\n')


if __name__ == '__main__':
    factorial_number = Example()
    vali = Validation()

    factorial_number.read_value('turns')
    factorial_number.calculate()
