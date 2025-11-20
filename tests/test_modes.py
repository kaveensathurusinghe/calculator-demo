import math
import pytest
from calculator import Calculator, CalculatorMode


def test_set_mode_changes_mode(calculator):
    assert calculator.mode == CalculatorMode.BASIC
    calculator.set_mode(CalculatorMode.SCIENTIFIC)
    assert calculator.mode == CalculatorMode.SCIENTIFIC
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    assert calculator.mode == CalculatorMode.PROGRAMMER


def test_programmer_operations_and_last_result_nan(calculator):
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    # programmer_operations returns string for bin
    result = calculator.programmer_operations(10, 'bin')
    assert result == '0b1010'
    # last_result should be nan because result is not int
    last = calculator.get_last_result()
    assert isinstance(last, float)
    assert math.isnan(last)


def test_scientific_operations_work(calculator):
    calculator.set_mode(CalculatorMode.SCIENTIFIC)
    # trig uses degrees internally
    assert round(calculator.scientific_operations(30, 'sin'), 6) == round(0.5, 6)
    # factorial with integer value
    fact = calculator.scientific_operations(5.0, 'factorial')
    assert fact == 120


def test_hex_operation(calculator):
    """Test hexadecimal conversion"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(255, 'hex')
    assert result == '0xff'
    # last_result should be nan since result is string
    assert math.isnan(calculator.get_last_result())


def test_oct_operation(calculator):
    """Test octal conversion"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(8, 'oct')
    assert result == '0o10'
    # last_result should be nan since result is string
    assert math.isnan(calculator.get_last_result())


def test_bitwise_and_operation(calculator):
    """Test bitwise AND operation"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(0xFF, 'and')
    assert result == 0xFF
    # last_result should be set to the int result
    assert calculator.get_last_result() == 0xFF


def test_bitwise_or_operation(calculator):
    """Test bitwise OR operation"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(0xF0, 'or')
    assert result == 0xFF  # 0xF0 | 0x0F = 0xFF
    assert calculator.get_last_result() == 0xFF


def test_bitwise_xor_operation(calculator):
    """Test bitwise XOR operation"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(0x00, 'xor')
    assert result == 0xFF  # 0x00 ^ 0xFF = 0xFF
    assert calculator.get_last_result() == 0xFF


def test_shift_left_operation(calculator):
    """Test left shift operation"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(5, 'shift_left')
    assert result == 10  # 5 << 1 = 10
    assert calculator.get_last_result() == 10


def test_shift_right_operation(calculator):
    """Test right shift operation"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(10, 'shift_right')
    assert result == 5  # 10 >> 1 = 5
    assert calculator.get_last_result() == 5


def test_programmer_operations_with_float_input(calculator):
    """Test programmer operations convert float to int"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    result = calculator.programmer_operations(10.7, 'shift_left')
    assert result == 20  # int(10.7) = 10, 10 << 1 = 20


def test_invalid_programmer_operation(calculator):
    """Test invalid programmer operation raises error"""
    calculator.set_mode(CalculatorMode.PROGRAMMER)
    with pytest.raises(ValueError, match="Unsupported programmer operation: invalid"):
        calculator.programmer_operations(10, 'invalid')
