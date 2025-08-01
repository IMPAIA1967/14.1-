class Product:
    """Класс для представления товара в магазине."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        """
        Инициализация экземпляра класса Product.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, value):
        """
        Устанавливает новую цену товара с проверками.

        Args:
            value: Новая цена товара
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirm = input(
                f'Цена товара {self.name} снизится с {self.__price} '
                f'до {value}. Подтверждаете изменение? (y/n): '
            )
            if confirm.lower() != 'y':
                print("Действие отменено.")
                return
            self.__price = value
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Создает новый товар из словаря с параметрами.

        Args:
            product_data: Словарь с параметрами товара

        Returns:
            Product: Новый экземпляр класса Product
        """
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )
