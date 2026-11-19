from calculator import add, subtract, multiply, divide
def test_add():
    assert add(10, 5) == 15
def test_subtract():
    assert subtract(10, 5) == 5
def test_multiply():
    assert multiply(2, 3) == 6
def test_divide():
    assert divide(10, 5) == 2