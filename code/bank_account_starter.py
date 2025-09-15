"""
Bank Account System - Starter Template
CSC 242 - Week 1

A skeleton for learning advanced object-oriented programming concepts
including inheritance, encapsulation, and error handling.

Complete the TODO sections to implement the functionality.

Author: Brian O'Donnell
"""

from datetime import datetime


class Transaction:
    """A class to represent a single transaction."""
    
    def __init__(self, transaction_type, amount, description=""):
        """Initialize a transaction."""
        # TODO: Set instance variables for:
        # - timestamp (current datetime)
        # - type (transaction_type)
        # - amount
        # - description
        pass
    
    def __str__(self):
        """Return a formatted string representation."""
        # TODO: Return a formatted string showing:
        # date | transaction_type | amount | description
        # Example: "2025-09-13 14:30:25 | Deposit      | $  100.00 | ATM deposit"
        pass


class BankAccount:
    """Base class for all types of bank accounts."""
    
    # TODO: Add class variables:
    # - bank_name = "DePaul Credit Union"
    # - routing_number = "271180810"
    # - total_accounts = 0
    
    def __init__(self, account_holder, initial_balance=0.0):
        """Initialize a bank account."""
        # TODO: Add input validation:
        # - account_holder cannot be empty
        # - initial_balance cannot be negative
        # Raise ValueError for invalid inputs
        
        # TODO: Set instance variables:
        # - account_holder (strip whitespace)
        # - balance (convert to float)
        # - transactions (empty list)
        # - is_active (True)
        
        # TODO: Generate unique account number and increment total_accounts
        
        # TODO: Record initial deposit if initial_balance > 0
        pass
    
    def _generate_account_number(self):
        """Generate a unique account number."""
        # TODO: Return a formatted account number like "DCU00000001"
        pass
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """Add a transaction to the history."""
        # TODO: Create a Transaction object and add to transactions list
        pass
    
    def deposit(self, amount, description=""):
        """Deposit money into the account."""
        # TODO: Validate account is active and amount is positive
        # Add to balance, record transaction, print confirmation
        # Return True on success, False on failure
        pass
    
    def withdraw(self, amount, description=""):
        """Withdraw money from the account."""
        # TODO: Validate account is active, amount is positive, and sufficient funds
        # Subtract from balance, record transaction, print confirmation
        # Return True on success, False on failure
        pass
    
    def _can_withdraw(self, amount):
        """Check if withdrawal is allowed."""
        # TODO: Return True if balance >= amount, False otherwise
        # Print error message if insufficient funds
        pass
    
    def transfer_to(self, other_account, amount, description=""):
        """Transfer money to another account."""
        # TODO: Withdraw from this account and deposit to other account
        # Record transfer transactions in both accounts
        # Return True on success, False on failure
        pass
    
    def get_balance(self):
        """Get current account balance."""
        # TODO: Return the current balance
        pass
    
    def get_transaction_history(self, limit=10):
        """Get recent transaction history."""
        # TODO: Return the last 'limit' transactions
        pass
    
    def get_account_info(self):
        """Get comprehensive account information."""
        # TODO: Return a dictionary with account details:
        # - account_number, account_holder, balance, is_active, total_transactions
        pass
    
    def close_account(self):
        """Close the account."""
        # TODO: Set is_active to False
        # Record a transaction for account closure
        # Print confirmation message
        pass
    
    def __str__(self):
        """Return basic account information."""
        # TODO: Return string like "Account {account_number} - {account_holder}: ${balance:.2f}"
        pass
    
    def __repr__(self):
        """Return detailed representation."""
        # TODO: Return string that could recreate the object
        pass


class CheckingAccount(BankAccount):
    """A checking account with overdraft protection."""
    
    def __init__(self, account_holder, initial_balance=0.0, overdraft_limit=100.0):
        """Initialize a checking account."""
        # TODO: Call parent constructor
        # Set account_type to "Checking"
        # Set overdraft_limit
        pass
    
    def _can_withdraw(self, amount):
        """Check if withdrawal is allowed with overdraft."""
        # TODO: Allow withdrawal if balance + overdraft_limit >= amount
        # Print appropriate error messages
        pass
    
    def get_available_balance(self):
        """Get balance including overdraft limit."""
        # TODO: Return balance + overdraft_limit
        pass


class SavingsAccount(BankAccount):
    """A savings account with interest calculation."""
    
    # TODO: Add class variable for interest_rate (e.g., 0.02 for 2%)
    
    def __init__(self, account_holder, initial_balance=0.0):
        """Initialize a savings account."""
        # TODO: Call parent constructor
        # Set account_type to "Savings"
        pass
    
    def calculate_interest(self, months=1):
        """Calculate interest for given months."""
        # TODO: Calculate monthly interest: balance * (interest_rate / 12) * months
        # Return the interest amount
        pass
    
    def apply_interest(self, months=1):
        """Apply interest to the account."""
        # TODO: Calculate interest and add to balance
        # Record as a transaction
        # Print confirmation
        pass


class BusinessAccount(BankAccount):
    """A business account with transaction fees."""
    
    def __init__(self, business_name, initial_balance=0.0, monthly_fee=25.0):
        """Initialize a business account."""
        # TODO: Call parent constructor with business_name
        # Set account_type to "Business"
        # Set monthly_fee
        # Set transaction_count to 0
        pass
    
    def deposit(self, amount, description=""):
        """Deposit with transaction counting."""
        # TODO: Call parent deposit method
        # Increment transaction_count if successful
        pass
    
    def withdraw(self, amount, description=""):
        """Withdraw with transaction counting."""
        # TODO: Call parent withdraw method
        # Increment transaction_count if successful
        pass
    
    def apply_monthly_fee(self):
        """Apply monthly maintenance fee."""
        # TODO: Subtract monthly_fee from balance
        # Record as transaction
        # Reset transaction_count to 0
        pass
    
    def get_monthly_summary(self):
        """Get summary of monthly activity."""
        # TODO: Return dictionary with transaction_count, monthly_fee, current_balance
        pass


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demo_basic_account():
    """Demonstrate basic BankAccount functionality."""
    print("=== BASIC ACCOUNT DEMO ===")
    
    # TODO: Create a basic account, perform deposits/withdrawals
    # Show transaction history
    pass


def demo_account_types():
    """Demonstrate different account types."""
    print("\n=== ACCOUNT TYPES DEMO ===")
    
    # TODO: Create checking, savings, and business accounts
    # Demonstrate unique features of each
    pass


def demo_transfers():
    """Demonstrate transfers between accounts."""
    print("\n=== TRANSFER DEMO ===")
    
    # TODO: Create multiple accounts and transfer money between them
    pass


def demo_error_handling():
    """Demonstrate error handling."""
    print("\n=== ERROR HANDLING DEMO ===")
    
    # TODO: Test invalid inputs and edge cases
    pass


# ============================================================================
# EXERCISES
# ============================================================================

def exercise_1():
    """Complete the Transaction class."""
    print("\n=== EXERCISE 1: Transaction Class ===")
    print("Complete the Transaction class __init__ and __str__ methods")


def exercise_2():
    """Complete the BankAccount class."""
    print("\n=== EXERCISE 2: BankAccount Class ===")
    print("Complete all methods in the BankAccount class")


def exercise_3():
    """Complete the specialized account classes."""
    print("\n=== EXERCISE 3: Specialized Accounts ===")
    print("Complete CheckingAccount, SavingsAccount, and BusinessAccount classes")


def exercise_4():
    """Add advanced features."""
    print("\n=== EXERCISE 4: Advanced Features ===")
    print("Add these features:")
    print("1. Account statements (formatted transaction history)")
    print("2. Account freeze/unfreeze functionality")
    print("3. Minimum balance requirements")
    print("4. Transaction limits per day")


def exercise_5():
    """Create a bank management system."""
    print("\n=== EXERCISE 5: Bank Management ===")
    print("Create a Bank class that manages multiple accounts:")
    print("1. Create and close accounts")
    print("2. Process transfers between accounts")
    print("3. Generate bank-wide reports")
    print("4. Apply monthly fees and interest to all accounts")


# ============================================================================
# TESTING FUNCTIONS
# ============================================================================

def test_transaction():
    """Test the Transaction class."""
    print("Testing Transaction class...")
    # TODO: Create test transactions and verify they work correctly


def test_basic_account():
    """Test the BankAccount class."""
    print("Testing BankAccount class...")
    # TODO: Test all basic account functionality


def test_specialized_accounts():
    """Test specialized account classes."""
    print("Testing specialized account classes...")
    # TODO: Test checking, savings, and business accounts


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("CSC 242 - Bank Account System Starter")
    print("=" * 50)
    
    # Uncomment these as you complete each section:
    
    # demo_basic_account()
    # demo_account_types()
    # demo_transfers() 
    # demo_error_handling()
    
    # Run exercises
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    
    # Uncomment to run tests:
    # test_transaction()
    # test_basic_account()
    # test_specialized_accounts()