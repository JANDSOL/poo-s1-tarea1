""" Elabore pseudocódigo para el caso en que se desean
    escribir los números del 1 al 100."""

class Example:
    """Show numbers."""
    def __init__(self):
        pass

    def show(self):
        i = 0
        while i <= 100:
            print(i, end=', ')
            i += 1


if __name__ == '__main__':
    while_loop = Example()

    while_loop.show()
