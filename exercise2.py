"""En una tienda se ofrece un descuento del 15% sobre el total de la compra
   y un cliente desea saber cuánto deberá pagar finalmente por su compra."""

class Example:
    """Discount for purchases."""
    def __init__(self):
        self.DISCOUNT = 0.15
        self.discount_purch = float
        self.tot_purch = float
        self.purchase = float

    def read_total_purchase(self, total_purch=100):
        """Read input by user."""
        self.tot_purch = total_purch
        if total_purch == 100:
            print('\n-Prueba automática del algoritmo-')
            print('Total de compras: $100')

    def calculation_discount(self):
        """Calculate discount."""
        self.discount_purch = round((self.tot_purch * self.DISCOUNT), 2)
        self.purchase = round((self.tot_purch - self.discount_purch), 2)

    def show(self):
        """Show total purchase value."""
        print('El valor total a pagar es: $' + str(self.purchase))


def validated_value():
    """Valid data entry by user."""
    while True:
        try:
            total_purch = input('Ingrese el total de compras: $')\
                                                .replace(' ', '')
            if total_purch == '':
                return ''
            else:
                total_purch = float(total_purch)
                break
        except ValueError:
            print(' ingrese un valor correcto\n')
    return total_purch


if __name__ == '__main__':
    discount_purchases = Example()
    value = validated_value()
    if value == '': discount_purchases.read_total_purchase()
    else: discount_purchases.read_total_purchase(value)
    discount_purchases.calculation_discount()
    discount_purchases.show()
