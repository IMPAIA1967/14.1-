

from src.main_14_1_product import Product
from src.main_14_1_category import Category


class TestProduct:
    """Проверка инициализации Product."""

    def test_product_initialization(self):
        p = Product("Телефон", "Описание", 999.99, 10)
        assert p.name == "Телефон"
        assert p.description == "Описание"
        assert p.price == 999.99
        assert p.quantity == 10


class TestCategory:
    """Проверка инициализации Category и счётчиков."""

    def setup_method(self):
        """Сброс счётчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        prod1 = Product("Телефон", "Описание", 999.99, 10)
        prod2 = Product("Наушники", "Описание", 199.99, 5)
        cat = Category("Электроника", "Гаджеты", [prod1, prod2])

        assert cat.name == "Электроника"
        assert cat.description == "Гаджеты"
        assert len(cat.products) == 2

    def test_category_product_counters(self):
        prod1 = Product("Товар 1", "Описание", 1.0, 1)
        prod2 = Product("Товар 2", "Описание", 2.0, 2)

        # Создаем первую категорию
        Category("Кат 1", "Описание", [prod1])
        assert Category.category_count == 1
        assert Category.product_count == 1

        # Создаем вторую категорию
        Category("Кат 2", "Описание", [prod1, prod2])
        assert Category.category_count == 2
        assert Category.product_count == 3


class TestProductAdditional:
    """Дополнительные тесты для Product."""

    def test_price_setter(self):
        """Тест изменения цены через сеттер."""
        p = Product("Телефон", "Описание", 1000, 5)
        p.price = 1200
        assert p.price == 1200

    def test_negative_price(self):
        """Тест на отрицательную цену."""
        p = Product("Телефон", "Описание", 1000, 5)
        p.price = -500  # Должно остаться 1000 и вывести сообщение об ошибке
        assert p.price == 1000


class TestCategoryAdditional:
    """Дополнительные тесты для Category."""

    def setup_method(self):
        """Сброс счётчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_empty_category(self):
        """Тест создания пустой категории."""
        cat = Category("Пустая", "Категория без товаров")
        assert len(cat.products) == 0
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_add_product(self):
        """Тест добавления товара в категорию."""
        cat = Category("Техника", "Электроника")
        p = Product("Планшет", "Описание", 500, 3)
        cat.add_product(p)
        assert len(cat.products) == 1
        assert Category.category_count == 1
        assert Category.product_count == 1

    def test_product_addition(self):
        """Тестирование сложения двух продуктов"""
        # Создаем тестовые продукты
        product1 = Product("Телефон", "Смартфон", 10000, 5)  # 10000 * 5 = 50000
        product2 = Product("Ноутбук", "Игровой", 50000, 2)  # 50000 * 2 = 100000

        # Проверяем сложение
        assert product1 + product2 == 150000  # 50000 + 100000
        assert product2 + product1 == 150000

    def test_product_str_representation(self):
        """Тестирование строкового представления продукта"""
        product = Product("Телефон", "Смартфон", 25000, 15)
        assert str(product) == "Телефон, 25000 руб. Остаток: 15 шт."

    def test_category_str_representation(self):
        """Тестирование строкового представления категории"""
        # 1. Создаем тестовые продукты
        product1 = Product("Телефон", "Смартфон", 25000, 10)
        product2 = Product("Ноутбук", "Игровой", 50000, 5)

        # 2. Создаем категорию с этими продуктами
        category = Category("Электроника", "Техника", [product1, product2])

        # 3. Проверяем строковое представление
        assert str(category) == "Электроника, количество продуктов: 15 шт."