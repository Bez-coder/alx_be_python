class BankAccount:
    """Represents a bank account with basic operations."""

    def __init__(self, initial_balance=0):
        """Initialize the account balance with an optional starting amount."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Deduct the amount from the account balance if funds are sufficient."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
import sys
from bank_account import BankAccount

def main():
    """Command-line interface for managing a bank account."""
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Error: Insufficient funds or invalid withdrawal amount.")
    elif command == "display":
        account.display_balance()
    else:
        print("Error: Invalid command.")

if __name__ == "__main__":
    main()
