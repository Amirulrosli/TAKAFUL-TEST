from models.bank import Bank
from models.checking_account import CheckingAccount
from models.savings_account import SavingsAccount
from models.flexible_savings_account import FlexibleSavingsAccount
from views.bank_view import BankView

class BankController:
    def __init__(self, bank_name):
        self.bank = Bank(bank_name)
        self.view = BankView()

    def create_account(self, account_type, holder_name, balance=0):
        if account_type == "checking":
            account = CheckingAccount(holder_name, balance)
        elif account_type == "savings":
            account = SavingsAccount(holder_name, balance)
        elif account_type == "flexible_savings":
            account = FlexibleSavingsAccount(holder_name, balance)
        else:
            raise ValueError("Invalid account type.")
        self.bank.create_account(account)
        self.view.display_message(f"Account created for {holder_name}.")

    def list_accounts(self):
        accounts = self.bank.list_accounts()
        self.view.display_accounts(accounts)

    def deposit(self, account_index, amount):
        try:
            account = self.bank.accounts[account_index]
            account.deposit(amount)
            self.view.display_message(f"Deposited ${amount} to {account.account_holder}'s account.")
        except Exception as e:
            self.view.display_message(str(e))

    def withdraw(self, account_index, amount):
        try:
            account = self.bank.accounts[account_index]
            account.withdraw(amount)
            self.view.display_message(f"Withdrew ${amount} from {account.account_holder}'s account.")
        except Exception as e:
            self.view.display_message(str(e))