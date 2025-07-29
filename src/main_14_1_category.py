from typing import List
from main_14_1_product import Product

class Category:
    """Описание категории продуктов."""
    category_count = 0  # Сколько создано категорий
    product_count = 0   # Сколько всего товаров среди всех категорий
    name: str
    description: str
    products: List[Product]

    def __init__(self, name: str, description: str, products: List[Product]):
        """Инициализация объекта категории."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1           # Создана новая категория
        Category.product_count += len(products)  # Добавлены новые товары