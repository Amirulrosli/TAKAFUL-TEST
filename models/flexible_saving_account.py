from models.saving_account import SavingAccount
from utils.data_types import Money, InterestRate
from datetime import datetime, timedelta

from utils.transaction_log import Transaction

class FlexibleSavingAccount(SavingAccount):
    def __init__(self, customer, balance=0, minimum_balance=100, base_interest_rate=0.01, bonus_interest_rate=0.02):
        """
        A flexible savings account with a base interest rate and an additional bonus interest rate 
        for higher balances.
        """
        super().__init__(customer, balance, minimum_balance, interest_rate=base_interest_rate)
        self.bonus_interest_rate = InterestRate(bonus_interest_rate)
        self.bonus_threshold = Money(1000)  # Apply bonus interest if balance exceeds this amount

    def apply_interest(self):
        """Apply interest to the account balance. Bonus interest is applied if balance exceeds the threshold."""
        today = datetime.now()
        if today >= self.last_interest_date + timedelta(days=30):  # Monthly interest application
            # Determine applicable interest rate
            applicable_rate = (
                self.bonus_interest_rate
                if self.balance > self.bonus_threshold
                else self.interest_rate
            )
            
            # Calculate interest
            interest = self.balance * applicable_rate
            self.balance += Money(interest)
            
            # Log the interest application
            transaction = Transaction("interest", interest, self.balance, "Monthly interest applied (Flexible)")
            self.transactions.append(transaction)
            
            # Update the last interest application date
            self.last_interest_date = today
            return transaction
        return None

    def withdraw(self, amount, description="Withdrawal"):
        """
        Allows withdrawal as long as the minimum balance requirement is met,
        but deducts a penalty fee if the balance falls below a certain threshold.
        """
        penalty_fee = Money(10)
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Cannot withdraw below the minimum balance.")
        
        # Apply penalty fee if withdrawing results in balance below bonus threshold
        if self.balance - amount < self.bonus_threshold:
            print(f"Penalty Fee of ${penalty_fee:.2f} will be applied for this withdrawal.")
            amount += penalty_fee
        
        return super().withdraw(amount, description)

    def show_details(self):
        """Display detailed information about the flexible savings account."""
        details = super().show_details()
        details += f"Bonus Interest Rate: {self.bonus_interest_rate:.2%}\n"
        details += f"Bonus Threshold: ${self.bonus_threshold:.2f}\n"
        return details