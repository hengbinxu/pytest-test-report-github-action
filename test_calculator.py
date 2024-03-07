import pytest
from calculator import Calculator


def test_add() -> None:
    calculator = Calculator(0)
    calculator.add(2, 2, 2)
    assert calculator.get_result() == 6


def test_subtract() -> None:
    calculator = Calculator(10)
    calculator.subtract(5)
    assert calculator.get_result() == 5


def test_multiply() -> None:
    calculator = Calculator(10)
    calculator.multiply(2)
    assert calculator.get_result() == 20


def test_divide() -> None:
    calculator = Calculator(10)
    calculator.divide(2)
    assert calculator.get_result() == 5


def test_zero_division_error() -> None:
    with pytest.raises(ZeroDivisionError):
        calculator = Calculator(10)
        calculator.divide(0)


def test_reset() -> None:
    calculator = Calculator(10)
    calculator.reset()
    assert calculator.get_result() == 0


def test_set() -> None:
    calculator = Calculator(10)
    calculator.set_result(100)
    assert calculator.get_result() == 100
