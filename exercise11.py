"""Calcular la suma de los cuadrados de los primeros
   100 enteros y escribir el resultado."""

class Example:
    """Sum of numbers squared."""
    def __init__(self):
        self.sum = 0
    
    def calculate(self):
        for number in range(1, 101):
            self.sum += number * number

    def show(self):
        print('La suma del cuadrado de los 100 primeros números es:', self.sum)


if __name__ == '__main__':
    squared_numbers = Example()

    squared_numbers.calculate()
    squared_numbers.show()
