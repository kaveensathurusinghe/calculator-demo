import pytest
from calculator import Calculator

def test_intentional_failure_demo(calculator):
    """This test will fail to show PyTest's error reporting"""
    result = calculator.basic_operations(10, 5, '+')
    assert result == 16  # This should be 15, will fail intentionally

def test_exception_handling(calculator):
    """Test that PyTest handles exceptions well"""
    with pytest.raises(ValueError, match="Unsupported operation"):
        calculator.basic_operations(10, 5, 'invalid_op')