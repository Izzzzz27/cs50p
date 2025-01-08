from twttr import shorten

def test_default():
    assert shorten("Twitter")=="Twttr"
    assert shorten("twitter")=="twttr"
    assert shorten("AE")==""
    assert shorten("12")=="12"
    assert shorten(";:")==";:"
