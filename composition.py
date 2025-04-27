class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine
    
    def start_engine(self):
        print(f"The {self.type_of_engine} engine is now running.")

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Engine object is passed to the Car class
    
    def start_car(self):
        print(f"{self.make} {self.model} is starting...")
        self.engine.start_engine()  # Access Engine's method via Car

# Example usage:
# Create an Engine object
engine = Engine("V8")

# Create a Car object, passing the Engine object to the Car
my_car = Car("Ford", "Mustang", engine)

# Start the car (which calls the Engine's start_engine method)
my_car.start_car()
