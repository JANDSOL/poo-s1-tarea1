"""Un ejemplo en el cual usamos el operador lógico AND sería: una escuela aplica dos
   exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones
   denotadas como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en
   ambos exámenes es aceptado; en caso contrario es rechazado.
   ··················································································
   Un ejemplo usando el operador lógico OR sería: una escuela aplica dos exámenes a 
   sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas
   como C1 y C2. El aspirante que obtenga una calificación mayor que 90 en cualquiera
   de los exámenes es aceptado; en caso contrario es rechazado.
   """

from validation_num import Validation
from random import uniform

class Example:
    """Switch and/or."""
    def __init__(self):
        self.note1 = float
        self.note2 = float
        self.status = str
        
    def read_values(self, operation):
        n1 = vali.validated_float('Ingrese su primer nota: ')
        n2 = vali.validated_float('Ingrese su segunda nota: ')
        if operation == 'and': test_and.read_default(n1, n2)
        else: test_or.read_default(n1, n2)

    def read_default(self, n1, n2):
        """Assign presets to make it automatic."""
        if n1 == '' or n2 == '':
            print('-Algoritmo Automático-')
        
        if n1 == '':
            self.note1 = round(uniform(70.0, 100.0), 1)
            print('Primera nota:', self.note1)
        else: self.note1 = n1
        if n2 == '':
            self.note2 = round(uniform(70.0, 100.0), 1)
            print('Segunda nota:', self.note2)
        else: self.note2 = n2

    def calculate(self, operation):
        """Flows and/or."""
        if operation == 'and':
            if self.note1 >= 80.0 and self.note2 >= 80.0: return 'ACEPTADO'
            else: return 'RECHAZADO'
        else:
            if self.note1 >= 90.0 or self.note2 >= 90.0: return 'ACEPTADO'
            else: return 'RECHAZADO'

    def show(self, operation):
        if operation == 'and': self.status = test_and.calculate('and')
        else: self.status = test_or.calculate('or')

        if self.status == 'ACEPTADO': print('Felicidades ha sido aceptado.')
        else: print('Lo sentimos no ha sido aceptado.')


if __name__ == '__main__':
    test_and = Example()
    test_or = Example()
    vali = Validation()

    # Exercise applying AND
    print('*AND*')
    test_and.read_values('and')
    test_and.show('and')

    # Exercise applying OR
    print('\n*OR*')
    test_or.read_values('or')
    test_or.show('or')
