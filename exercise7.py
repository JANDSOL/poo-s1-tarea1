"""Determinar la cantidad de dinero que recibirá un trabajador por concepto de las
   horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo
   exceden de 40, el resto se consideran horas extras y que éstas se pagan al doble
   de una hora normal cuando no exceden de 8; si las horas extras exceden de 8 se pagan
   las primeras 8 al doble de lo que se paga por una hora normal y el resto al triple."""

from validation_num import Validation

class Example:
    """Overtime worked."""
    def __init__(self):
        self.worker_pay = float
        self.hours_worked = float
        self.hourly_pay = float
        self.extra_hours = float
        self.worker_extra_hours = float
        self.paid_for_overtime = float
        self.EXCEED40 = 40
        self.EXCEED8 = 8
        self.EXC8_DOBLE = 2
        self.EXC8_TRIPLE = 3

    def read_salary(self):
        """Read the salary and hourly pay."""
        hours_work = \
            vali.validated_float('Ingrese las horas trabajadas: ')
        hour_pay = \
            vali.validated_float('Ingrese el pago por hora: ')

        worker_salary.read_default(hours_work, hour_pay)
    
    def read_default(self, hours_work, hour_pay):
        """Assign presets to make it automatic."""
        if hours_work == '' or hour_pay == '': print('-Algoritmo automático-')
        if hours_work == '':
            self.hours_worked = 56
            print('Horas trabajadas:', self.hours_worked)
        else: self.hours_worked = hours_work
        if hour_pay == '': 
            self.hourly_pay = 2
            print('Pago por hora: $' + str(self.hourly_pay))
        else: self.hourly_pay = hour_pay

    def algorithm_for_determining_overtime(self):
        """Algorithm in charge of carrying the conditions and calculations."""
        if self.hours_worked > self.EXCEED40:
            self.extra_hours = self.hours_worked - self.EXCEED40

            if self.extra_hours > self.EXCEED8:
                self.worker_extra_hours = self.extra_hours - self.EXCEED8
                self.paid_for_overtime = \
                    self.hourly_pay * self.EXC8_DOBLE * self.EXCEED8 + self.hourly_pay\
                    * self.EXC8_TRIPLE * self.worker_extra_hours
            else:
                self.paid_for_overtime = \
                    self.hourly_pay * self.EXC8_DOBLE * self.extra_hours

            self.worker_pay = self.hourly_pay * self.EXCEED40 + self.paid_for_overtime
        
        else:
            self.worker_pay = self.hourly_pay * self.hours_worked

    def show(self):
        """Show new salary."""
        if self.hours_worked <= 40:
            print('No hay horas extras trabajadas\nSu pago es de: $'\
                                             + str(self.worker_pay))
        else:
            print('Horas extras trabajadas\nSu pago es de :$' + str(self.worker_pay))


if __name__ == '__main__':
    worker_salary = Example()
    vali = Validation()

    worker_salary.read_salary()
    worker_salary.algorithm_for_determining_overtime()
    worker_salary.show()
