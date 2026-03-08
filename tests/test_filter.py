from wiqaya import Wiqaya

def test_is_profane_clean_ar():
    w = Wiqaya(lang="ar")
    assert w.is_profane("نص عادي") == False

def test_is_profane_dirty_ar():
    w = Wiqaya(lang="ar")
    assert w.is_profane("حرامي") == True

def test_is_profane_tashkeel():
    w = Wiqaya(lang="ar")
    assert w.is_profane("حَرَامِي") == True

def test_is_profane_mixed():
    w = Wiqaya(lang="ar")
    assert w.is_profane("نص عادي فيه حرامي") == True

def test_get_profane_words_found():
    w = Wiqaya(lang="ar")
    assert w.get_profane_words("نص فيه حرامي و أطرش") == ["حرامي", "أطرش"]

def test_get_profane_words_empty():
    w = Wiqaya(lang="ar")
    assert w.get_profane_words("نص نظيف تماماً") == []

def test_censor_ar():
    w = Wiqaya(lang="ar")
    assert w.censor("نص سيء حرامي", char="*") == "نص سيء *****"

def test_censor_custom_char():
    w = Wiqaya(lang="ar")
    assert w.censor("حرامي", char="#") == "#####"

def test_censor_clean_text():
    w = Wiqaya(lang="ar")
    assert w.censor("نص نظيف") == "نص نظيف"

def test_is_profane_clean_en():
    w = Wiqaya(lang="en")
    assert w.is_profane("Hello World") == False

def test_is_profane_dirty_en():
    w = Wiqaya(lang="en")
    assert w.is_profane("damn") == True

def test_censor_en():
    w = Wiqaya(lang="en")
    assert w.censor("this is damn annoying", char="*") == "this is **** annoying"

def test_get_profane_words_en():
    w = Wiqaya(lang="en")
    assert w.get_profane_words("what the damn hell") == ["damn", "hell"]

def test_invalid_lang():
    import pytest
    with pytest.raises(ValueError):
        Wiqaya(lang="xx")