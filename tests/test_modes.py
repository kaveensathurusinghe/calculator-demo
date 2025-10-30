import math
import pytest
from calculator import Calculator, CalculatorMode


def test_set_mode_changes_mode():
    calc = Calculator()
    assert calc.mode == CalculatorMode.BASIC
    calc.set_mode(CalculatorMode.SCIENTIFIC)
    assert calc.mode == CalculatorMode.SCIENTIFIC
    calc.set_mode(CalculatorMode.PROGRAMMER)
    assert calc.mode == CalculatorMode.PROGRAMMER


def test_programmer_operations_and_last_result_nan():
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    # programmer_operations returns string for bin
    result = calc.programmer_operations(10, 'bin')
    assert result == '0b1010'
    # last_result should be nan because result is not int
    last = calc.get_last_result()
    assert isinstance(last, float)
    assert math.isnan(last)


def test_scientific_operations_work():
    calc = Calculator()
    calc.set_mode(CalculatorMode.SCIENTIFIC)
    # trig uses degrees internally
    assert round(calc.scientific_operations(30, 'sin'), 6) == round(0.5, 6)
    # factorial with integer value
    fact = calc.scientific_operations(5.0, 'factorial')
    assert fact == 120


def test_hex_operation():
    """Test hexadecimal conversion"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(255, 'hex')
    assert result == '0xff'
    # last_result should be nan since result is string
    assert math.isnan(calc.get_last_result())


def test_oct_operation():
    """Test octal conversion"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(8, 'oct')
    assert result == '0o10'
    # last_result should be nan since result is string
    assert math.isnan(calc.get_last_result())


def test_bitwise_and_operation():
    """Test bitwise AND operation"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(0xFF, 'and')
    assert result == 0xFF
    # last_result should be set to the int result
    assert calc.get_last_result() == 0xFF


def test_bitwise_or_operation():
    """Test bitwise OR operation"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(0xF0, 'or')
    assert result == 0xFF  # 0xF0 | 0x0F = 0xFF
    assert calc.get_last_result() == 0xFF


def test_bitwise_xor_operation():
    """Test bitwise XOR operation"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(0x00, 'xor')
    assert result == 0xFF  # 0x00 ^ 0xFF = 0xFF
    assert calc.get_last_result() == 0xFF


def test_shift_left_operation():
    """Test left shift operation"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(5, 'shift_left')
    assert result == 10  # 5 << 1 = 10
    assert calc.get_last_result() == 10


def test_shift_right_operation():
    """Test right shift operation"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(10, 'shift_right')
    assert result == 5  # 10 >> 1 = 5
    assert calc.get_last_result() == 5


def test_programmer_operations_with_float_input():
    """Test programmer operations convert float to int"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    result = calc.programmer_operations(10.7, 'shift_left')
    assert result == 20  # int(10.7) = 10, 10 << 1 = 20


def test_invalid_programmer_operation():
    """Test invalid programmer operation raises error"""
    calc = Calculator()
    calc.set_mode(CalculatorMode.PROGRAMMER)
    with pytest.raises(ValueError, match="Unsupported programmer operation: invalid"):
        calc.programmer_operations(10, 'invalid')
