class Car:
    # Public variable
    brand = "Toyota"
    
    # Public method
    def start(self):
        print(f"The {self.brand} car has started.")
        
# Example usage:
# Instantiate the Car class
my_car = Car()

# Access the public variable
print(f"Car brand: {my_car.brand}")

# Call the public method
my_car.start()
