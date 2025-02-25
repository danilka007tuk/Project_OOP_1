import pytest


def test_smartphone(smart_product):
    assert smart_product.name == "Samsung Galaxy S23 Ultra"
    assert smart_product.description == "256GB, Серый цвет, 200MP камера"
    assert smart_product.price == 180000.0
    assert smart_product.quantity == 5
    assert smart_product.efficiency == 95.5
    assert smart_product.model == "S23 Ultra"
    assert smart_product.memory == 256
    assert smart_product.color == "Серый"


def test_smartphone_2(smart_product_2):
    assert smart_product_2.name == "Iphone 15"
    assert smart_product_2.description == "512GB, Gray space"
    assert smart_product_2.price == 210000.0
    assert smart_product_2.quantity == 8
    assert smart_product_2.efficiency == 98.2
    assert smart_product_2.model == "15"
    assert smart_product_2.memory == 512
    assert smart_product_2.color == "Gray space"


def test_smart_add(smart_product, smart_product_2):
    assert (
        smart_product.price * smart_product.quantity
        + smart_product_2.quantity * smart_product_2.price
        == 2580000.0
    )


def test_smart_add_error(smart_product, smart_product_2):
    with pytest.raises(TypeError):
        assert smart_product + 1
