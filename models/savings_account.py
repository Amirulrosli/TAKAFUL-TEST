from models.account import Account

class SavingsAccount(Account):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Cannot withdraw: Minimum balance of ${self.MIN_BALANCE} required.")
        super().withdraw(amount)