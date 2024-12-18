from Models.Product import Product
from Services.CoffeeShop import CoffeeShop

coffee_shop = CoffeeShop()

coffee = Product("Café Expresso", 1.5)

stock = coffee_shop.stock
stock.add_product(coffee, 10)


coffee_shop.create_order()
order = coffee_shop.current_order
order.add_to_order(coffee, 5, stock)


print("Total de la commande :", order.calculate_total(), "€")


coffee_shop.serve_order()
