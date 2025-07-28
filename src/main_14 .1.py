from typing import List


class Product:
    """Описание продукта."""
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация объекта продукта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Описание продукта."""
    category_count = 0  # Сколько создано категорий
    products_count = 0  # Сколько всего товаров среди всех категорий
    name: str
    description: str
    products: List[Product]


    def __init__(self, name: str, description: str, products: List[Product]):
        """Инициализация объекта продукта."""
        self.name = name
        self.description = description
        self.products = products


        Category.category_count += 1                   # Новая категория создана
        Category.products_count += len(products) # Новые товары добавились в общий счётчик