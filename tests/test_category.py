from src.category import Category

def test_category_smartphones(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert (
        category_smartphones.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_smartphones.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_television(category_televisions):
    assert category_televisions.name == "Телевизоры"
    assert (
        category_televisions.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category_televisions.products) == 1
    assert Category.category_count == 2
    assert Category.product_count == 4


# def test_init(create_category):
#     assert create_category.name == "Электроника"
#     assert create_category.description == "Техника и гаджеты"
#     assert create_category._products == []
#     assert Category.category_count == 1
#     assert Category.product_count == 0
#
#
# def test_add_product(create_category, create_products):
#     create_category.add_product(create_products[0])
#     assert len(create_category._products) == 1
#     assert Category.product_count == 1
#
#     # Добавляем второй продукт
#     create_category.add_product(create_products[1])
#     assert len(create_category._products) == 2
#     assert Category.product_count == 2
#
#
# def test_get_product_info(create_category, create_products):
#     create_category.add_product(create_products[0])
#     expected_output = (
#         "Название продукта: Смартфон, 30000 руб. Остаток: 10 шт.\n"
#     )
#     assert create_category.get_product_info() == expected_output
#
#     create_category.add_product(create_products[1])
#     expected_output += (
#         "Название продукта: Ноутбук, 50000 руб. Остаток: 5 шт.\n"
#     )
#     assert create_category.get_product_info() == expected_output




#
# def test_category_product(category_product):
#     assert category_product.name == "Смартфоны"
#     assert (
#         category_product.description
#         == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
#     )
#     assert len(category_product.products) == 3
#     assert category_product.category_count == 1
#     assert category_product.product_count == 3
#
#
# def test_category_product_2(category_product_2):
#     assert category_product_2.name == "Телевизоры"
#     assert (
#         category_product_2.description
#         == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
#     )
#     assert len(category_product_2.products) == 1
#
# def test_category_products():
#     product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
#     task = Category("Телевизоры",
#         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                     [product4])
#     task.name = "Телевизоры"
#     task.description = "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
#     task.product = '55" QLED 4K', "Фоновая подсветка", 123000.0, 7