from customer import Customer
class Debit(Customer):

    def get_debit(self,amt):
        self.d=int(input("Enter the amput to be credited :"))
        self.amt = amt - self.d
        return self.amt