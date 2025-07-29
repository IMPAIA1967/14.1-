from typing import Optional

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
        self.quantity = quantit
