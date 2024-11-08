# src/calculator.py

class Calculator:
    def __init__(self, precision=10, max_input_value=1e100):
        self.precision = precision
        self.max_input_value = max_input_value

    def add(self, a, b):
        self._validate_inputs(a, b)
        return round(a + b, self.precision)

    def subtract(self, a, b):
        self._validate_inputs(a, b)
        return round(a - b, self.precision)

    def multiply(self, a, b):
        self._validate_inputs(a, b)
        return round(a * b, self.precision)

    def divide(self, a, b):
        self._validate_inputs(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return round(a / b, self.precision)

    def power(self, base, exponent):
        self._validate_inputs(base, exponent)
        return round(base ** exponent, self.precision)

    def root(self, value, n):
        self._validate_inputs(value, n)
        if value < 0:
            raise ValueError("Cannot take the root of a negative number.")
        return round(value ** (1/n), self.precision)

    def _validate_inputs(self, *values):
        for val in values:
            if abs(val) > self.max_input_value:
                raise ValueError(f"Value {val} exceeds maximum allowed input.")
