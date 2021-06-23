"""Aplicar los pasos de la metodología para la solución de un problema para leer un
   número entero N y calcular el resultado de la siguiente serie:
                          1 – 1/2 + 1/3 – 1/4 + ... +/- 1/N.
   Resolveremos el problema utilizando bucle Repeat
   controlado por contador y usando banderas."""

from validation_num import Validation
from random import uniform as randfloat

class Example:
    """Simulate repeat loop."""
    def __init__(self):
        self.number = int
        self.serie = 0
    
    def read_value(self):
        num = vali.validated_float('Ingrese un número: ')
        repeat_loop.read_default(num)

    def read_default(self, num):
        """Assign presets to make it automatic."""
        if num == '':
            print('-Algoritmo Automático-')
            self.number = round(randfloat(0, 101), 2)
            print('Valor del número:', self.number)
        else: self.number = num

    def calculate(self):
        counter = 1
        flag = True
        while counter < self.number:
            if flag:
                self.serie += (1/counter)
                flag = False
            else:
                self.serie -= (1/counter)
                flag = True
            counter += 1

    def show(self):
        print('Resultado:', round(self.serie, 2))


if __name__ == '__main__':
    repeat_loop = Example()
    vali = Validation()

    repeat_loop.read_value()
    repeat_loop.calculate()
    repeat_loop.show()
