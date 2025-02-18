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

    def __str__(self):
        return f"Название категории: {self.name}, количество продуктов: {len(self.__products)} шт."

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
