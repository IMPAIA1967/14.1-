

def test_product_initialization(self):
    """ Проверка правильной инициализации товара. """
    product = Product("Телефон", "Смартфон последней модели", 999.99, 10)

    # Проверяем правильность значений полей
    self.assertEqual(product.name, "Телефон")
    self.assertEqual(product.description, "Смартфон последней модели")
    self.assertEqual(product.price, 999.99)
    self.assertEqual(product.quantity, 10)


def test_category_initialization_and_counts(self):
    """ Проверка правильности инициализации категории и верности изменения глобальных счетчиков. """
    # Инициализируем продукты
    product1 = Product("Ноутбук", "Мощный ноутбук", 1499.99, 5)
    product2 = Product("Монитор", "Большой монитор Full HD", 799.99, 8)

    # Инициализируем категорию
    category = Category("Электроника", "Категория электроники", [product1, product2])

    # Проверяем название и описание категории
    self.assertEqual(category.name, "Электроника")
    self.assertEqual(category.description, "Категория электроники")

    # Проверяем наличие двух продуктов в списке
    self.assertListEqual(category.products, [product1, product2])

    # Категория должна создать новый объект, увеличив count на единицу
    self.assertEqual(Category.category_count, 1)

    # Должно учитываться количество товаров в общей сумме
    self.assertEqual(Category.products_count, 2)


if __name__ == '__main__':
    unittest.main()