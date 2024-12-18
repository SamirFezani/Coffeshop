from Services.Stock import Stock
from Services.Order import Order

class CoffeeShop:
    def __init__(self):
      
        self.stock = Stock()
        self.current_order = None

    def create_order(self):
       
        self.current_order = Order()

    def serve_order(self):
      
        if not self.current_order:
            raise ValueError("Aucune commande à servir.")
        
        for product, quantity in self.current_order.get_items():
            self.stock.remove_product(product, quantity)

        total = self.current_order.calculate_total()
        print(f"Commande servie. Total à payer : {total} €")
        self.current_order = None
