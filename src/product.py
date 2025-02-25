class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        return f"Название продукта: {self.name}, {self.price} руб. Остаток: {self.quantity}шт."

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self._price * self.quantity + other._price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, params):
        return cls(
            params["name"], params["description"], params["price"], params["quantity"]
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value
