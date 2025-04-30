def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    if a is None or b is None:
        raise ValueError("All arguments a, and b must be provided")
    return a + b


def parse_age(age_str: str) -> int:
    """Convert age string to integer if valid, else raise error."""
    age_str = age_str.strip()

    if not age_str.isdigit():
        raise ValueError(f"Invalid age: {age_str}")

    age = int(age_str)

    if age < 0 or age > 130:
        raise ValueError(f"Age out of valid range: {age}")

    return age
