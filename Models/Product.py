class Product:
    def __init__(self, name: str, price: float):
      
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
