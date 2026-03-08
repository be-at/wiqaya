from wiqaya.utils import remove_tashkeel

def test_no_tashkeel():
    text = "مرحبا"
    assert remove_tashkeel(text) == text

def test_with_tashkeel():
    assert remove_tashkeel("مَرْحَباً") == "مرحبا"

def test_english_unchanged():
    text = "hello world"
    assert remove_tashkeel(text) == text