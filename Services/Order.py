class Order:
    def __init__(self):
     
        self.items = []

    def add_to_order(self, product, quantity: int, stock):
    
        if stock.check_stock(product, quantity):
            self.items.append((product, quantity))
        else:
            raise ValueError("Stock insuffisant pour ajouter : {}".format(product.get_name()))

    def calculate_total(self) -> float:
     
        return sum(product.get_price() * quantity for product, quantity in self.items)

    def get_items(self):
        return self.items
