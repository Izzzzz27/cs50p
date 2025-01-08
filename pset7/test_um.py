from um import count

def test_1():
    assert count("um")==1
    assert count("um um") ==2
    assert count("re um re um ") == 2
    assert count("Um")==1
    assert count("ff")==0

