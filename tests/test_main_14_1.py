from src.main_14_1 import Product, Category


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
