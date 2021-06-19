class Validation:
    """Valid data entry by user."""
    def __init__(self):
        self.message = str

    def validated_float(self, message):
        while True:
            try:
                validated_value = input(message).replace(' ', '')
                if validated_value == '':
                    return ''
                else:
                    validated_value = float(validated_value)
                    break
            except ValueError:
                print(' ingrese un dato correcto...\n')
        return validated_value
