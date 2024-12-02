class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.statements = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self._add_statement(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self._add_statement(f"Withdrew: ${amount}")

    def get_balance(self):
        return self.balance

    def _add_statement(self, content):
        self.statements.append(content)

    def __str__(self):
        return f"{self.account_holder} - Balance: ${self.balance}"