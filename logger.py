class Logger:
    # Constructor
    def __init__(self):
        print("Logger object created.")
    
    # Destructor
    def __del__(self):
        print("Logger object destroyed.")
        
# Example usage:
# Create an instance of Logger (this will trigger the constructor)
logger1 = Logger()

# Delete the instance (this will trigger the destructor)
del logger1
