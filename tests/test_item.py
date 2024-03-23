"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


example = Item("Телевизор", 30_000, 10)


def test_calculate_total_price():
    assert example.calculate_total_price() == 300_000


def test_apply_discount():
    example.pay_rate = 0.5
    example.apply_discount()
    assert example.price == 15_000
