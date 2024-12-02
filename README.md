# Banking System

This is a simple banking system implemented in Python, which supports basic banking operations such as deposits, withdrawals, account creation, and transfers between accounts. It includes multiple account types such as Checking and Saving accounts, with additional features like overdraft protection, interest calculation, and transaction logging.

## Features

- **BankAccount Base Class**:
  - Common fields: `account_holder`, `balance`.
  - Core methods: `deposit(amount)`, `withdraw(amount)`, `get_balance()`.
  - Allows extensions with additional methods and properties.

- **CheckingAccount**:
  - Inherits from `BankAccount`.
  - Standard withdrawal rules, with overdraft protection.
  
- **SavingAccount**:
  - Inherits from `BankAccount`.
  - Withdrawals are allowed only if the balance remains above a minimum threshold (e.g., $100).
  - Interest calculation is applied to the balance.

- **FlexibleSavingAccount**:
  - Inherits from `SavingAccount`.
  - Offers a base interest rate and bonus interest for higher balances.
  - Includes a penalty fee for withdrawals that fall below the bonus interest threshold.

- **Transaction Logging**:
  - Each transaction (deposit, withdrawal, interest) is logged with timestamp and description.

- **Transfer Functionality**:
  - Allows transferring money between accounts.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/banking-system.git

2. Install required dependencies (if any). For this simple implementation, no external libraries are needed.

3. Run the application:
    ```bash
   python main.py


## System Design

### Base Classes:

- **Account**: The base class for all accounts, containing methods for deposits, withdrawals, balance checking, and transaction logging.

### Subclasses:

- **CheckingAccount**: Extends `Account` with overdraft protection.
- **SavingAccount**: Extends `Account` with a withdrawal restriction based on a minimum balance.
- **FlexibleSavingAccount**: Extends `SavingAccount` with bonus interest rates and penalty fees for specific withdrawals.

### Transaction Logging:

- Every deposit, withdrawal, or interest application is logged in the `transactions` list, providing an audit trail.

## Code Structure

- **account.py**: Contains the `Account` class and its core methods.
- **checking_account.py**: Contains the `CheckingAccount` class.
- **saving_account.py**: Contains the `SavingAccount` class.
- **flexible_saving_account.py**: Contains the `FlexibleSavingAccount` class.
- **transaction.py**: Contains the `Transaction` class to log transactions.
- **bank.py**: Contains the `Bank` class to manage customers and accounts.
- **customer.py**: Contains the `Customer` and `Contact` classes.
- **address.py**: Contains the `Address` class.

## Future Enhancements

- **Implement user authentication** for account access.
- **Add support for loan accounts** and credit card functionalities.
- **Introduce more comprehensive error handling**, such as logging failed transactions.
- **Implement an interactive CLI or a GUI** for better user experience.
- **Introduce unit tests** for key functionalities.

