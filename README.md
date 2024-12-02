# Bank Account System

## Overview
The Bank Account System is an Object-Oriented Python application that allows users to manage their bank accounts, perform transactions like deposits and withdrawals, and implement business logic such as overdraft protection and minimum balance rules. The system is designed using the **Model-View-Controller (MVC)** architecture to ensure scalability and maintainability.

---

## Key Features
1. **Base Class (`Account`)**:
   - Tracks account holder and balance.
   - Core methods:
     - **`deposit(amount)`**: Add a specified amount to the balance.
     - **`withdraw(amount)`**: Deduct a specified amount if funds are sufficient.
     - **`get_balance()`**: Retrieve the current balance.
   - Additional features:
     - Transaction history (statements).
     - User-friendly string representation of account details.

2. **Account Subclasses**:
   - **`CheckingAccount`**:
     - Includes overdraft protection up to $500.
   - **`SavingsAccount`**:
     - Enforces a minimum balance of $100 after withdrawals.
   - **`FlexibleSavingsAccount`**:
     - Supports interest calculation using `apply_interest(rate)`.

3. **Bank Management**:
   - Create and manage multiple accounts.
   - List all accounts and their balances.

4. **User Interface**:
   - Command-line interface for account operations.
   - User-friendly messages and prompts for interaction.

---

