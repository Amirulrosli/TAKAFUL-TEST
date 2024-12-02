import datetime

class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self.account_id = self.generate_account_id()
        self.creation_date = datetime.datetime.now()

    def generate_account_id(self):
        """Generate a unique account ID."""
        return f"{self.account_holder[:3].upper()}{int(datetime.datetime.now().timestamp())}"

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            self._log_transaction("Deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account."""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self._log_transaction("Withdrawal", amount)
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Returns the current balance."""
        return self.balance

    def _log_transaction(self, transaction_type, amount):
        """Logs each transaction (deposit/withdrawal)."""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transaction_history.append({
            'transaction_type': transaction_type,
            'amount': amount,
            'timestamp': timestamp
        })

    def transfer(self, target_account, amount):
        """Transfers a specified amount to another BankAccount."""
        if self.balance >= amount:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Successfully transferred ${amount:.2f} to {target_account.account_holder}.")
        else:
            print("Insufficient funds for transfer.")

    def display_account_details(self):
        """Returns account details in a dictionary (for view)."""
        return {
            "Account ID": self.account_id,
            "Account Holder": self.account_holder,
            "Balance": self.balance,
            "Account Creation Date": self.creation_date.strftime('%Y-%m-%d %H:%M:%S'),
            "Transaction History": self.transaction_history
        }