class BankAccount():
    def __init__(self, full_name, account_number)
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = 0
        self.balance = 0
    
    #add amount to balance
    def deposit(self, amount):
        self.balance += amount 
        print(f'Amount Deposited: ${amount}')
        get_balance()

    #subtracts amount from balance
    def withdraw(self, amount):
        if self.balance < amount 
            print(f'Insufficient funds.\n Overdraft fee: $10')
            self.balance -= 10
        else 
            self.balance +- amount
            print(f'Amount Withdrawn: ${amount}')

        get_balance()

    #print current balance and returns amount
    def get_balance(self):
        print(f'Your current balance is {self.balance}')  
        return self.balance   

    #calculates interest, 1%/yr
    def add_interest(self):
        interest = self.balance * 0.00083

    def print_receipt(self):
        print full_name
        print(f'Account No.: ****{account_number[-5]}')
        print(f'Routing No.: {routing_number}')
