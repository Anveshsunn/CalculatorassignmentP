# tests/test_calculator.py

import pytest
from src.calculator import Calculator
from src.history_manager import HistoryManager  # Import HistoryManager

# Test for add method
def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

# Test for subtract method
def test_subtract():
    calc = Calculator()
    result = calc.subtract(5, 3)
    assert result == 2

# Test for multiply method
def test_multiply():
    calc = Calculator()
    result = calc.multiply(3, 4)
    assert result == 12

# Test for divide method
def test_divide():
    calc = Calculator()
    result = calc.divide(10, 2)
    assert result == 5

# Test for division by zero
def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

# Test for power method
def test_power():
    calc = Calculator()
    result = calc.power(2, 3)  # 2^3 = 8
    assert result == 8

    result = calc.power(3, 2)  # 3^2 = 9
    assert result == 9

    result = calc.power(5, 0)  # 5^0 = 1
    assert result == 1

# Test for root method
def test_root():
    calc = Calculator()
    result = calc.root(16, 2)  # sqrt(16) = 4
    assert result == 4

    result = calc.root(81, 3)  # cube root of 81 ≈ 4.326
    assert result == pytest.approx(4.326, rel=1e-2)  # Approximate result for floating-point

    # Testing invalid input for root operation (negative number)
    with pytest.raises(ValueError):
        calc.root(-16, 2)

# Additional test for other edge cases or possible operations

# Test for max input value (edge case for large numbers)
def test_max_input_value():
    calc = Calculator()
    large_number = 1e100  # A very large number
    result = calc.add(large_number, large_number)
    assert result == 2 * large_number

# Test for precision handling
def test_precision():
    calc = Calculator(precision=5)  # Set precision to 5 decimal places
    result = calc.add(1.123456789, 2.987654321)
    assert result == 4.11111  # The result should be rounded to 5 decimal places

# Test for clear history (if implemented in history_manager)
def test_clear_history():
    history_manager = HistoryManager()  # Create an instance of HistoryManager
    history_manager.add_to_history('add 1 and 2', 3)
    history_manager.add_to_history('subtract 5 and 3', 2)
    history_manager.clear_history()

    assert len(history_manager.history) == 0  # History should be empty now
