class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed
    
    # Instance method to print a bark message
    def bark(self):
        print(f"{self.name} says woof!")

# Example usage:
# Create an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Call the bark method
my_dog.bark()
