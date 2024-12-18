class Stock:
    def __init__(self):
      
        self.products = {}

    def add_product(self, product, quantity: int):
    
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def check_stock(self, product, quantity: int) -> bool:
    
        return self.products.get(product, 0) >= quantity

    def remove_product(self, product, quantity: int):
      
        if self.check_stock(product, quantity):
            self.products[product] -= quantity
            if self.products[product] == 0:
                del self.products[product]
        else:
            raise ValueError("Stock insuffisant pour le produit : {}".format(product.get_name()))
