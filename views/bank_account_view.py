class BankAccountView:
    @staticmethod
    def display_account_details(account_details):
        """Display account details in a user-friendly format."""
        print(f"Account ID: {account_details['Account ID']}")
        print(f"Account Holder: {account_details['Account Holder']}")
        print(f"Balance: ${account_details['Balance']:.2f}")
        print(f"Account Creation Date: {account_details['Account Creation Date']}")
        print(f"Transaction History:")
        for transaction in account_details['Transaction History']:
            print(f"  {transaction['timestamp']} - {transaction['transaction_type']}: ${transaction['amount']:.2f}")
        if 'Overdraft Limit' in account_details:
            print(f"Overdraft Limit: ${account_details['Overdraft Limit']:.2f}")
        if 'Minimum Balance' in account_details:
            print(f"Minimum Balance: ${account_details['Minimum Balance']:.2f}")
            print(f"Interest Rate: {account_details['Interest Rate']:.2f}%")
        print("\n")