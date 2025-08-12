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

    def __add__(self, other):
        """
        Сложение товаров с проверкой совместимости типов.
        Возвращает общую стоимость товаров одного типа
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Нельзя складывать товары разных типов: {self.__class__.__name__} и {other.__class__.__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Вычисление стоимости всех товаров на складе."""
        return (self.price * self.quantity) + (other.price * other.quantity)

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

class Smartphone(Product):
    """Класс для представления смартфонов"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: int, color: str):
        """
                Инициализация экземпляра класса Smartphone

                Args:
                    efficiency: Производительность процессора
                    model: Модель смартфона
                    memory: Объем встроенной памяти (в ГБ)
                    color: Цвет устройства
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение только объектов Smartphone"""
        if not isinstance(other, Smartphone):
            raise TypeError("Можно складывать только смартфоны")
        return super().__add__(other)

class LawnGrass(Product):
    """Класс для представления газонной травы"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
                Инициализация экземпляра класса LawnGrass

                Args:
                    country: Страна-производитель
                    germination_period: Срок прорастания
                    color: Цвет травы
                """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение только объектов LawnGrass"""
        if not isinstance(other, LawnGrass):
            raise TypeError("Можно складывать только газонную траву")
        return super().__add__(other)
