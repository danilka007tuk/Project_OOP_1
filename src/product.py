class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params):
        return cls(
            params["name"], params["description"], params["price"], params["quantity"]
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    #
    # @classmethod
    # def new_product(cls, product_info):
    #     return cls(
    #         name=product_info["name"],
    #         price=product_info["price"],
    #         description=product_info["description"],
    #         quantity=product_info["quantity"],
    #     )
    #
    # @property
    # def price(self):
    #     return self.__price
    #
    # @price.setter
    # def price(self, new_price: float):
    #     if new_price <= 0:
    #         print("Цена не должна быть нулевая или отрицательная")
    #         return
    #     self.__price = new_price
    #
    # @property
    # def price_list(self):
    #     return self.__price
    #
    # def __str__(self):
    #     return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
