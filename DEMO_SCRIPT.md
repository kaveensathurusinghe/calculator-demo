# Pytest Testing Framework Demo Script

## 🎯 Demo Overview
**Duration:** 15-20 minutes  
**Objective:** Demonstrate pytest capabilities using a Calculator application

---

## 📋 Pre-Demo Checklist
- [ ] Terminal ready in project directory
- [ ] Code editor open with `tests/` folder visible
- [ ] pytest installed: `pip install -r requirements.txt`
- [ ] Run quick test to ensure everything works: `pytest --version`

---

## 🎬 Part 1: Introduction (2 minutes)

### What You'll Say:
> "Today we'll explore pytest, Python's most popular testing framework, using a calculator application. We'll see how pytest makes testing simple, powerful, and actually enjoyable!"

### Show the Project Structure:
```bash
tree -L 2
```

### Key Points to Mention:
- **src/** contains the calculator and history modules
- **tests/** contains all our test files
- **conftest.py** is special - it defines shared fixtures
- **pytest.ini** contains pytest configuration

---

## 🎬 Part 2: Running Tests - The Basics (3 minutes)

### Demo Command 1: Run all tests
```bash
pytest
```

**What to highlight:**
- Pytest auto-discovers test files (test_*.py)
- Green dots = passing tests
- Shows total count and duration

### Demo Command 2: Verbose output
```bash
pytest -v
```

**What to highlight:**
- See individual test names
- Understand what each test does
- PASSED/FAILED status for each

### Demo Command 3: Run specific test file
```bash
pytest tests/test_basic_operations.py -v
```

**What to highlight:**
- Can target specific files
- Useful when working on particular features

### Demo Command 4: Run specific test
```bash
pytest tests/test_basic_operations.py::test_addition_and_subtraction_and_multiplication -v
```

**What to highlight:**
- Granular test execution
- Use `::` to specify exact test

---

## 🎬 Part 3: Simple Assert Statements (2 minutes)

### Open: `tests/test_basic_operations.py`

### Show This Test:
```python
def test_addition_and_subtraction_and_multiplication():
    calc = Calculator()
    assert calc.basic_operations(2, 3, '+') == 5
    assert calc.basic_operations(5, 2, '-') == 3
    assert calc.basic_operations(4, 3, '*') == 12
```

**What to say:**
> "Notice how clean this is! Just plain `assert` statements. No `self.assertEqual()` or complex syntax. Pytest makes tests readable like regular Python code."

### Demo: Intentional Failure
Temporarily modify the test:
```python
assert calc.basic_operations(2, 3, '+') == 6  # Wrong!
```

Run:
```bash
pytest tests/test_basic_operations.py::test_addition_and_subtraction_and_multiplication -v
```

**What to highlight:**
- Beautiful failure output with actual vs expected
- Shows exactly where it failed
- Stack trace is clear and helpful

**Don't forget to revert the change!**

---

## 🎬 Part 4: Fixture System (3 minutes)

### Open: `tests/conftest.py`

### Show the Fixtures:
```python
@pytest.fixture
def calculator():
    return Calculator()

@pytest.fixture
def history():
    return History(max_entries=10)
```

**What to say:**
> "Fixtures are pytest's superpower! They provide reusable test data and objects. Define once in conftest.py, use anywhere."

### Create a New Test Using Fixtures

Open `tests/test_basic_operations.py` and add at the bottom:
```python
def test_with_fixture(calculator):
    """Demo: Using the calculator fixture"""
    result = calculator.basic_operations(10, 5, '+')
    assert result == 15
    assert calculator.get_last_result() == 15
```

Run it:
```bash
pytest tests/test_basic_operations.py::test_with_fixture -v
```

**What to highlight:**
- No need to create `Calculator()` manually
- Just add `calculator` as parameter
- Pytest automatically provides it
- Each test gets a fresh instance (isolation)

---

## 🎬 Part 5: Parametrized Tests (3 minutes)

### Open: `tests/test_parametrized_demo.py`

### Show a Parametrized Test:
```python
@pytest.mark.parametrize("a,b,operation,expected", [
    (2, 3, '+', 5),
    (10, 5, '-', 5),
    (4, 5, '*', 20),
    (20, 4, '/', 5),
])
def test_basic_operations_parametrized(a, b, operation, expected):
    calc = Calculator()
    assert calc.basic_operations(a, b, operation) == expected
```

**What to say:**
> "Instead of writing 4 separate tests, parametrize runs the same test with different inputs. This is DRY (Don't Repeat Yourself) testing!"

Run it:
```bash
pytest tests/test_parametrized_demo.py -v
```

**What to highlight:**
- Each parameter set runs as a separate test
- 4 test executions from 1 test function
- If one fails, others still run
- Great for edge cases and data-driven testing

---

## 🎬 Part 6: Testing Exceptions (2 minutes)

### Open: `tests/test_basic_operations.py`

### Show Exception Test:
```python
def test_invalid_operation_raises_error():
    """Test that invalid operations raise ValueError"""
    calc = Calculator()
    with pytest.raises(ValueError, match="Unsupported operation: invalid"):
        calc.basic_operations(1, 2, 'invalid')
```

Run it:
```bash
pytest tests/test_basic_operations.py::test_invalid_operation_raises_error -v
```

**What to say:**
> "Testing that code properly fails is just as important as testing success! pytest.raises() makes this elegant."

**What to highlight:**
- `pytest.raises()` context manager
- Can match error message with regex
- Test passes when exception is raised
- Fails if exception is NOT raised

---

## 🎬 Part 7: Test Organization with Classes (2 minutes)

### Open: `tests/test_history.py`

### Show Class-Based Organization:
```python
class TestHistoryBasics:
    """Test basic History functionality"""

    def test_init_with_default_max_entries(self):
        history = History()
        assert history.max_entries == 100

    def test_init_with_custom_max_entries(self):
        history = History(max_entries=50)
        assert history.max_entries == 50
```

**What to say:**
> "Pytest supports organizing related tests into classes. No need to inherit from TestCase - just group logically!"

Run class tests:
```bash
pytest tests/test_history.py::TestHistoryBasics -v
```

**What to highlight:**
- Group related tests together
- Clear structure with descriptive class names
- Can run entire class or individual tests
- No inheritance required (unlike unittest)

---

## 🎬 Part 8: Mocking and Patching (2 minutes)

### Open: `tests/test_history.py`

### Show Mock Example:
```python
def test_add_entry_timestamp_format(self):
    """Test that timestamp is in ISO format"""
    history = History()
    with patch('history.datetime') as mock_datetime:
        mock_datetime.now.return_value.isoformat.return_value = '2023-01-01T12:00:00'
        history.add_entry('+', [1, 1], 2.0)
        
        entry = history.history[0]
        assert entry['timestamp'] == '2023-01-01T12:00:00'
```

**What to say:**
> "When testing, we need to control external dependencies. Here we mock datetime to get predictable timestamps."

Run it:
```bash
pytest tests/test_history.py::TestAddEntry::test_add_entry_timestamp_format -v
```

**What to highlight:**
- `unittest.mock.patch` works great with pytest
- Mock external dependencies (time, file I/O, APIs)
- Tests become deterministic and fast
- No real files created or network calls made

---

## 🎬 Part 9: Test Coverage (2 minutes)

### Run Coverage Report:
```bash
pytest --cov=src --cov-report=term-missing
```

**What to highlight:**
- Shows which lines are tested
- Identifies untested code paths
- `term-missing` shows exact line numbers
- Aim for high coverage, but 100% isn't always necessary

### Generate HTML Report (Optional):
```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

**What to say:**
> "Coverage tools help identify gaps in testing. The HTML report is interactive and shows exactly what's covered."

---

## 🎬 Part 10: Demonstrating Test Failure (2 minutes)

### Open: `tests/test_demo_failure.py`

This file should have an intentional failing test for demo purposes.

Run:
```bash
pytest tests/test_demo_failure.py -v
```

**What to highlight:**
- Clear failure messages
- Helpful traceback
- Actual vs expected values
- Easy to debug

---

## 🎬 Part 11: Useful Pytest Options (1 minute)

### Show Quick Commands:

```bash
# Stop at first failure
pytest -x

# Run last failed tests only
pytest --lf

# Show print statements
pytest -s

# Run tests matching keyword
pytest -k "history"

# Show slowest tests
pytest --durations=5

# Parallel execution (if pytest-xdist installed)
pytest -n auto
```

**What to say:**
> "Pytest has tons of useful flags to speed up your workflow!"

---

## 🎬 Part 12: Wrap-Up (1 minute)

### Summary Points:
1. ✅ **Simple syntax** - Plain assert statements
2. ✅ **Fixtures** - Reusable test components
3. ✅ **Parametrization** - DRY testing
4. ✅ **Great output** - Clear success/failure messages
5. ✅ **Flexible organization** - Functions or classes
6. ✅ **Rich ecosystem** - Plugins for everything
7. ✅ **Coverage tools** - Know what's tested
8. ✅ **Easy to learn** - Start simple, grow advanced

### Final Demo:
```bash
pytest -v --cov=src --cov-report=term
```

**What to say:**
> "Pytest makes testing accessible and even enjoyable. It grows with you from simple unit tests to complex integration scenarios. That's why it's the standard for modern Python projects!"

---

## 💡 Bonus Tips for Your Presentation

### Engage the Audience:
- Ask: "Who's written tests before? Who's used pytest?"
- Show enthusiasm about testing (it's actually cool!)
- Mention real-world benefits (fewer bugs, confident refactoring)

### Common Questions & Answers:

**Q: Is pytest better than unittest?**  
A: For most cases, yes! Simpler syntax, more features, active development. Unittest is good for standard library users.

**Q: Do I need to learn all features at once?**  
A: No! Start with basic assertions, add fixtures later, then parametrization, etc.

**Q: What about pytest vs Jest/JUnit?**  
A: Similar philosophy across languages. Pytest is Python's equivalent.

**Q: How do I run tests in CI/CD?**  
A: Same command! `pytest` works in GitHub Actions, Jenkins, etc.

---

## 📝 Practice Run Checklist

Before your presentation:
- [ ] Run through entire script once
- [ ] Time yourself (aim for 15-18 minutes)
- [ ] Prepare backup examples
- [ ] Test all commands work
- [ ] Have questions ready
- [ ] Prepare for technical difficulties

---

## 🚀 Good Luck!

Remember: 
- Speak clearly and not too fast
- Show passion for testing
- Make eye contact
- Be ready to go off-script for questions
- Have fun! 🎉
