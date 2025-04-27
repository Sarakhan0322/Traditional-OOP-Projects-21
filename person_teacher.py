class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person's name is {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        # Use super() to call the base class constructor
        super().__init__(name)
        self.subject = subject
        print(f"Teacher's subject is {self.subject}")

# Example usage:
# Create an instance of Teacher, which will call the Person constructor via super()
teacher = Teacher("Arsala", "Mathematics")
