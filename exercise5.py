"""Dado como dato la calificación de un alumno en un examen, escriba “aprobado”
   si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario."""

from validation_num import Validation

class Example:
    """Pass or fail a test."""
    def __init__(self):
        self.grade = float

    def read_grade(self, grade='auto'):
        """Read the student's grade."""
        if grade == 'auto':
            self.grade = 10
            print('-Algoritmo automático-')
        else: self.grade = grade

    def show_grade(self):
        """Show information."""
        print('Calificación:', self.grade)
        if self.grade >= 7: print('Usted ha aprobado.')
        else: print('Usted ha reprobado.')


if __name__ == '__main__':
    student_grade = Example()
    vali_value = Validation()  # Object to validate value.

    grade = vali_value.validated_float('Ingrese una calificación: ')
    if grade == '':
        student_grade.read_grade()
    else:
        student_grade.read_grade(grade)

    student_grade.show_grade()
