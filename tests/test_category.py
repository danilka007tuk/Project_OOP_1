from src.category import Category


def test_category_product(category_product):
    assert category_product.name == "Смартфоны"
    assert (
        category_product.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_product.products_list) == 3
    assert category_product.category_count == 1
    assert category_product.product_count == 3


def test_category_product_2(category_product_2):
    assert category_product_2.name == "Телевизоры"
    assert (
        category_product_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category_product_2.products_list) == 1


def test_category_len(category_len):
    assert (
        str(category_len)
        == "Название категории: Смартфоны, количество продуктов: 3 шт."
    )
    assert len(category_len.products) == 202


def test_product_len_price(product_name_1, product_name_2, product_name_3):
    category1 = Category(
        "Смартфоны",
        "Категория смартфонов",
        [product_name_1, product_name_2, product_name_3],
    )
    assert category1.middle_price() == 140333.33333333334


def test_product_len_price_null(product_name_1, product_name_2, product_name_3):
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
