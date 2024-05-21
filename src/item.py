import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(self.__name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, csvfile='../src/items.csv'):
        try:
            Item.all.clear()
            with open(csvfile, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(str(row['name']), float(row['price']), int(row['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        else:
            if len(cls.all) != 5:
                raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(number_string):
        for number in number_string:
            if number.isdigit():
                return int(number)

    def __add__(self, other):
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        raise ValueError('Складывать можно только объекты классов Phone или Item')


class InstantiateCSVError(Exception):
    pass

Item.instantiate_from_csv()
print(Item.all)
