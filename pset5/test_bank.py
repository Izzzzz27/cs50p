from bank import value
def test_default():
    assert value("Hello")==0
    assert value("hello")==0
    assert value("hi")==20


