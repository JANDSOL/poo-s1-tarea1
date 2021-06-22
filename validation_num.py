class Validation:
    """Valid data entry by user."""
    def __init__(self):
        self.message = str

    def validated_float(self, message):
        self.message = message
        while True:
            try:
                validated_value = input(self.message).replace(' ', '')
                if validated_value == '':
                    return ''
                else:
                    validated_value = float(validated_value)
                    validated_value = round(validated_value, 2)
                    break
            except ValueError:
                print(' ingrese un dato correcto...\n')
        return validated_value
    
    def validated_int(self, message):
        self.message = message
        while True:
            try:
                validated_value = input(self.message).replace(' ', '')
                if validated_value == '':
                    return ''
                if '.' in validated_value:
                    validated_value = float(validated_value)
                validated_value = int(validated_value)
                break
            except ValueError:
                print(' ingrese un dato correcto...\n')
        return validated_value
