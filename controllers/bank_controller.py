from models.bank import Bank
from models.data_types import Money, InterestRate, Period
from models.child_account_classes import CheckingAccount, SavingAccount, FlexibleSavingAccount

class BankController:
    def __init__(self, bank: Bank):
        self.bank = bank

    def create_account(self, name: str, account_type: str, initial_balance: float, interest_rate: float, interest_period: str, overdraft_limit: float = 500.0, min_balance: float = 100.0):
        balance = Money(initial_balance)
        rate = InterestRate(interest_rate)
        period = Period(interest_period)

        if account_type == "checking":
            overdraft = Money(overdraft_limit)
            account = CheckingAccount(name, balance, rate, period, overdraft)
        elif account_type == "savings":
            min_balance = Money(min_balance)
            account = SavingAccount(name, balance, rate, period, min_balance)
        elif account_type == "flexible_savings":
            account = FlexibleSavingAccount(name, balance, rate, period)
        else:
            raise ValueError("Invalid account type.")

        self.bank.add_account(account)

    def list_accounts(self):
        return self.bank.list_accounts()