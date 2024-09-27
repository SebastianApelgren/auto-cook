class Ingredient:
    def __init__(self, name: str, quantity: str, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.quantity} of {self.name} - ${self.price:.2f}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def set_price(self, new_price):
        self.price = new_price

    def set_name(self, new_name):
        self.name = new_name
    
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return self.quantity