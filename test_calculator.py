import pytest

from calculator import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1, 2) == 3

def test_subtraction():
    assert subtraction(5, 2) == 3

def test_multiplication():
    assert multiplication(3, 4) == 12

def test_division():
    assert division(10, 2) == 5
    assert division(10, 0) == "Error! Division by zero."
