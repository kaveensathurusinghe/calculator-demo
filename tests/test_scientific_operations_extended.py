import math
import pytest
from calculator import Calculator, CalculatorMode

def test_hyperbolic_trigonometry(calculator):
    """Test hyperbolic trig functions by comparing with manual calculations"""
    # sinh(x) = (e^x - e^-x)/2
    x = 1.0
    sinh_x = (math.exp(x) - math.exp(-x))/2
    result = calculator.scientific_operations(x, 'exp') - calculator.scientific_operations(-x, 'exp')
    assert result/2 == pytest.approx(sinh_x)

def test_inverse_operations(calculator):
    """Test that operations are inverses of each other"""
    # exp(ln(x)) should be x for positive x
    x = 2.5
    ln_x = calculator.scientific_operations(x, 'ln')
    result = calculator.scientific_operations(ln_x, 'exp')
    assert result == pytest.approx(x)

def test_scientific_special_values(calculator):
    """Test operations with special values like e, pi"""
    # ln(e) should be 1
    e_value = math.e
    assert calculator.scientific_operations(e_value, 'ln') == pytest.approx(1.0)
    
    # sin(90°) should be 1
    assert calculator.scientific_operations(90, 'sin') == pytest.approx(1.0)

def test_memory_with_scientific(calculator):
    """Test memory operations combined with scientific operations"""
    # Store sin(30°) in memory
    sin_30 = calculator.scientific_operations(30, 'sin')
    calculator.memory_operations('store', sin_30)
    
    # Recall and verify
    recalled = calculator.memory_operations('recall')
    assert recalled == pytest.approx(0.5)  # sin(30°) = 0.5

def test_mode_switching_with_scientific(calculator):
    """Test switching modes while using scientific operations"""
    # Start in scientific mode
    calculator.set_mode(CalculatorMode.SCIENTIFIC)
    result1 = calculator.scientific_operations(45, 'sin')
    
    # Switch to basic and back
    calculator.set_mode(CalculatorMode.BASIC)
    calculator.set_mode(CalculatorMode.SCIENTIFIC)
    result2 = calculator.scientific_operations(45, 'sin')
    
    # Results should be the same
    assert result1 == result2


def test_store_operation(calculator):
    """Test storing value in memory"""
    result = calculator.memory_operations('store', 42.5)
    assert result == 42.5
    assert calculator.memory == 42.5


def test_recall_operation(calculator):
    """Test recalling value from memory"""
    calculator.memory = 15.7
    result = calculator.memory_operations('recall')
    assert result == 15.7


def test_add_to_memory(calculator):
    """Test adding value to memory"""
    calculator.memory = 10.0
    result = calculator.memory_operations('add', 5.0)
    assert result == 15.0
    assert calculator.memory == 15.0


def test_subtract_from_memory(calculator):
    """Test subtracting value from memory"""
    calculator.memory = 20.0
    result = calculator.memory_operations('subtract', 7.0)
    assert result == 13.0
    assert calculator.memory == 13.0


def test_clear_memory(calculator):
    """Test clearing memory"""
    calculator.memory = 99.9
    result = calculator.memory_operations('clear')
    assert result == 0.0
    assert calculator.memory == 0.0


def test_invalid_memory_operation(calculator):
    """Test invalid memory operation raises error"""
    with pytest.raises(ValueError, match="Unsupported memory operation: invalid"):
        calculator.memory_operations('invalid', 10.0)