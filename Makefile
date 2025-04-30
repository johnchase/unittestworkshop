.PHONY: setup test lint coverage clean

# Create virtualenv and install requirements
setup:
	./install.sh

# Run tests with pytest
test:
	source .venv/bin/activate && pytest -v

# Run tests and show coverage report in terminal
coverage:
	source .venv/bin/activate && pytest --cov=utw --cov-report=term

# Run ruff linter (optional, if ruff is added to requirements)
lint:
	source .venv/bin/activate && ruff .

# Remove virtualenv and .pyc files
clean:
	rm -rf .venv __pycache__ */__pycache__ .pytest_cache .coverage htmlcov
