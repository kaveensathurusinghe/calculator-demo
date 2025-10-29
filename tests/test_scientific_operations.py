import math
import pytest
from calculator import Calculator

def test_trigonometric_operations():
    calc = Calculator()
    # Test sine
    assert round(calc.scientific_operations(30, 'sin'), 4) == 0.5  # sin(30°) = 0.5
    assert round(calc.scientific_operations(90, 'sin'), 4) == 1.0  # sin(90°) = 1
    
    # Test cosine
    assert round(calc.scientific_operations(60, 'cos'), 4) == 0.5  # cos(60°) = 0.5
    assert round(calc.scientific_operations(0, 'cos'), 4) == 1.0   # cos(0°) = 1
    
    # Test tangent
    assert round(calc.scientific_operations(45, 'tan'), 4) == 1.0  # tan(45°) = 1
    assert round(calc.scientific_operations(0, 'tan'), 4) == 0.0   # tan(0°) = 0

def test_logarithmic_operations():
    calc = Calculator()
    # Test log (base 10)
    assert calc.scientific_operations(100, 'log') == 2.0  # log10(100) = 2
    assert calc.scientific_operations(1000, 'log') == 3.0  # log10(1000) = 3
    assert math.isnan(calc.scientific_operations(-1, 'log'))  # log of negative number
    assert math.isnan(calc.scientific_operations(0, 'log'))   # log of zero
    
    # Test natural log (base e)
    assert round(calc.scientific_operations(math.e, 'ln'), 4) == 1.0  # ln(e) = 1
    assert math.isnan(calc.scientific_operations(-1, 'ln'))  # ln of negative number
    assert math.isnan(calc.scientific_operations(0, 'ln'))   # ln of zero

def test_square_root_operations():
    calc = Calculator()
    assert calc.scientific_operations(16, 'sqrt') == 4.0  # sqrt(16) = 4
    assert calc.scientific_operations(0, 'sqrt') == 0.0   # sqrt(0) = 0
    assert math.isnan(calc.scientific_operations(-1, 'sqrt'))  # sqrt of negative number

def test_factorial_operations():
    calc = Calculator()
    assert calc.scientific_operations(5, 'factorial') == 120    # 5! = 120
    assert calc.scientific_operations(0, 'factorial') == 1      # 0! = 1
    assert calc.scientific_operations(1, 'factorial') == 1      # 1! = 1
    assert math.isnan(calc.scientific_operations(5.5, 'factorial'))  # factorial of non-integer
    assert math.isnan(calc.scientific_operations(-1, 'factorial'))   # factorial of negative number

def test_exponential_operations():
    calc = Calculator()
    assert calc.scientific_operations(1, 'exp') == pytest.approx(math.e)  # e^1 = e
    assert calc.scientific_operations(0, 'exp') == pytest.approx(1.0)     # e^0 = 1
    assert calc.scientific_operations(-1, 'exp') == pytest.approx(1/math.e)  # e^-1 = 1/e

def test_invalid_operations():
    calc = Calculator()
    with pytest.raises(ValueError, match="Unsupported scientific operation: invalid"):
        calc.scientific_operations(1, 'invalid')

def test_last_result_updates():
    calc = Calculator()
    result = calc.scientific_operations(30, 'sin')
    assert calc.get_last_result() == result  # Check if last_result is updated

def test_edge_cases():
    calc = Calculator()
    # Test very small numbers
    assert calc.scientific_operations(-100, 'exp') < 1e-40  # e^-100 should be very close to 0
    
    # Test precision for small angles in trigonometry
    assert abs(calc.scientific_operations(1, 'sin')) < 0.02  # sin(1°) is very small
    
    # Test very large inputs for logarithms
    assert calc.scientific_operations(1e100, 'log') == pytest.approx(100.0)  # log10(1e100) = 100