class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Initialize with the factor
    
    # Define __call__() to make the object callable
    def __call__(self, value):
        return value * self.factor

# Example usage
multiplier = Multiplier(5)

# Test using callable()
print("Is multiplier callable?", callable(multiplier))  # Should return True

# Calling the object like a function
result = multiplier(10)  # Calls the __call__() method with 10 as the argument
print("Result of multiplying 10 by factor:", result)  # Output: 50
