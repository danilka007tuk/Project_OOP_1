class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавление продукта в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_list(self):
        return self.__products

    @property
    def products(self):
        product_list = [
            f"Название продукта: {p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        ]
        return "\n".join(product_list)

    # def get_product_info(self):
    #     result = ""
    #     for product in self.__products:
    #         result += f"Название продукта: {product.name}, {product.price} руб. Остаток:{product.quantity} шт.\n"
    #     return result

    # @property
    # def products(self):
    #     products_str = ""
    #     for product in self.__products:
    #   products_str += f"Название продукта: {product.name}, {product.price} руб. Остаток:{product.quantity} шт.\n"
    #     return products_str
    #
    # def add_product(self, product):
    #     """Добавление продукта в категорию"""
    #     self.__products.append(product)  # Доступ к приватному атрибуту внутри класса
    #     Category.product_count += 1

    #
    # def add_product(self, product):
    #     """Добавление продукта в категорию"""
    # self.__products.append(product)
    # Category.product_count += 1
    #
    #
    # @property
    # def products(self):
    #     products_str = ""
    #     for product in self.__products:
    #    products_str += f"Название продукта: {product.name}, {product.price} руб. Остаток:{product.quantity} шт.\n"
    #     return products_str
    #
    # @products.setter
    # def products(self, product: Product):
    #     self.__products.append(product)
    #     Category.product_count += 1
