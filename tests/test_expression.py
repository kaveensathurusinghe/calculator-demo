import pytest
from calculator import Calculator


def test_evaluate_simple_expression(calculator):
    assert calculator.evaluate_expression("2 + 3 * 4") == 14.0


def test_evaluate_invalid_characters(calculator):
    with pytest.raises(ValueError) as excinfo:
        calculator.evaluate_expression("2 + 3a")
    assert "invalid characters" in str(excinfo.value).lower()


def test_evaluate_division_by_zero_raises_valueerror(calculator):
    with pytest.raises(ValueError) as excinfo:
        calculator.evaluate_expression("1/0")
    # Implementation wraps underlying exception in ValueError
    assert "invalid expression" in str(excinfo.value).lower()
