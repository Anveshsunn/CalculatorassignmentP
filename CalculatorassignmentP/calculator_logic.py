from cal_operations import Operations
from history_manager import HistoryManager

class Calculator:
    """Main class for handling the calculator logic (addition, subtraction, etc.)"""
    
    def __init__(self, config):
        self.config = config
        self.history_manager = HistoryManager(config)

    def _validate_input(self, value):
        """Ensure the input value does not exceed the max allowable value."""
        if value > self.config.max_input_value:
            raise ValueError(f"Input exceeds maximum allowed value: {self.config.max_input_value}")
        return value

    def add(self, x, y):
        """Perform addition and log the result."""
        x, y = self._validate_input(x), self._validate_input(y)
        result = Operations.add(x, y, self.config.result_precision)
        self.history_manager._log_history(f"add({x}, {y}) = {result}")
        return result

    def subtract(self, x, y):
        """Perform subtraction and log the result."""
        x, y = self._validate_input(x), self._validate_input(y)
        result = Operations.subtract(x, y, self.config.result_precision)
        self.history_manager._log_history(f"subtract({x}, {y}) = {result}")
        return result

    def multiply(self, x, y):
        """Perform multiplication and log the result."""
        x, y = self._validate_input(x), self._validate_input(y)
        result = Operations.multiply(x, y, self.config.result_precision)
        self.history_manager._log_history(f"multiply({x}, {y}) = {result}")
        return result

    def divide(self, x, y):
        """Perform division and log the result."""
        x, y = self._validate_input(x), self._validate_input(y)
        result = Operations.divide(x, y, self.config.result_precision)
        self.history_manager._log_history(f"divide({x}, {y}) = {result}")
        return result

    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        base, exponent = self._validate_input(base), self._validate_input(exponent)
        result = Operations.power(base, exponent, self.config.result_precision)
        self.history_manager._log_history(f"power({base}, {exponent}) = {result}")
        return result

    def sqrt(self, x):
        """Calculate square root."""
        x = self._validate_input(x)
        result = Operations.sqrt(x, self.config.result_precision)
        self.history_manager._log_history(f"sqrt({x}) = {result}")
        return result

    def save_history(self):
        """Save the current history to file."""
        self.history_manager.save_history()

    def load_history(self):
        """Load history from file."""
        self.history_manager.load_history()

    def get_history(self):
        """Return the history of calculations."""
        return self.history_manager.get_history()

    def clear_history(self):
        """Clear the history."""
        self.history_manager.clear_history()

    def undo(self):
        """Undo the last operation."""
        return self.history_manager.undo()

    def redo(self):
        """Redo the previously undone operation."""
        return self.history_manager.redo()
