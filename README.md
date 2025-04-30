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

### 📁 Directory Overview

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

### 📁 Root (`utw/`)

- **Makefile**  
  Automates setup and workflow tasks like creating the virtual environment, installing dependencies, and running tests.

- **README.md**  
  Project overview and documentation for contributors or users.

- **install.sh**  
  Optional shell script to initialize the environment or run setup steps.

- **pyproject.toml**  
  Central configuration file defining the project metadata, dependencies, build system, and tool settings.

### Source Code (`src/`)

Organize to isolote test and application code

#### 📁 `src/tests/`

- **test_calculator_01.py**  
  Unit tests for the `calculator.py` module. The `01` may imply this is part of a multi-part test suite.

#### `src/utw/`

- \***\*init**.py\*\*  
  Marks this directory as a Python package. May also expose selected functionality at the package level.

- **calculator.py**  
  Contains core logic or utility functions that the project provides — this is the main code being tested.

- **py.typed**  
  A [PEP 561](https://peps.python.org/pep-0561/) marker file indicating this package uses type hints and supports type checking.

## 3. Running and Evaluating Tests (Hands On)

### tests

```bash
make test
```

### Coverage

```bash
make coverage
```

### Inspect coverage

```bash
coverage html
open htmlcov/index.html
```

## 4. Basic Unit Testing (Hands On)

#### 1. Create basic unit tests

```bash
git checkout 01-basic-unit-tests
```

1. Write a new function
2. Define tests for that function

#### 2. Fixtures for reusable data

```bash
git checkout 02-fixtures
```

#### 3. Mocking for external dependencies and complex objects

```bash
git checkout 03-mocking
```

## 5. Test Driven Development - (Demo/Discussion)

1. What does it look like?
2. Is TDD the "best" way?
