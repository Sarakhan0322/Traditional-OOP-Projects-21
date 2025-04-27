class Employee:
    # Public variable
    name = "John Doe"
    
    # Protected variable
    _salary = 50000
    
    # Private variable
    __ssn = "123-45-6789"
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
        
# Example usage:
# Create an instance of the Employee class
emp = Employee()

# Accessing public variable (name) is allowed
print(f"Employee name: {emp.name}")

# Accessing protected variable (_salary) is allowed but it's a convention to not access directly
print(f"Employee salary: {emp._salary}")

# Accessing private variable (__ssn) directly is not allowed, will raise an error
# Uncomment the following line to see the error
# print(f"Employee SSN: {emp.__ssn}")  # This will raise an AttributeError

# Accessing private variable via name mangling
print(f"Employee SSN (using name mangling): {emp._Employee__ssn}")
