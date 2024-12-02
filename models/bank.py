from models.saving_account import SavingAccount
from models.checking_account import CheckingAccount
from models.flexible_saving_account import FlexibleSavingAccount
from models.customer import Customer

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []  # List of all accounts in the bank
        self.customers = []  # List of customers in the bank

    def create_customer(self, firstname, surname, contact):
        """Create a new customer and add them to the bank."""
        customer = Customer(firstname, surname, contact)
        self.customers.append(customer)
        return customer

    def create_account(self, account_type, customer, initial_balance=0):
        """Create a new account for a customer."""
        if account_type == "SavingAccount":
            account = SavingAccount(customer, balance=initial_balance)
        elif account_type == "CheckingAccount":
            account = CheckingAccount(customer, balance=initial_balance)
        elif account_type == "FlexibleSavingAccount":
            account = FlexibleSavingAccount(customer, balance=initial_balance)
        else:
            raise ValueError(f"Unsupported account type: {account_type}")

        self.accounts.append(account)
        return account

    def get_customer_accounts(self, customer):
        """Retrieve all accounts associated with a specific customer."""
        return [account for account in self.accounts if account.customer == customer]

    def transfer(self, from_account, to_account, amount):
        """Transfer funds between two accounts."""
        from_account.transfer(to_account, amount)

    def show_all_accounts(self):
        """Display details of all accounts in the bank."""
        details = f"Bank: {self.name}\nTotal Accounts: {len(self.accounts)}\n\n"
        for account in self.accounts:
            details += f"{account.show_details()}\n"
        return details

    def apply_monthly_interest(self):
        """Apply interest to all saving accounts."""
        for account in self.accounts:
            if isinstance(account, SavingAccount):
                account.apply_interest()