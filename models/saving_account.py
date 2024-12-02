from models.account import Account
from utils.data_types import Money, InterestRate
from datetime import datetime, timedelta

from utils.transaction_log import Transaction

class SavingAccount(Account):
    def __init__(self, customer, balance=0, minimum_balance=100, interest_rate=0.02):
        super().__init__(customer, balance)
        self.minimum_balance = Money(minimum_balance)
        self.interest_rate = InterestRate(interest_rate)
        self.last_interest_date = datetime.now()

    def withdraw(self, amount, description="Withdrawal"):
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Cannot withdraw below minimum balance.")
        return super().withdraw(amount, description)

    def apply_interest(self):
        today = datetime.now()
        if today >= self.last_interest_date + timedelta(days=30):  # Monthly interest
            interest = self.balance * self.interest_rate
            self.balance += Money(interest)
            transaction = Transaction("interest", interest, self.balance, "Monthly interest applied")
            self.transactions.append(transaction)
            self.last_interest_date = today
            return transaction