from utils import dicts
exzampl = {1: "alex", 2: "Vova", 3: "Slava"}

def test_get_value():
    assert dicts.get_value(exzampl, 1,'default') == "alex"
    assert dicts.get_value(exzampl, 5, 'default') == "default"
