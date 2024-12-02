class BankView:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_accounts(accounts):
        if not accounts:
            print("No accounts available.")
        else:
            for account in accounts:
                print(account)