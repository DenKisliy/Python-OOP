class StrLengthException(ValueError):
    def __init__(self):
        super().__init__("string length too small")

    def __str__(self):
        return f"String length too small"

def check_len(value):
    if len(value) < 10:
        raise StrLengthException
    return len(value)