import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import Calculator, CalculatorMode
from history import History

@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture
def history():
    return History(max_entries=10)