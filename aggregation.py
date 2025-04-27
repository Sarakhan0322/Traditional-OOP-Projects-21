class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # A list to store multiple employees

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def show_employees(self):
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_info()

# Example usage:
# Create Employee objects
employee1 = Employee("Ali kasim", "Software Engineer")
employee2 = Employee("Sara Khan", "Project Manager")

# Create a Department object
department = Department("IT")

# Add employees to the department (aggregation: employees exist independently)
department.add_employee(employee1)
department.add_employee(employee2)

# Show all employees in the department
department.show_employees()
