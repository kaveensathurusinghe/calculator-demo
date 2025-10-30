# PyTest Demo Script for Calculator Project

## Setup Commands (30 seconds)
```bash
# Show project structure
ls -la

# Install dependencies (if needed)
pip install pytest pytest-cov

# Show what tests we have
ls tests/
```

## Key PyTest Features Demo (2.5 minutes)

### 1. Basic Test Execution (30 seconds)
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_basic_operations.py

# Verbose output
pytest tests/test_basic_operations.py -v
```

### 2. PyTest Fixtures Demo (45 seconds)
Show conftest.py and fixture usage:
```bash
# Show fixture file
cat tests/conftest.py

# Run test that uses fixtures
pytest tests/test_basic_operations.py::test_addition -v
```

### 3. Parametrized Testing (45 seconds)
```bash
# Show parametrized test
pytest tests/test_scientific_operations.py::test_trigonometric_functions -v

# Show the actual test code briefly
```

### 4. Coverage Reporting (30 seconds)
```bash
# Run tests with coverage
pytest tests/ --cov=src --cov-report=html

# Show coverage report
open htmlcov/index.html
```

### 5. Advanced Features (20 seconds)
```bash
# Run specific test markers (if any)
pytest tests/ -k "basic"

# Show failing test handling
pytest tests/ --tb=short
```

## Key Points to Mention During Demo:
1. **No boilerplate code needed** - just name files test_*.py
2. **Automatic test discovery** - finds tests automatically
3. **Rich fixture system** - powerful dependency injection
4. **Parametrized tests** - run same test with different inputs
5. **Excellent error reporting** - clear failure messages
6. **Plugin ecosystem** - coverage, parallel testing, etc.
7. **Industry standard** - used by Django, Flask, Pandas, etc.