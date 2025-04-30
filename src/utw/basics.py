def add_numbers(a, b):
    """Add two numbers together."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b


def parse_age(age_str: str) -> int:
    """Convert age string to integer if valid, else raise error."""
    age_str = age_str.strip()

    if not age_str.isdigit():
        raise ValueError(f"Invalid age: {age_str}")

    age = int(age_str)

    if age < 0 or age > 130:
        raise ValueError(f"Age out of valid range: {age}")

    return age
