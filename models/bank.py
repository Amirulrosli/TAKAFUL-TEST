class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)

    def list_accounts(self):
        return [str(account) for account in self.accounts]