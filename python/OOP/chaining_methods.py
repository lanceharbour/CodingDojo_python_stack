class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    #adding deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    #adding withdrawal metho
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    #adding display balance method
    def display_user_balance(self):
        print(self.name, "your account balance is $",self.account_balance)
        return self
    #adding transfer method
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(self.name, "you transfered $", amount, "to ",other_user.name)
        return self
        
tuser1 = User("Test User1","Tuser1@gmail.com")
tuser2 = User("Test User2","Tuser2@gmail.com")
tuser3 = User("Test User3","Tuser3@gmail.com")

tuser1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

tuser2.make_deposit(200).make_deposit(174).make_withdrawal(90).make_withdrawal(200).display_user_balance()

tuser3.make_deposit(500).make_withdrawal(20).make_withdrawal(100).make_withdrawal(75).display_user_balance()

tuser1.transfer_money(tuser2,50).display_user_balance()
tuser2.display_user_balance()