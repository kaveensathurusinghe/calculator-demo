# Calculator Demo

A Python calculator with basic, scientific, and programmer operations.

## Setup Guide

### Prerequisites
- Python 3.6 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaveensathurusinghe/calculator-demo.git
   cd calculator-demo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the calculator**
   ```bash
   python -c "from src.calculator import Calculator; calc = Calculator(); print('Calculator ready!')"
   ```

### Running Tests
```bash
pytest tests/
```

### Usage Example
```python
from src.calculator import Calculator

calc = Calculator()
result = calc.basic_operations(10, 5, '+')
print(f"Result: {result}")  # Output: 15.0
```