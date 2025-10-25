import math
from typing import Union, List, Optional
from enum import Enum

class CalculatorMode(Enum):
    BASIC = "basic"
    SCIENTIFIC = "scientific"
    PROGRAMMER = "programmer"

class Calculator:
    def __init__(self):
        self.memory: float = 0.0
        self.mode: CalculatorMode = CalculatorMode.BASIC
        self.last_result: Optional[float] = None
    
    def basic_operations(self, a: float, b: float, operation: str) -> float:
        """Perform basic arithmetic operations"""
        operations = {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b if b != 0 else float('inf'),
            '^': a ** b,
            '%': a % b if b != 0 else float('nan')
        }
        
        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")
        
        result = operations[operation]
        self.last_result = result
        return result
    
    def scientific_operations(self, value: float, operation: str) -> float:
        """Perform scientific operations"""
        if operation == 'sin':
            result = math.sin(math.radians(value))
        elif operation == 'cos':
            result = math.cos(math.radians(value))
        elif operation == 'tan':
            result = math.tan(math.radians(value))
        elif operation == 'log':
            result = math.log10(value) if value > 0 else float('nan')
        elif operation == 'ln':
            result = math.log(value) if value > 0 else float('nan')
        elif operation == 'sqrt':
            result = math.sqrt(value) if value >= 0 else float('nan')
        elif operation == 'factorial':
            result = math.factorial(int(value)) if value >= 0 and value.is_integer() else float('nan')
        elif operation == 'exp':
            result = math.exp(value)
        else:
            raise ValueError(f"Unsupported scientific operation: {operation}")
        
        self.last_result = result
        return result
    
    def programmer_operations(self, value: int, operation: str) -> Union[int, str]:
        """Perform programmer operations"""
        if not isinstance(value, int):
            value = int(value)
        
        if operation == 'bin':
            result = bin(value)
        elif operation == 'hex':
            result = hex(value)
        elif operation == 'oct':
            result = oct(value)
        elif operation == 'and':
            result = value & 0xFF
        elif operation == 'or':
            result = value | 0x0F
        elif operation == 'xor':
            result = value ^ 0xFF
        elif operation == 'shift_left':
            result = value << 1
        elif operation == 'shift_right':
            result = value >> 1
        else:
            raise ValueError(f"Unsupported programmer operation: {operation}")
        
        self.last_result = result if isinstance(result, int) else float('nan')
        return result
    
    def memory_operations(self, operation: str, value: float = None) -> float:
        """Perform memory operations"""
        if operation == 'store':
            self.memory = value
        elif operation == 'recall':
            return self.memory
        elif operation == 'add':
            self.memory += value
        elif operation == 'subtract':
            self.memory -= value
        elif operation == 'clear':
            self.memory = 0.0
        else:
            raise ValueError(f"Unsupported memory operation: {operation}")
        
        return self.memory
    
    def set_mode(self, mode: CalculatorMode):
        """Set calculator mode"""
        self.mode = mode
    
    def evaluate_expression(self, expression: str) -> float:
        """Evaluate simple mathematical expressions"""
        try:
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Expression contains invalid characters")
            
            result = eval(expression)
            self.last_result = float(result)
            return self.last_result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
    
    def get_last_result(self) -> Optional[float]:
        """Get the last calculation result"""
        return self.last_result
    
    def clear(self):
        """Clear calculator state"""
        self.last_result = None