from controllers.bank_controller import BankController

def main():
    controller = BankController("My Bank")

    while True:
        print("\n1. Create Account")
        print("2. List Accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            acc_type = input("Enter account type (checking/savings/flexible_savings): ")
            balance = float(input("Enter initial balance: "))
            controller.create_account(acc_type, name, balance)
        elif choice == "2":
            controller.list_accounts()
        elif choice == "3":
            index = int(input("Enter account index: "))
            amount = float(input("Enter deposit amount: "))
            controller.deposit(index, amount)
        elif choice == "4":
            index = int(input("Enter account index: "))
            amount = float(input("Enter withdrawal amount: "))
            controller.withdraw(index, amount)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()