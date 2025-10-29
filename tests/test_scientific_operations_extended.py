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