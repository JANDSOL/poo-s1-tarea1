"""Un vendedor recibe un sueldo base más un 10% extra por comisión de sus
   ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de
   comisiones por las tres ventas que realiza en el mes y el total que
   recibirá en el mes tomando en cuenta su sueldo base y sus comisiones."""

class Example:
    """."""
    def __init__(self):
        self.base_salary = float
        self.extra_commis = 0.1
        self.sale1 = float
        self.sale2 = float
        self.sale3 = float
        self.total_receive = float

    def read_salary_v1_2_3(self, sal=1500, v1=100, v2=150, v3=250):
        """Read input by user."""
        self.base_salary = sal
        self.sale1 = v1
        self.sale2 = v2
        self.sale3 = v3

    def calculate(self):
        """Calculate ."""
        pass

    def show(self):
        """Show ."""
        print('El valor total a pagar es: $' + str(self.purchase))


if __name__ == '__main__':
    discount_purchases = Example()
    total_purch = float(input('Ingrese el total de compras: $')\
                                             .replace(' ', ''))
    discount_purchases.read()
    discount_purchases.calculate()
    discount_purchases.show()
