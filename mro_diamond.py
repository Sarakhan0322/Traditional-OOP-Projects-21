class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):  # Inheriting from both B and C
    pass

# Example usage:
# Create an object of class D
obj = D()

# Call the show() method
obj.show()
