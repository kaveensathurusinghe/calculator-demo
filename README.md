# Calculator Demo

A small Python calculator project with basic and scientific operations and a simple test suite.

## Quick setup (macOS / zsh)

These steps get you from a fresh clone to running tests and trying the calculator interactively.

1. Install a recent Python (this project was developed with Python 3.12). On macOS you can use Homebrew:

```zsh
brew install python@3.12
# or use pyenv / other manager if you prefer
```

2. Create and activate a virtual environment (recommended):

```zsh
cd /path/to/calculator-demo
python3 -m venv .venv
source .venv/bin/activate
# On some systems use: source .venv/bin/activate.fish (for fish) or .venv\Scripts\activate (Windows)
```

3. Install project dependencies:

```zsh
pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the test suite (uses pytest):

```zsh
pytest -q
```

5. Quick smoke test / REPL example:

```zsh
python -c "from src.calculator import Calculator; c=Calculator(); print('2 + 3 =', c.basic_operations(2, 3, '+'))"
# or run a small script:
python - <<'PY'
from src.calculator import Calculator
calc = Calculator()
print('7 * 6 =', calc.basic_operations(7, 6, '*'))
PY
```

## Project layout

- `src/` - library code (calculator implementation and history)
- `tests/` - pytest test suite
- `requirements.txt` - runtime test dependencies

## Notes

- If you add dependencies, update `requirements.txt` (pip freeze > requirements.txt is acceptable for this demo).
- For development, run `pytest` frequently to catch regressions. Tests are intentionally small and fast.

If you'd like, I can also add a short CONTRIBUTING or a script to bootstrap the environment automatically.