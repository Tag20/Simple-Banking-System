from customer import Customer
from credit import Credit
def main_menu():
    while True :
        print("*" * 10, "WELCOME TO NET BANKING", "*" * 10)

        print("1.ADD customer\n2.View Balance\n3.Credit\n4.Debit\n5.EXIT")
        choice = input("Enter the choice :")
        c = Customer()
        cr = Credit()
        if choice =='1':
            c.get_details()
            amt = c.get_amount()
        elif choice =='2':
            print("Balance In your account is ", cr.balance_amt(amt))
        elif choice =='3':
            print("Amount credited is ", cr.credit_amt(amt))
        elif choice =='4':
            print("Amount debited is", cr.debit_amt(amt))
        elif choice =='5':
            exit()
        else:
            print("Invali option")

        choice1 = input("Do you wish to continue ? {Y/N} ")
        if choice1 in ('y','Y'):
            continue
        else:
            print("thank Youfor banking ")
            break

main_menu()