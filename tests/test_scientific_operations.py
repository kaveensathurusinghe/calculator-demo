import math
import pytest
from calculator import Calculator, CalculatorMode

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


def test_hyperbolic_trigonometry():
    """Test hyperbolic trig functions by comparing with manual calculations"""
    calc = Calculator()
    # sinh(x) = (e^x - e^-x)/2
    x = 1.0
    sinh_x = (math.exp(x) - math.exp(-x))/2
    result = calc.scientific_operations(x, 'exp') - calc.scientific_operations(-x, 'exp')
    assert result/2 == pytest.approx(sinh_x)


def test_inverse_operations():
    """Test that operations are inverses of each other"""
    calc = Calculator()
    # exp(ln(x)) should be x for positive x
    x = 2.5
    ln_x = calc.scientific_operations(x, 'ln')
    result = calc.scientific_operations(ln_x, 'exp')
    assert result == pytest.approx(x)


def test_scientific_special_values():
    """Test operations with special values like e, pi"""
    calc = Calculator()
    # ln(e) should be 1
    e_value = math.e
    assert calc.scientific_operations(e_value, 'ln') == pytest.approx(1.0)
    
    # sin(90°) should be 1
    assert calc.scientific_operations(90, 'sin') == pytest.approx(1.0)


def test_memory_with_scientific():
    """Test memory operations combined with scientific operations"""
    calc = Calculator()
    # Store sin(30°) in memory
    sin_30 = calc.scientific_operations(30, 'sin')
    calc.memory_operations('store', sin_30)
    
    # Recall and verify
    recalled = calc.memory_operations('recall')
    assert recalled == pytest.approx(0.5)  # sin(30°) = 0.5


def test_mode_switching_with_scientific():
    """Test switching modes while using scientific operations"""
    calc = Calculator()
    # Start in scientific mode
    calc.set_mode(CalculatorMode.SCIENTIFIC)
    result1 = calc.scientific_operations(45, 'sin')
    
    # Switch to basic and back
    calc.set_mode(CalculatorMode.BASIC)
    calc.set_mode(CalculatorMode.SCIENTIFIC)
    result2 = calc.scientific_operations(45, 'sin')
    
    # Results should be the same
    assert result1 == result2


def test_store_operation():
    """Test storing value in memory"""
    calc = Calculator()
    result = calc.memory_operations('store', 42.5)
    assert result == 42.5
    assert calc.memory == 42.5


def test_recall_operation():
    """Test recalling value from memory"""
    calc = Calculator()
    calc.memory = 15.7
    result = calc.memory_operations('recall')
    assert result == 15.7


def test_add_to_memory():
    """Test adding value to memory"""
    calc = Calculator()
    calc.memory = 10.0
    result = calc.memory_operations('add', 5.0)
    assert result == 15.0
    assert calc.memory == 15.0


def test_subtract_from_memory():
    """Test subtracting value from memory"""
    calc = Calculator()
    calc.memory = 20.0
    result = calc.memory_operations('subtract', 7.0)
    assert result == 13.0
    assert calc.memory == 13.0


def test_clear_memory():
    """Test clearing memory"""
    calc = Calculator()
    calc.memory = 99.9
    result = calc.memory_operations('clear')
    assert result == 0.0
    assert calc.memory == 0.0


def test_invalid_memory_operation():
    """Test invalid memory operation raises error"""
    calc = Calculator()
    with pytest.raises(ValueError, match="Unsupported memory operation: invalid"):
        calc.memory_operations('invalid', 10.0)