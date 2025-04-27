class MathUtils:
    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b
        
# Example usage:
# Call the static method without creating an instance
result = MathUtils.add(5, 3)

# Display the result
print(f"The sum is: {result}")
