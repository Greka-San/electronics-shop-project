from src.item import Item


example = Item("Телевизор", 30_000, 10)


def test_calculate_total_price():
    assert example.calculate_total_price() == 300_000


def test_apply_discount():
    example.pay_rate = 0.5
    example.apply_discount()
    assert example.price == 15_000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.9") == 5

