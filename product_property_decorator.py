class Product:
    def __init__(self, price):
        self._price = price  # Private attribute
    
    # Getter for the price
    @property
    def price(self):
        return self._price
    
    # Setter for the price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value
    
    # Deleter for the price
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
product = Product(100)

# Accessing price using the getter
print("Price:", product.price)  # Calls the getter

# Updating price using the setter
product.price = 150
print("Updated Price:", product.price)

# Trying to set a negative price
product.price = -50  # Will trigger the validation in setter

# Deleting price using the deleter
del product.price  # Calls the deleter
