import random

class BankAccount():
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.routing_number = 546325981
        self.balance = 0
    
    #add amount to balance
    def deposit(self, amount):
        self.balance += amount 
        print(f'Amount Deposited: ${amount}')
        self.get_balance()

    #subtracts amount from balance
    def withdraw(self, amount):
        if self.balance < amount: 
            print(f'- Insufficient funds -\n- Overdraft fee: $10 -')
            self.balance -= 10
        else: 
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}')

        self.get_balance()

    #print current balance and returns amount
    def get_balance(self):
        print(f'Balance: ${round(self.balance, 2)}')

    #calculates interest, 1%/yr
    def add_interest(self, months):
        for i in range(months):
            interest = round(self.balance * 0.00083, 2)
            self.balance += interest
        print(f'- Interest: 1% per year -\nTotal months of accrued interest: {str(months)}')
        
    def print_receipt(self):
        account_num_str = (str(self.account_number))[-4:]
        print("--------------------------------------------")
        print(self.full_name)
        print(f'Account No.: ****{account_num_str}')
        print(f'Routing No.: {self.routing_number}')
        self.get_balance()

johnny = BankAccount('Johnny Quinn', 54652321)
johnny.deposit(150)
johnny.add_interest(2)
johnny.print_receipt()
print('\n')

yoko = BankAccount('Yoko Quinn', 56873921)
yoko.deposit(7000)
yoko.withdraw(8000)
yoko.withdraw(560)
yoko.print_receipt()
print('\n')

aldo = BankAccount('Aldo Cabara', 78534602)
aldo.deposit(10000)
aldo.add_interest(24)
aldo.print_receipt()
