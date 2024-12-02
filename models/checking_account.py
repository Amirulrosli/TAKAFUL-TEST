from models.bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0.0, overdraft_limit=500.0):
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Withdraw with overdraft protection."""
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            self._log_transaction("Withdrawal", amount)
        elif amount > self.balance + self.overdraft_limit:
            print("Insufficient funds, even with overdraft protection.")
        else:
            print("Withdrawal amount must be positive.")

    def display_account_details(self):
        """Override to include overdraft limit in account details."""
        details = super().display_account_details()
        details["Overdraft Limit"] = self.overdraft_limit
        return details