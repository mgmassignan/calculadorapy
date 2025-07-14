class Calculator:
    def __init__(self):
        self.current_value = 0
        self.operation = None
        self.new_input_required = True

    def set_current_value(self, value):
        self.current_value = value

    def set_operation(self, op):
        self.operation = op

    def calculate(self, new_value):
        if self.operation == '+':
            result = self.current_value + new_value
        elif self.operation == '-':
            result = self.current_value - new_value
        elif self.operation == '*':
            result = self.current_value * new_value
        elif self.operation == '/':
            if new_value == 0:
                return "Erro"
            result = self.current_value / new_value
        else:
            result = new_value
        
        self.current_value = result
        self.operation = None
        return result

    def clear(self):
        self.current_value = 0
        self.operation = None
        self.new_input_required = True


