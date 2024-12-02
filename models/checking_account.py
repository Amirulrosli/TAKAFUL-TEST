from models.account import Account
from utils.data_types import Money
from utils.transaction_log import Transaction

class CheckingAccount(Account):
    def __init__(self, customer, balance=0, overdraft_limit=500):
        super().__init__(customer, balance)
        self.overdraft_limit = Money(overdraft_limit)

    def withdraw(self, amount, description="Withdrawal"):
        if self.balance + self.overdraft_limit < amount:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= Money(amount)
        transaction = Transaction("withdrawal", amount, self.balance, description)
        self.transactions.append(transaction)
        return transaction