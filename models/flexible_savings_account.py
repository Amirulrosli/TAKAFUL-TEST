from models.savings_account import SavingsAccount

class FlexibleSavingsAccount(SavingsAccount):
    def apply_interest(self, rate):
        if rate <= 0:
            raise ValueError("Interest rate must be positive.")
        interest = self.balance * rate
        self.deposit(interest)