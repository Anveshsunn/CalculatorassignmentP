import pytest
from cal_settings import Config
from calculator_logic import Calculator

@pytest.fixture
def calc():
    config = Config()
    return Calculator(config)

def test_add(calc):
    assert calc.add(1, 2) == 3
    assert calc.add(1.1, 2.2) == 3.3

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2

def test_multiply(calc):
    assert calc.multiply(3, 2) == 6
    assert calc.multiply(1.5, 2) == 3.0

def test_divide(calc):
    assert calc.divide(6, 2) == 3
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(4, 0.5) == 2.0

def test_sqrt(calc):
    assert calc.sqrt(9) == 3
    with pytest.raises(ValueError):
        calc.sqrt(-1)
