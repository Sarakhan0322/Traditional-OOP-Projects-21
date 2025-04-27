from abc import ABC, abstractmethod

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Implementing the area method
    def area(self):
        return self.width * self.height

# Example usage:
# Create a Rectangle object
rect = Rectangle(5, 3)

# Call the area method
print(f"The area of the rectangle is: {rect.area()} square units.")
