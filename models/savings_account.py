from models.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0.0, min_balance=100.0, interest_rate=0.02):
        super().__init__(account_holder, initial_balance)
        self.min_balance = min_balance
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        """Withdraw only if balance stays above the minimum threshold."""
        if amount > 0 and self.balance - amount >= self.min_balance:
            self.balance -= amount
            self._log_transaction("Withdrawal", amount)
        elif amount > self.balance - self.min_balance:
            print(f"Cannot withdraw. Balance must remain above ${self.min_balance:.2f}.")
        else:
            print("Withdrawal amount must be positive.")

    def apply_interest(self):
        """Applies interest to the account balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction("Interest Applied", interest)

    def display_account_details(self):
        """Override to include minimum balance and interest rate in account details."""
        details = super().display_account_details()
        details["Minimum Balance"] = self.min_balance
        details["Interest Rate"] = self.interest_rate * 100
        return details