import pytest
from calculator import Calculator

# Parametrized test example for demo
@pytest.mark.parametrize("a,b,operation,expected", [
    (10, 5, '+', 15),
    (10, 5, '-', 5), 
    (10, 5, '*', 50),
    (10, 5, '/', 2),
])
def test_basic_operations_parametrized(calculator, a, b, operation, expected):
    """Parametrized test showing multiple test cases at once"""
    result = calculator.basic_operations(a, b, operation)
    assert result == expected

@pytest.mark.parametrize("angle,expected", [
    (0, 0),
    (30, 0.5),
    (90, 1.0),
])
def test_sine_values(calculator, angle, expected):
    """Test sine function with different angles"""
    result = calculator.scientific_operations(angle, 'sin')
    assert round(result, 1) == expected