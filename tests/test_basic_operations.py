import math
import pytest
from calculator import Calculator, CalculatorMode


def test_addition_and_subtraction_and_multiplication(calculator):
    assert calculator.basic_operations(2, 3, '+') == 5
    assert calculator.basic_operations(5, 2, '-') == 3
    assert calculator.basic_operations(4, 3, '*') == 12


def test_division_and_division_by_zero(calculator):
    assert calculator.basic_operations(8, 2, '/') == 4
    # division by zero returns inf according to implementation
    result = calculator.basic_operations(1, 0, '/')
    assert result == float('inf')


def test_power_and_modulo(calculator):
    assert calculator.basic_operations(2, 3, '^') == 8
    assert calculator.basic_operations(10, 3, '%') == 1
    # modulo by zero returns nan
    mod_zero = calculator.basic_operations(5, 0, '%')
    assert math.isnan(mod_zero)


def test_last_result_is_set(calculator):
    calculator.basic_operations(7, 3, '+')
    assert calculator.get_last_result() == 10


def test_invalid_operation_raises_error(calculator):
    """Test that invalid operations raise ValueError"""
    with pytest.raises(ValueError, match="Unsupported operation: invalid"):
        calculator.basic_operations(1, 2, 'invalid')


def test_clear_resets_last_result(calculator):
    """Test that clear() resets last_result to None"""
    calculator.basic_operations(5, 3, '+')
    assert calculator.get_last_result() == 8
    calculator.clear()
    assert calculator.get_last_result() is None
