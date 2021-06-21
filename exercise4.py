"""Construir un algoritmo tal, que dado como dato la calificación de un alumno
   en un examen, presente un alumno aprueba si la calificación es mayor o
   igual que 7."""

from validation_num import Validation

class Example:
    """A student passes or fails."""
    def __init__(self):
        self.grade = float

    def read_grade(self, grade=7.5):
        """Read the student's grade."""
        self.grade = grade
        if grade == 7.5: print('-Algoritmo automático-')

    def show_grade(self):
        """Show information."""
        print('Calificación:', self.grade)
        if self.grade >= 7: print('Usted ha aprobado.')


if __name__ == '__main__':
    student_grade = Example()
    vali_value = Validation()  # Object to validate value.
    
    while True:
        grade = vali_value.validated_float('Ingrese una calificación: ')
        if grade == '':
            student_grade.read_grade()
        elif grade >= 7:
            grade = round(grade, 2)
            student_grade.read_grade(grade)
            break
        else:
            print(' ingresa otra nota...\n')

    student_grade.show_grade()
