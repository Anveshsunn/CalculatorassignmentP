import math

class Operations:
    """Class containing basic and advanced mathematical operations."""
    
    @staticmethod
    def add(x, y, precision):
        """Perform addition."""
        return round(x + y, precision)

    @staticmethod
    def subtract(x, y, precision):
        """Perform subtraction."""
        return round(x - y, precision)

    @staticmethod
    def multiply(x, y, precision):
        """Perform multiplication."""
        return round(x * y, precision)

    @staticmethod
    def divide(x, y, precision):
        """Perform division."""
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return round(x / y, precision)

    @staticmethod
    def power(base, exponent, precision):
        """Perform exponentiation (base raised to the power of exponent)."""
        return round(math.pow(base, exponent), precision)

    @staticmethod
    def sqrt(x, precision):
        """Calculate square root."""
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return round(math.sqrt(x), precision)
