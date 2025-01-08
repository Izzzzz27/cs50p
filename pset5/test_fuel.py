from fuel import convert
from fuel import gauge
import pytest

def test_valid():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("1/100")==1
    assert convert("99/100")==99
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_gauge():
    assert gauge(50)=="50%"
    assert gauge(1)=="E"
    assert gauge(99)=="F"
