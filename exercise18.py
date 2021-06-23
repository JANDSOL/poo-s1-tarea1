"""Aplicar las fases para la resolución de un problema para leer un vector de 20
   números enteros y a continuación escribir en un vector A todos los números negativos
   y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores."""

class Example:
    """Array."""
    def __init__(self):
        self.arrayA = []
        self.arrayB = []

    def calculate(self):
        numbers = []
        turns = 0
        for i in range(-10, 11):
            numbers.append(i)
            if numbers[turns] > 0:
                self.arrayA.append(numbers[turns])
            else:
                self.arrayB.append(numbers[turns])
            turns += 1

    def show(self):
        print('Array A: ', end='')
        for value in self.arrayA:
            print(value, end=', ')
        print('\nArray B: ', end='')
        for value in self.arrayB:
            print(value, end=', ')

if __name__ == '__main__':
    array = Example()

    array.calculate()
    array.show()
