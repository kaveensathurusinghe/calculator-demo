import math
import pytest
from calculator import Calculator, CalculatorMode

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