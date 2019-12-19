class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.interest_rate = int_rate
        self.account_balance = balance

    #adding deposit method
    def deposit(self, amount):
        self.account_balance += amount
        return self
    #adding withdrawal method
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds: Charging a $5 fee.")
            self.account_balance -= 5.00
        else:
            self.account_balance -= amount
        return self
    #adding display account balance
    def display_account_info(self):
        print("Balance: $", self.account_balance)
        return self
    #add's interest rate to current balance
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * self.interest_rate)
            print("Interest of $", (self.account_balance * self.interest_rate),"was added to account")
        else:
            print("No interest as balance isn't positive")
        return self
