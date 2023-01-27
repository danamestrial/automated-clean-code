from automated_clean_code.exercise_20_histlib import find_min_max_key, hist_filler, hist_lib


def test_hist_filler():
    sol = {"h": 1, "e": 1, "l": 2, "o": 1}
    assert hist_filler("hello") == sol


def test_find_min_max_key():
    sol = ("l", "h")
    hist = {"h": 1, "e": 1, "l": 2, "o": 1}
    assert find_min_max_key(hist) == sol


def test_hist_lib(capsys: object):
    hist_lib("hello")
    captured = capsys.readouterr()
    assert captured.out == "Min Key = h with count = 1 \nMax Key = l with count = 2\n"
