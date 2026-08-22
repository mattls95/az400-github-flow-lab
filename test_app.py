from app import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_add_negative_number():
    assert add(2, -1) == 1

def test_multiply():
    assert multiply(3, 4) == 12