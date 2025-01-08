from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

def test_format_2():
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')

def test_time():
    with pytest.raises(ValueError):
        convert('13 AM to 9 PM')
    with pytest.raises(ValueError):
        convert('5 AM to 0 PM')
    with pytest.raises(ValueError):
        convert('5:60 AM to 11:30 PM')
    with pytest.raises(ValueError):
        convert('5:30 AM to 11:90 PM')

def test_return_value():
    assert convert('5 AM to 9 PM') == '05:00 to 21:00'
    assert convert('5:30 AM to 9:30 PM') == '05:30 to 21:30'

def test_return_value2():
    assert convert('5 AM to 9 PM') != '5:0 to 21:00'
    assert convert('5:30 AM to 9:30 PM') != '5 to 9'

def main():
    test_format()
    test_time()
    test_return_value()
    test_return_value2()
    test_format_2()

if __name__ == '__main__':
    main()
