"""Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga
   el resultado de la siguiente función:
                   .--
                   |  100 * V          si num == 1
                  <   100 ^ V          si num == 2
                   |  100 / V          si num == 3, para V < > 0
                   |     0             cualquier otro valor de num
                   .--                                                             """


from validation_num import Validation
from random import randint

class Example:
    """Result of a function."""
    def __init__(self):
        self.DEFAULT_VAL = 100
        self.number = 0
        self.value = 0
        self.answer = 0
        
    def read_values(self):
        n1 = vali.validated_int('Ingrese un número: ')
        n2 = vali.validated_int('Ingrese otro número: ')
        function_switch.read_default(n1, n2)

    def read_default(self, n1, n2):
        """Assign presets to make it automatic."""
        if n1 == '' or n2 == '':
            print('-Algoritmo Automático-')

        if n1 == '':
            self.number = randint(0, 10)
            print('Valor 1er número:', self.number)
        else: self.number = n1
        if n2 == '':
            self.value = randint(0, 10)
            print('Valor 2do número:', self.value)
        else: self.value = n2

    def calculate_switch(self):
        """Simulation of a switch."""
        if self.number == 1:
            return int(self.DEFAULT_VAL * self.value)
        if self.number == 2:
            return int(self.DEFAULT_VAL ** self.value)
        if self.number == 3:
            return int(self.DEFAULT_VAL / self.value)
        return 0

    def show(self):
        self.answer = function_switch.calculate_switch()
        print('Resultado:', self.answer)


if __name__ == '__main__':
    function_switch = Example()
    vali = Validation()

    function_switch.read_values()
    function_switch.show()
