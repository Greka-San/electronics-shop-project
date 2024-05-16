from src.phone import Phone


def test_repr():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
