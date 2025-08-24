from credit import Credit
class Balance(Customer):
    def get_balance(self,amt):
        self.amt = amt
        return self.amt