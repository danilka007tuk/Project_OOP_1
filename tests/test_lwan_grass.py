import pytest


def test_lawn_grass(lawn_product):
    assert lawn_product.name == "Газонная трава"
    assert lawn_product.description == "Элитная трава для газона"
    assert lawn_product.price == 500.0
    assert lawn_product.quantity == 20
    assert lawn_product.country == "Россия"
    assert lawn_product.germination_period == "7 дней"
    assert lawn_product.color == "Зеленый"


def test_lawn_grass_2(lawn_product_2):
    assert lawn_product_2.name == "Газонная трава 2"
    assert lawn_product_2.description == "Выносливая трава"
    assert lawn_product_2.price == 450.0
    assert lawn_product_2.quantity == 15
    assert lawn_product_2.country == "США"
    assert lawn_product_2.germination_period == "5 дней"
    assert lawn_product_2.color == "Темно-зеленый"


def test_add_grass(lawn_product, lawn_product_2):
    assert (
        lawn_product.price * lawn_product.quantity
        + lawn_product_2.quantity * lawn_product_2.price
        == 16750.0
    )


def test_lawn_add_error(lawn_product, lawn_product_2):
    with pytest.raises(TypeError):
        assert lawn_product + 1
