import pytest

from src.product import Product


def test_product_1(product_name_1):
    assert product_name_1.name == "Samsung Galaxy S23 Ultra"
    assert product_name_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_name_1.price == 180000.0
    assert product_name_1.quantity == 5


def test_product_1_property(product_name_1):
    assert product_name_1.price == 180000.0


def test_product_2(product_name_2):
    assert product_name_2.name == "Iphone 15"
    assert product_name_2.description == "512GB, Gray space"
    assert product_name_2.price == 210000.0
    assert product_name_2.quantity == 8


def test_product_2_property(product_name_2):
    assert product_name_2.price == 210000.0


def test_product_3(product_name_3):
    assert product_name_3.name == "Xiaomi Redmi Note 11"
    assert product_name_3.description == "1024GB, Синий"
    assert product_name_3.price == 31000.0
    assert product_name_3.quantity == 14


def test_product_3_property(product_name_3):
    assert product_name_3.price == 31000.0


def test_product_4(product_name_4):
    assert product_name_4.name == '55" QLED 4K'
    assert product_name_4.description == "Фоновая подсветка"
    assert product_name_4.price == 123000.0
    assert product_name_4.quantity == 7


def test_product_4_property(product_name_4):
    assert product_name_4.price == 123000.0


def test_product_str(product_str):
    assert (
        str(product_str)
        == "Название продукта: Samsung Galaxy, 180000.0 руб. Остаток: 5шт."
    )


def test_len_add(product_name_1, product_name_2):
    assert (
        product_name_1.price * product_name_1.quantity
        + product_name_2.quantity * product_name_2.price
        == 2580000.0
    )


def test_product_invalid_raises_value_error():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_invalid_raises_value_error_2(product_invalid):
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product(*product_invalid)
