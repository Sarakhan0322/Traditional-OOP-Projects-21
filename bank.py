class Bank:
    # Class variable
    bank_name = "ABC Bank"
    
    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
# Example usage:
# Create instances of Bank
bank1 = Bank()
bank2 = Bank()

# Display initial bank name for both instances
print(f"Bank 1 name: {bank1.bank_name}")
print(f"Bank 2 name: {bank2.bank_name}")

# Change the bank name using the class method
Bank.change_bank_name("XYZ Bank")

# Display updated bank name for both instances
print(f"Bank 1 name after change: {bank1.bank_name}")
print(f"Bank 2 name after change: {bank2.bank_name}")
