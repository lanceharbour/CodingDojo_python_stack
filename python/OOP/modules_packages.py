from bankaccount import BankAccount
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

tuser1 = User("Test User1","Tuser1@gmail.com")
tuser2 = User("Test User2","Tuser2@gmail.com")
tuser3 = User("Test User3","Tuser3@gmail.com")

tuser1.account.deposit(200)
tuser1.account.yield_interest().display_account_info()
print(tuser3.name)
tuser3.account.deposit(450).withdraw(74).display_account_info()

tuser1.account.display_account_info()
tuser2.account.display_account_info()

