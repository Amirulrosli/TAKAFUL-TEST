from models.account import Account

class CheckingAccount(Account):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = 500

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Cannot withdraw: Overdraft limit exceeded.")
        super().withdraw(amount)