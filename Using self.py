# Define the Student class
class Student:
    # Constructor to initialize the name and marks attributes using 'self'
    def __init__(self, name, marks):
        self.name = name  # Initialize name
        self.marks = marks  # Initialize marks

    # Method to display student details
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
# Create student objects and pass the name and marks to the constructor

# Student 1
student1 = Student("Arsala", 95)
# Call the display method to show student 1 details
student1.display()

# Student 2
student2 = Student("Ali", 88)
# Call the display method to show student 2 details
student2.display()
