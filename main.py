from controllers.bank_account_controller import BankAccountController
from views.bank_account_view import BankAccountView

def main():
    # Create View and Controller instances
    view = BankAccountView()
    controller = BankAccountController(view)

    # Create accounts
    john_checking = controller.create_checking_account("John Doe", 2000.0)
    jane_savings = controller.create_savings_account("Jane Smith", 1500.0, min_balance=200.0, interest_rate=0.03)

    # Perform operations
    controller.deposit(john_checking, 500)
    controller.withdraw(john_checking, 700)
    controller.transfer(john_checking, jane_savings, 200)

    jane_savings.apply_interest()
    controller.withdraw(jane_savings, 1500)  # Should trigger min balance warning

    # Display account details
    controller.display_account(john_checking)
    controller.display_account(jane_savings)

if __name__ == "__main__":
    main()