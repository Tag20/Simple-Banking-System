class Customer():
    def __init__(self):
        pass

    def get_details(self):
        self.name = input("Enter the name :")
        self.age = int(input("Enter the age :"))
        self.acc = int(input("Enter the account :"))
    def get_amount(self):
        self.amount = int(input("Enter the minium amount  of 500:"))
        return self.amount
            