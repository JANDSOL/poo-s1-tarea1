"""Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30
   alumnos. Los datos sobre estos exámenes se proporcionan de la siguiente manera:
                      Cal1,1 Cal1,2 ............ Cal1,6
                      Cal2,1 Cal2,2 ............ Cal2,6
                      .................................
                      Cal30,1 Cal30,2 ........ Cal30,6
   Donde Cali,j es una variable real que expresa la calificación que obtuvo el alumno
   i en el examen j. 
                            1 £ i £ 30, 1£ j £ 6
   Calcular lo siguiente:
   a) El promedio de calificaciones de cada uno de los 6 exámenes.
   b) El promedio de cada alumno.
   c) El tipo (número) de examen que tuvo el mayor promedio de calificación.
      Escriba también dicho promedio."""

from validation_num import Validation
from random import uniform as randfloat

class Example:
    """Students notes."""
    def __init__(self):
        self.notes_list = []
        self.students_list = []
        self.STUDENTS = 30
        self.BOXES_NOTES = 6
        self.average_test = []

    def read_value(self):
        for student in range(1, 31):
            """Lectura de los 30 alumnos."""
            stu_temporary = input('Nombre del alumno {}: '.format(student))
            self.students_list.append(stu_temporary)

            for note in range(1, 7):
                print('Escriba la calificación del alumno "{}" en el exámen "{}"'\
                                             .format(stu_temporary, note))
                """Lectura de las 6 calificaciones de los 30 alumnos."""
                num = vali.validated_float('Nota #{}: '.format(note))
                students.read_default(num)
                if note == 1:
                    self.notes_list.append([self.notes_temporary])
                else:
                    self.notes_list[student-1].append(self.notes_temporary)
            print('')

    def read_default(self, num):
        """Assign presets to make it automatic."""
        if num == '':
            print('-Algoritmo Automático-')
            self.notes_temporary = round(randfloat(0, 10.0), 2)
            print('Valor del número:', self.notes_temporary)
        else: self.notes_temporary = num

    def calculate(self):
            """Calculo promedio de calificaciones de cada uno de los exámenes."""
            for number_test in range(6):
                sum_notes = 0
                for note in self.notes_list:
                    sum_notes += note[number_test]
                average = round((sum_notes/self.STUDENTS), 2)
                print('Promedio de exámen {}: {}'.format(number_test+1, average))

            """Cálculo del promedio de cada alumno."""
            print('')
            for number, student in enumerate(self.students_list):
                sum_notes = sum(self.notes_list[number])
                average = round((sum_notes/self.BOXES_NOTES), 2)
                print('{} su promedio es: {}'.format(student, average))

            """Cálculo del tipo de exámen que tuvo mayor promedio de calificación."""
            self.aver_major = 0
            for number_test in range(6):
                sum_notes = 0
                for note in self.notes_list:
                    sum_notes += note[number_test]
                average = round((sum_notes/self.STUDENTS), 2)
                if self.aver_major < average:
                    self.aver_major = average
                self.average_test.append(average)
            
    def show(self):
        print('')
        print('El exámen', self.average_test.index(self.aver_major)+1,\
              'obtuvo el mayor promedio:', self.aver_major)


if __name__ == '__main__':
    students = Example()
    vali = Validation()

    students.read_value()
    students.calculate()
    students.show()
