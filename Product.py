class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

# Creating an instance of the Product class
product_instance = Product(name="Laptop", price=1200.0, quantity=2)

print(f"Product Name: {product_instance.name}")
print(f"Price per unit: ${product_instance.price}")
print(f"Quantity: {product_instance.quantity}")
print(f"Total cost: ${product_instance.calculate_total()}")
