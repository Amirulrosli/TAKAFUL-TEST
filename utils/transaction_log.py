from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount, balance_after, description=""):
        self.transaction_type = transaction_type  # 'deposit', 'withdrawal', or 'transfer'
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()
        self.description = description

    def __str__(self):
        return f"[{self.timestamp}] {self.transaction_type.capitalize()}: ${self.amount:.2f} | Balance: ${self.balance_after:.2f} | {self.description}"