"""Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento
 del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento."""

from validation_num import Validation

class Example:
    """New increase."""
    def __init__(self):
        self.starting_salary = float
        self.new_salary = float
        self.INCREASE = 0.1

    def read_salary(self, sal='auto'):
        """Read the employee's salary."""
        if sal == 'auto':
            print('-Algoritmo automático-')
            self.starting_salary = 600.0
        else: self.starting_salary = sal

    def calculate_new_salary(self):
        if self.starting_salary <= 600:
            self.new_salary = self.starting_salary + self.starting_salary\
                                                          * self.INCREASE
        else: self.new_salary = self.starting_salary

    def show(self):
        """Show salary."""
        print('Salario viejo:', self.starting_salary, end='; ')
        print('Salario nuevo:', self.new_salary)
        if self.starting_salary == self.new_salary: print('Salario sin aumento.')
        else: print('Su nuevo salario es:', self.new_salary)


if __name__ == '__main__':
    employee_salary = Example()
    vali_value = Validation()  # Object to validate value.

    sal = vali_value.validated_float('Ingrese su salario: ')
    if sal == '': employee_salary.read_salary()
    else: employee_salary.read_salary(sal)
    employee_salary.calculate_new_salary()
    employee_salary.show()
