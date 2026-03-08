from wiqaya import Wiqaya

def test_is_profane():
    w = Wiqaya(lang="ar")
    assert w.is_profane("نص عادي") == False

def test_censor():
    w = Wiqaya(lang="ar")
    text = "نص سيء حرامي"
    print(w.censor(text, char="*") )
    assert w.censor(text, char="*") == "نص سيء *****"