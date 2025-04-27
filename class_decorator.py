# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add greet() method to the class
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        return f"My name is {self.name}"

# Example usage
person = Person("John")
print(person.display_name())  # Output: My name is John
print(person.greet())         # Output: Hello from Decorator!
