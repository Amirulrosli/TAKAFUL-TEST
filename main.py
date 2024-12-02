from models.bank import Bank
from models.customer import Customer, Contact
from models.address import Address

def main():
    # Step 1: Create the Bank
    bank = Bank("Global Bank")

    # Step 2: Create a Customer
    address = Address("Main St", "123", "56789", "Springfield")
    contact = Contact("123-4567", "987-6543", "customer@example.com", address)
    customer = bank.create_customer("John", "Doe", contact)

    # Step 3: Create Different Types of Accounts
    checking_account = bank.create_account("CheckingAccount", customer, initial_balance=500)
    savings_account = bank.create_account("SavingAccount", customer, initial_balance=1000)
    flexible_savings_account = bank.create_account("FlexibleSavingAccount", customer, initial_balance=2000)

    # Step 4: Test Checking Account
    print("Testing Checking Account:")
    checking_account.deposit(100)  # Deposit $100
    print(checking_account.show_details())

    try:
        checking_account.withdraw(700)  # Attempt withdrawal (should succeed)
    except ValueError as e:
        print(f"Error: {e}")
    print(checking_account.show_details())

    try:
        checking_account.withdraw(1000)  # Attempt overdraft (should fail)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n")

    # Step 5: Test Savings Account
    print("Testing Savings Account:")
    savings_account.deposit(200)  # Deposit $200
    print(savings_account.show_details())

    try:
        savings_account.withdraw(1100)  # Attempt withdrawal below minimum threshold
    except ValueError as e:
        print(f"Error: {e}")
    print(savings_account.show_details())

    # Apply interest
    savings_account.apply_interest()
    print(savings_account.show_details())
    print("\n")

    # Step 6: Test Flexible Savings Account
    print("Testing Flexible Savings Account:")
    flexible_savings_account.deposit(500)  # Deposit $500
    print(flexible_savings_account.show_details())

    try:
        flexible_savings_account.withdraw(1500)  # Attempt withdrawal with penalty
    except ValueError as e:
        print(f"Error: {e}")
    print(flexible_savings_account.show_details())

    # Apply interest
    flexible_savings_account.apply_interest()
    print(flexible_savings_account.show_details())
    print("\n")

    # Step 7: Test Transfers Between Accounts
    print("Testing Transfers:")
    print("Before Transfer:")
    print(f"Checking Account Balance: ${checking_account.get_balance()}")
    print(f"Flexible Savings Account Balance: ${flexible_savings_account.get_balance()}")

    try:
        bank.transfer(flexible_savings_account, checking_account, 500)  # Transfer $500
    except ValueError as e:
        print(f"Error: {e}")

    print("After Transfer:")
    print(f"Checking Account Balance: ${checking_account.get_balance()}")
    print(f"Flexible Savings Account Balance: ${flexible_savings_account.get_balance()}")
    print("\n")

    # Step 8: Show All Accounts
    print("All Accounts in the Bank:")
    print(bank.show_all_accounts())

if __name__ == "__main__":
    main()