import pytest
from calculator import Calculator

def test_intentional_failure_demo():
    """This test will fail to show PyTest's error reporting"""
    calc = Calculator()
    result = calc.basic_operations(10, 5, '+')
    assert result == 16  # This should be 15, will fail intentionally

def test_exception_handling():
    """Test that PyTest handles exceptions well"""
    calc = Calculator()
    with pytest.raises(ValueError, match="Unsupported operation"):
        calc.basic_operations(10, 5, 'invalid_op')