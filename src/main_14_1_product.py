from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта"""
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        """Сложение продуктов (стоимость всех товаров на складе)"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Получение текущей цены товара"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value) -> None:
        """Установка новой цены товара с проверками"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        """Создание нового продукта из словаря с параметрами"""
        pass

class Mixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        # Передаем управление следующему классу в цепочке наследования




class Product(Mixin, BaseProduct):
    """Класс для представления товара в магазине."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int, *args, **kwargs):
        """
        Инициализация экземпляра класса Product.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара
        """
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        """
        Сложение товаров с проверкой совместимости типов.
        Возвращает общую стоимость товаров одного типа
        """
        if type(other) != type(self):
            raise TypeError(
                f"Нельзя складывать товары разных типов: {type(self).__name__} и {type(other).__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

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
        if type(other) != type(self):
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
        if type(other) != type(self):
            raise TypeError("Можно складывать только газонную траву")
        return super().__add__(other)

    def __repr__(self):
        """
            Официальное строковое представление объекта

            Возвращает строку вида:
                Класс(name='название', price=цена, quantity=количество)
        """
        return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, quantity={self.quantity})"
