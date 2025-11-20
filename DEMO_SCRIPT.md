# Pytest Demo Script - 3 MINUTES ⚡

## 🎯 Quick Setup
- Terminal in project directory
- Editor showing `tests/` folder
- Confidence! 💪

---

## ⏱️ PART 1: What is Pytest? (30 seconds)

**Say:** "Pytest is Python's most popular testing framework. Why? Simple syntax, powerful features, and great developer experience!"

---

## ⏱️ PART 2: Running Tests (45 seconds)

```bash
# Run all tests
pytest -v
```

**Show:**
- ✅ Auto-discovers test files
- ✅ Clear PASSED/FAILED output
- ✅ 40+ tests running in seconds

---

## ⏱️ PART 3: Simple Assert Magic (30 seconds)

**Open:** `tests/test_basic_operations.py`

**Show this test:**
```python
def test_addition_and_subtraction_and_multiplication():
    calc = Calculator()
    assert calc.basic_operations(2, 3, '+') == 5  # That's it!
    assert calc.basic_operations(5, 2, '-') == 3
```

**Say:** "Just plain `assert` - no `self.assertEqual()` needed. Clean and readable!"

---

## ⏱️ PART 4: Fixtures = Reusable Setup (30 seconds)

**Open:** `tests/conftest.py`

```python
@pytest.fixture
def calculator():
    return Calculator()
```

**Say:** "Fixtures provide reusable test objects. Define once, use everywhere!"

**Quick example:**
```python
def test_with_fixture(calculator):  # ← Auto-injected!
    assert calculator.basic_operations(10, 5, '+') == 15
```

---

## ⏱️ PART 5: Parametrized Tests = DRY (30 seconds)

**Open:** `tests/test_parametrized_demo.py`

```python
@pytest.mark.parametrize("a,b,operation,expected", [
    (2, 3, '+', 5),
    (10, 5, '-', 5),
    (4, 5, '*', 20),
])
def test_basic_operations_parametrized(a, b, operation, expected):
    calc = Calculator()
    assert calc.basic_operations(a, b, operation) == expected
```

**Say:** "One test function, multiple scenarios. No code duplication!"

---

## ⏱️ PART 6: Coverage Report (15 seconds)

```bash
pytest --cov=src --cov-report=term
```

**Say:** "Built-in coverage shows what's tested. We have 95%+ coverage!"

---

## ⏱️ PART 7: Wrap-Up (30 seconds)

**Key Takeaways:**
1. ✅ **Simple** - Plain assert statements
2. ✅ **Fixtures** - Reusable test setup  
3. ✅ **Parametrize** - Test multiple cases easily
4. ✅ **Coverage** - Know what's tested
5. ✅ **Powerful** - Mocking, exceptions, and more!

**Final words:** "Pytest makes testing fast, easy, and actually enjoyable. That's why it's the industry standard!"

---

## 💡 Pro Tips

### If you have 30 extra seconds:
**Show a failing test:**
```bash
pytest tests/test_demo_failure.py -v
```
Point out the beautiful error messages!

### If someone asks "Why pytest over unittest?":
"Simpler syntax, better output, modern features, and active development!"

### Commands cheat sheet:
```bash
pytest -v          # Verbose
pytest -x          # Stop on first failure  
pytest -k "test_name"  # Run specific tests
pytest --cov=src   # With coverage
```

---

## ⏱️ Practice Timeline

- 0:00 - 0:30 → Introduction
- 0:30 - 1:15 → Run tests + show assert
- 1:15 - 1:45 → Fixtures demo
- 1:45 - 2:15 → Parametrized tests
- 2:15 - 2:30 → Coverage
- 2:30 - 3:00 → Wrap-up

**Total: 3 minutes sharp!**

---

## 🚀 You Got This!

- Speak clearly, not rushed
- Show confidence
- Let your enthusiasm shine
- Good luck! 🎉
