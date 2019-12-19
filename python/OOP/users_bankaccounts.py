class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

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
    # #adding transfer method
    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount
    #     other_user.user.account.account_balance += amount
    #     print(self, "you transfered $", amount, "to ",other_user.name)

tuser1 = User("Test User1","Tuser1@gmail.com")
tuser2 = User("Test User2","Tuser2@gmail.com")
tuser3 = User("Test User3","Tuser3@gmail.com")

tuser1.account.deposit(200)
tuser1.account.yield_interest().display_account_info()

tuser1.account.display_account_info()
tuser2.account.display_account_info()
