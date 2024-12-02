from models.checking_account import CheckingAccount
from models.savings_account import SavingsAccount

class BankAccountController:
    def __init__(self, view):
        self.view = view

    def create_checking_account(self, holder, initial_balance=0.0, overdraft_limit=500.0):
        return CheckingAccount(holder, initial_balance, overdraft_limit)

    def create_savings_account(self, holder, initial_balance=0.0, min_balance=100.0, interest_rate=0.02):
        return SavingsAccount(holder, initial_balance, min_balance, interest_rate)

    def deposit(self, account, amount):
        account.deposit(amount)

    def withdraw(self, account, amount):
        account.withdraw(amount)

    def transfer(self, from_account, to_account, amount):
        from_account.transfer(to_account, amount)

    def display_account(self, account):
        account_details = account.display_account_details()
        self.view.display_account_details(account_details)