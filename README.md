# Unit Testing Workshop

If at any point during the coding exercises you want to jump ahead, or start fresh,
you can checkout the "final" version of the exercise
for example if you are working on the 01-running-tests branch and want to start fresh,
you can run:

```bash
git checkout 01-running-tests-final
```

## 1. Setup (Hands On)

```bash
make setup
source .venv/bin/activate
```

## 2. Project Structure (Discussion)

# Project Structure: `utw`

This is a Python project organized using a `src/`-layout pattern, with a focus on clean separation of source code, tests, and configuration.

## 📁 Directory Overview

```text
utw/
├── Makefile
├── README.md
├── install.sh
├── pyproject.toml
├── src/
│   ├── tests/
│   │   └── test_calculator_01.py
│   └── utw/
│       ├── __init__.py
│       ├── calculator.py
│       └── py.typed

```

File Desctiptions:
📂 Root Directory (utw/)
Makefile
Automates setup and development tasks like installing dependencies, running tests, or setting up the environment.

README.md
Project documentation: usage, purpose, how to run tests, etc.

install.sh
Shell script to bootstrap the environment. Called manually or from the Makefile.

pyproject.toml
Central configuration file. Used to declare dependencies and tool settings for Python build backends (e.g., setuptools, uv, pytest).

📂 Source Directory (src/)
Used to isolate production code from top-level config and test files.

📂 Tests (src/tests/)
test_calculator_01.py
Unit tests for logic in calculator.py. Organized separately to avoid polluting the main namespace.

📂 Application Code (src/utw/)
**init**.py
Declares this as a Python package. May define **all** or initialize package-wide variables.

calculator.py
Core module with the functions to be tested. Implements business logic.

py.typed
A marker file indicating this package supports static type checking (PEP 561).

## 3. Running and Evaluating Tests (Hands On)

```

git checkout 01-running-tests

```

### tests

```

make test

```

### Coverage

```

make coverage

```

### Inspect coverage

```

coverage html
open htmlcov/index.html

```

## 4. Basic Unit Testing (Hands On)

Objective: Create basic unit tests

1. Write a new function
2. Define tests for that function

## 5. Test Driven Development - (Demo/Discussion)

1. What does it look like?
2. Is TDD the "best" way?

## 6. Fixtures (Hands On)

## 7. Mocking (Hands On)

```

```
