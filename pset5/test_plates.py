from plates import is_valid
def test_valid():
    assert is_valid("HELLO")==True
    assert is_valid("hello, world") == False
def test_valid1():
    assert is_valid("23")==False
    assert is_valid("cs")==True
def test_valid2():
    assert is_valid("cs.,23") == False
def test_valid3():
    assert is_valid("cs05")==False
    assert is_valid("cs50p")==False




