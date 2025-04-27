class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize with the starting number
    
    # __iter__ method to return the iterator object itself
    def __iter__(self):
        self.current = self.start  # Set the current value to start
        return self
    
    # __next__ method to return the next value in the countdown
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration when we reach 0 or below
        self.current -= 1
        return self.current

# Example usage
countdown = Countdown(5)

# Using Countdown object in a for-loop
for number in countdown:
    print(number)
