from typing import List
from src.main_14_1_product import Product


class Category:
    """Описание категории продуктов."""
    category_count = 0  # Сколько создано категорий
    product_count = 0   # Сколько всего товаров среди всех категорий
    name: str
    description: str
    __products: List[Product]  # Приватный атрибут для хранения товаров

    def __init__(self, name: str, description: str,
                 products: List[Product] = None):
        """Инициализация объекта категории."""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1  # Новая категория создана
        Category.product_count += len(self.__products)  # Новые товары

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        """Возвращает список товаров (не строку!)."""
        return self.__products

    def products_info(self) -> str:
        """Возвращает информацию о товарах в виде строки."""
        result = []
        for product in self.__products:
            line = (f"{product.name}, {product.price} руб. "
                    f"Остаток: {product.quantity} шт.")
            result.append(line)
        return "\n".join(result)
