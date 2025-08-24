from customer import Customer
class Credit(Customer):

    def get_credit(self,amt):
        self.a=int(input("Enter the amput to be credited :"))
        self.amt = self.a + amt
        return self.amt