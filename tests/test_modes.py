import math
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
