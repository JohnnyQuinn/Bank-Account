class BankAccount():
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
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
            print(f'Insufficient funds.\n Overdraft fee: $10')
            self.balance -= 10
        else: 
            self.balance +- amount
            print(f'Amount Withdrawn: ${amount}')

        self.get_balance()

    #print current balance and returns amount
    def get_balance(self):
        return f'${self.balance}'

    #calculates interest, 1%/yr
    def add_interest(self):
        interest = round(self.balance * 0.00083, 2)
        self.balance += interest

    def print_receipt(self):
        account_num_str = (str(self.account_number))[-5:]
        print("--------------------------------------------")
        print(self.full_name)
        print(f'Account No.: ****{account_num_str}')
        print(f'Routing No.: {self.routing_number}')
        print(f'Balance: {self.get_balance()}')

johnny = BankAccount('Johnny Quinn', 5465231)
johnny.deposit(150)
johnny.add_interest()
johnny.print_receipt()