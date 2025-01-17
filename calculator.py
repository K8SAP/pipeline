def add(a, b):
    c = a + b
    # c += 2
    return c

def subtract(a, b):
    return a - b

# Example usage
if __name__ == "__main__":
    print("Addition: ", add(2, 3))
    print("Subtraction: ", subtract(5, 3))

# Tests
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
