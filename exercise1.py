"""En ejemplos anteriores, diseñamos un pseudocódigo para encontrar
   la superficie de un círculo para un radio cualquiera. El Flujograma que
   representa a dicho ejemplo es el siguiente:"""

class Example:
    """Surface of a circle."""
    def __init__(self):
        self.PI = 3.1416
        self.surface = int
        self.radio = float
    
    def read_radio(self, rad):
        """Read input by user."""
        self.radio = rad
    
    def calculation_surface(self):
        """Calculation of surface."""
        self.surface = round((self.PI * self.radio**2), 2)

    def show(self):
        """Show result of surface."""
        print('La superficie del círculo es:', self.surface)


if __name__ == '__main__':
    surface_circle = Example()
    rad = float(input('Ingrese el radio de su círculo: ').replace(' ', ''))
    surface_circle.read_radio(rad)
    surface_circle.calculation_surface()
    surface_circle.show()
