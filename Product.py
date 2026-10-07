class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount

product1 = Product("Laptop", 1200)
product2 = Product("Headphones", 150)

product1.apply_discount(10)
product2.apply_discount(20)

print(f"Final price of {product1.name}: ${product1.price:.2f}")
print(f"Final price of {product2.name}: ${product2.price:.2f}") 
