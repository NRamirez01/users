class User:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print("Cannot complete transaction.")
    def display_user_balance(self):
        print(f"Current Balance {self.balance}")
    def transfer_money(self, other_user, amount):
        other_user.balance += amount
        self.balance -= amount
        print(f"{self.name}'s balance: {self.balance} {other_user.name}'s balance: {other_user.balance}")
john = User("John", 1000)
josh = User("Josh", 200)
tonya = User("Tonya", 9000)
john.make_deposit(900)
john.make_deposit(20)
john.make_deposit(400)
john.make_withdrawal(920)
john.display_user_balance()
josh.make_deposit(400)
josh.make_deposit(200)
josh.make_withdrawal(500)
josh.make_withdrawal(100)
josh.display_user_balance()
tonya.make_deposit(1)
tonya.make_withdrawal(999)
tonya.make_withdrawal(7000)
tonya.make_withdrawal(1002)
tonya.display_user_balance()
john.transfer_money(tonya, 1399)