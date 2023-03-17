from utils import dicts
import pytest

@pytest.fixture
def exzampl():
    return {1: "alex", 2: "Vova", 3: "Slava"}

def test_get_value(exzampl):
    assert dicts.get_value(exzampl, 1,'default') == "alex"
    assert dicts.get_value(exzampl, 5,) == "git"
