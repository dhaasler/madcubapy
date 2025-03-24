__all__ = [
    'is_number',
]

def is_number(s):
    """Checks if a string is a float number or has other characters."""
    try:
        float(s)
        return True
    except ValueError:
        return False
    