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
