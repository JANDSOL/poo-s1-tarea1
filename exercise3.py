"""Un vendedor recibe un sueldo base más un 10% extra por comisión de sus
   ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de
   comisiones por las tres ventas que realiza en el mes y el total que
   recibirá en el mes tomando en cuenta su sueldo base y sus comisiones."""

from validation_num import Validation

class Example:
    """."""
    def __init__(self):
        self.base_salary = float
        self.EXTRA_COMMIS = 0.1
        self.sale1 = float
        self.sale2 = float
        self.sale3 = float
        self.total_receive = float

    def read_salary_v1_2_3(self, sal, s1, s2, s3):
        """Read input by user."""
        if sal == '': self.base_salary = 1500  # Default value if no data.
        else: self.base_salary = sal
        if s1 == '': self.sale1 = 100
        else: self.sale1 = s1
        if s2 == '': self.sale2 = 150
        else: self.sale2 = s2
        if s3 == '': self.sale3 = 250
        else: self.sale3 = s3

        if self.base_salary == 1500 and self.sale1 == 100\
           and self.sale2 == 150 and self.sale3 == 250:
            print('\n-Algoritmo por defecto-')
            print('Salario:${}, venta1:${}, venta2:${}, venta3:${}.'\
              .format(self.base_salary, self.sale1,self.sale2, self.sale3))

    def commission_calculation(self):
        """Commission calculation."""
        total_sales = self.sale1 + self.sale2 + self.sale3
        commission = total_sales * self.EXTRA_COMMIS
        self.total_receive = round((self.base_salary + commission), 2)

    def show(self):
        """Show total to receive."""
        print('El valor total a recibir es: $' + str(self.total_receive))


if __name__ == '__main__':
    commission_money = Example()
    vali_value = Validation()  # Object to validate value.

    base_sal = vali_value.validated_float('Ingrese su salario base: $')
    s1 = vali_value.validated_float('Ingrese su primer venta: $')
    s2 = vali_value.validated_float('Ingrese su segunda venta: $')
    s3 = vali_value.validated_float('Ingrese su tercer venta: $')
    commission_money.read_salary_v1_2_3(base_sal, s1, s2, s3)
    commission_money.commission_calculation()
    commission_money.show()
