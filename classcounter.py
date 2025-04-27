class Counter:
    # Class variable to keep track of the count
    count = 0
    
    def __init__(self):
        # Increment the count each time a new object is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        # Class method to display the count of objects created
        print(f"Number of objects created: {cls.count}")
        
# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the count of objects created
Counter.display_count()
