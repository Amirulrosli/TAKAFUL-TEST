from datetime import datetime
import uuid
from utils.transaction_log import Transaction
from utils.data_types import Money, InterestRate

class Account:
    def __init__(self, customer, balance=0):
        self.account_id = str(uuid.uuid4())  # Generate unique account ID
        self.customer = customer
        self.balance = Money(balance)
        self.transactions = []  # List of Transaction objects
        self.created_date = datetime.now()

    def deposit(self, amount, description="Deposit"):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += Money(amount)
        transaction = Transaction("deposit", amount, self.balance, description)
        self.transactions.append(transaction)
        return transaction

    def withdraw(self, amount, description="Withdrawal"):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance >= amount:
            self.balance -= Money(amount)
            transaction = Transaction("withdrawal", amount, self.balance, description)
            self.transactions.append(transaction)
            return transaction
        else:
            raise ValueError("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def show_details(self):
        details = f"Account ID: {self.account_id}\nCustomer: {self.customer.firstname} {self.customer.surname}\n"
        details += f"Balance: ${self.balance:.2f}\nCreated: {self.created_date}\n"
        details += "Recent Transactions:\n"
        for transaction in self.transactions[-5:]:  # Show last 5 transactions
            details += f"  {transaction}\n"
        return details

    def transfer(self, target_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        self.withdraw(amount, description=f"Transfer to {target_account.account_id}")
        target_account.deposit(amount, description=f"Transfer from {self.account_id}")