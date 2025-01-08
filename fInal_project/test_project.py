from project import curren, howmany, val
def test_curren():
    assert curren("ff") == "FF"
def test_hm():
    assert howmany("5")==5
def test_val():
    assert val("5.2") == 5.2
