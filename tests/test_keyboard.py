from src.keyboard import Keyboard


kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_str():
    assert str(kb) == 'Dark Project KD87A'

def test_change_lang():
    assert kb.language == 'EN'
    kb.change_lang()
    assert kb.language == 'RU'
