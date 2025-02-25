from src.product import Product


class Smartphone(Product):
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self._price * self.quantity + other._price * other.quantity
        raise TypeError


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self._price * self.quantity + other._price * other.quantity
        raise TypeError

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
