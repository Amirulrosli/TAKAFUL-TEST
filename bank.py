import datetime

# Base class for BankAccount
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
    
    def display_account_details(self):
        """Displays account details in a user-friendly format."""
        print(f"Account ID: {self.account_id}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Account Creation Date: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"  {transaction['timestamp']} - {transaction['transaction_type']}: ${transaction['amount']:.2f}")
    
    def transfer(self, target_account, amount):
        """Transfers a specified amount to another BankAccount."""
        if self.balance >= amount:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Successfully transferred ${amount:.2f} to {target_account.account_holder}.")
        else:
            print("Insufficient funds for transfer.")
        

# CheckingAccount subclass (inherits from BankAccount)
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
        """Overrides to include overdraft limit in account details."""
        super().display_account_details()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")


# SavingsAccount subclass (inherits from BankAccount)
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
        """Overrides to include minimum balance and interest rate in account details."""
        super().display_account_details()
        print(f"Minimum Balance: ${self.min_balance:.2f}")
        print(f"Interest Rate: {self.interest_rate * 100:.2f}%")

# Testing the BankAccount system
if __name__ == "__main__":
    # Creating checking and savings accounts
    john_checking = CheckingAccount("John Doe", 2000.0)
    jane_savings = SavingsAccount("Jane Smith", 1500.0, min_balance=200.0, interest_rate=0.03)

    # Perform operations
    john_checking.deposit(500)
    john_checking.withdraw(700)
    john_checking.transfer(jane_savings, 200)

    jane_savings.apply_interest()
    jane_savings.withdraw(1500)  # Should trigger min balance warning

    # Display account details
    john_checking.display_account_details()
    jane_savings.display_account_details()