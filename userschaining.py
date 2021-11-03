class User:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print("Cannot complete transaction.")
        return self
    def display_user_balance(self):
        print(f"Current Balance: {self.balance}")
        return self
    def transfer_money(self, other_user, amount):
        other_user.balance += amount
        self.balance -= amount
        print(f"{self.name}'s balance: {self.balance} {other_user.name}'s balance: {other_user.balance}")
        return self
john = User("John", 1000)
josh = User("Josh", 200)
tonya = User("Tonya", 9000)
john.make_deposit(900).make_deposit(20).make_deposit(400).make_withdrawal(920).display_user_balance()
josh.make_deposit(400).make_deposit(200).make_withdrawal(500).make_withdrawal(100).display_user_balance()
tonya.make_deposit(1).make_withdrawal(999).make_withdrawal(7000).make_withdrawal(1002).display_user_balance()
john.transfer_money(tonya, 1399)