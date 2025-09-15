"""
First Classes in Python - Starter Template
CSC 242 - Week 1

This file provides skeleton code for learning Python classes. Complete the
TODO sections to implement the functionality.

Author: Brian O'Donnell
"""


# ============================================================================
# EXAMPLE 1: Basic Class Structure
# ============================================================================

class SimpleWrapper:
    """A basic wrapper class that stores and retrieves a value."""
    
    # TODO: Add a class variable called 'version' and set it to 1.0
    
    def set_value(self, value):
        """Set the stored value."""
        # TODO: Store the value in an instance variable called 'data'
        pass
    
    def get_value(self):
        """Get the stored value."""
        # TODO: Return the stored data
        pass
    
    def __str__(self):
        """Return string representation."""
        # TODO: Return a string that shows what the wrapper contains
        # If no value is set, return "SimpleWrapper containing: <no value set>"
        # If a value is set, return "SimpleWrapper containing: {value}"
        pass


def demo_simple_wrapper():
    """Demonstrate the SimpleWrapper class."""
    print("=== SIMPLE WRAPPER DEMO ===")
    
    # Create instances
    wrapper1 = SimpleWrapper()
    wrapper2 = SimpleWrapper()
    
    # Use the methods
    wrapper1.set_value("Hello, World!")
    wrapper2.set_value(42)
    
    print(f"Wrapper 1: {wrapper1.get_value()}")
    print(f"Wrapper 2: {wrapper2.get_value()}")
    print(f"Class version: {SimpleWrapper.version}")
    
    # Show string representation
    print(f"String representation: {wrapper1}")


# ============================================================================
# EXAMPLE 2: Class with Constructor
# ============================================================================

class Student:
    """A class to represent a student with courses."""
    
    # TODO: Add class variables:
    # - school_name = "DePaul University"
    # - total_students = 0
    
    def __init__(self, name, student_id, major="Undeclared"):
        """Initialize a new student."""
        # TODO: Set instance variables for:
        # - name
        # - student_id  
        # - major
        # - courses (empty list)
        # - gpa (0.0)
        
        # TODO: Increment the total_students class variable
        pass
    
    def add_course(self, course_name, credits=3):
        """Add a course to the student's course list."""
        # TODO: Create a dictionary with course name and credits
        # Add it to the courses list
        # Print a message like "{name} enrolled in {course_name}"
        pass
    
    def drop_course(self, course_name):
        """Remove a course from the student's course list."""
        # TODO: Find the course in the list and remove it
        # Print appropriate success or failure message
        pass
    
    def get_total_credits(self):
        """Calculate total credits enrolled."""
        # TODO: Sum up all the credits from all courses
        # Hint: Use a loop or sum() with a generator expression
        pass
    
    def set_gpa(self, gpa):
        """Set the student's GPA."""
        # TODO: Check if gpa is between 0.0 and 4.0
        # If valid, set it; if not, print an error message
        pass
    
    def get_academic_standing(self):
        """Determine academic standing based on GPA."""
        # TODO: Return academic standing based on GPA:
        # >= 3.5: "Dean's List"
        # >= 3.0: "Good Standing" 
        # >= 2.0: "Satisfactory"
        # < 2.0: "Academic Probation"
        pass
    
    def __str__(self):
        """Return a readable string representation."""
        # TODO: Return a string like:
        # "Student: {name} (ID: {student_id}, Major: {major}, Credits: {total_credits})"
        pass
    
    def __repr__(self):
        """Return a string that could recreate the object."""
        # TODO: Return a string like:
        # "Student('{name}', '{student_id}', '{major}')"
        pass


def demo_student_class():
    """Demonstrate the Student class."""
    print("\n=== STUDENT CLASS DEMO ===")
    
    # Create students
    alice = Student("Alice Johnson", "A12345", "Computer Science")
    bob = Student("Bob Smith", "B67890", "Mathematics")
    
    # Add courses
    alice.add_course("CSC 242", 4)
    alice.add_course("MAT 151", 4)
    alice.add_course("ENG 101", 3)
    
    bob.add_course("MAT 200", 4)
    bob.add_course("CSC 241", 4)
    
    # Set GPAs
    alice.set_gpa(3.7)
    bob.set_gpa(3.2)
    
    # Display information
    print(f"\n{alice}")
    print(f"GPA: {alice.gpa}, Standing: {alice.get_academic_standing()}")
    
    print(f"\n{bob}")
    print(f"GPA: {bob.gpa}, Standing: {bob.get_academic_standing()}")
    
    print(f"\nTotal students: {Student.total_students}")
    print(f"School: {Student.school_name}")


# ============================================================================
# EXAMPLE 3: Bank Account - Real-World Application
# ============================================================================

class BankAccount:
    """A class representing a bank account with realistic features."""
    
    # TODO: Add class variables:
    # - bank_name = "DePaul Credit Union"
    # - total_accounts = 0
    # - interest_rate = 0.02  # 2% annual interest
    
    def __init__(self, account_holder, initial_balance=0.0, account_type="Checking"):
        """Initialize a new bank account."""
        # TODO: Set instance variables for:
        # - account_holder
        # - balance (convert to float)
        # - account_type
        # - transaction_history (empty list)
        
        # TODO: Generate account number by incrementing total_accounts
        # and creating a string like "DCU000001"
        
        # TODO: If initial_balance > 0, record an initial deposit transaction
        pass
    
    def deposit(self, amount):
        """Deposit money into the account."""
        # TODO: Validate amount is positive
        # Add to balance
        # Record transaction
        # Print confirmation message
        # Return True on success, False on failure
        pass
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        # TODO: Validate amount is positive
        # Check if sufficient funds available
        # Subtract from balance
        # Record transaction  
        # Print confirmation message
        # Return True on success, False on failure
        pass
    
    def transfer(self, other_account, amount):
        """Transfer money to another account."""
        # TODO: Use withdraw() and deposit() methods
        # Record transfer transactions in both accounts
        # Print confirmation message
        # Return True on success, False on failure
        pass
    
    def apply_interest(self):
        """Apply annual interest to the account."""
        # TODO: Only apply interest to Savings accounts
        # Calculate interest and add to balance
        # Record transaction
        # Print confirmation message
        pass
    
    def get_balance(self):
        """Get the current balance."""
        # TODO: Return the current balance
        pass
    
    def get_transaction_history(self, limit=5):
        """Get recent transaction history."""
        # TODO: Return the last 'limit' transactions
        pass
    
    def _record_transaction(self, transaction_type, amount):
        """Private method to record transactions."""
        # TODO: Create a transaction dictionary with:
        # - date (current timestamp)
        # - type
        # - amount
        # - balance (current balance after transaction)
        # Add to transaction_history list
        pass
    
    def __str__(self):
        """Return account summary."""
        # TODO: Return a string like:
        # "{account_type} Account - {account_holder} ({account_number}): ${balance:.2f}"
        pass
    
    def __repr__(self):
        """Return detailed representation."""
        # TODO: Return a string like:
        # "BankAccount('{account_holder}', {balance}, '{account_type}')"
        pass


def demo_bank_account():
    """Demonstrate the BankAccount class."""
    print("\n=== BANK ACCOUNT DEMO ===")
    
    # Create accounts
    alice_checking = BankAccount("Alice Johnson", 1000.0, "Checking")
    bob_savings = BankAccount("Bob Smith", 5000.0, "Savings")
    
    print(f"Created: {alice_checking}")
    print(f"Created: {bob_savings}")
    
    # Perform transactions
    print("\n--- Transactions ---")
    alice_checking.deposit(250.0)
    alice_checking.withdraw(100.0)
    bob_savings.apply_interest()
    
    # Transfer money
    print("\n--- Transfer ---")
    alice_checking.transfer(bob_savings, 200.0)
    
    # Show final balances
    print("\n--- Final Balances ---")
    print(alice_checking)
    print(bob_savings)
    
    # Show transaction history
    print(f"\nAlice's recent transactions:")
    for transaction in alice_checking.get_transaction_history():
        print(f"  {transaction['date']}: {transaction['type']} ${transaction['amount']:.2f}")


# ============================================================================
# EXERCISES FOR STUDENTS
# ============================================================================

def exercise_1():
    """Exercise 1: Complete the SimpleWrapper class."""
    print("\n=== EXERCISE 1 ===")
    print("Complete the SimpleWrapper class methods above.")
    print("Test your implementation by running demo_simple_wrapper()")


def exercise_2():
    """Exercise 2: Complete the Student class."""
    print("\n=== EXERCISE 2 ===")
    print("Complete the Student class methods above.")
    print("Test your implementation by running demo_student_class()")


def exercise_3():
    """Exercise 3: Complete the BankAccount class."""
    print("\n=== EXERCISE 3 ===")
    print("Complete the BankAccount class methods above.")
    print("Test your implementation by running demo_bank_account()")


def exercise_4():
    """Exercise 4: Add new features."""
    print("\n=== EXERCISE 4 ===")
    print("Add these methods to the Student class:")
    print("1. get_course_count() - return number of courses")
    print("2. is_full_time() - return True if 12+ credits")
    print("3. get_courses_by_credits() - return courses sorted by credits")


def exercise_5():
    """Exercise 5: Bank account enhancements."""
    print("\n=== EXERCISE 5 ===")
    print("Add these methods to the BankAccount class:")
    print("1. calculate_monthly_interest() - for monthly interest calculation")
    print("2. get_account_summary() - detailed account information")
    print("3. close_account() - mark account as closed")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("CSC 242 - First Classes Starter Template")
    print("=" * 50)
    
    # Uncomment these as you complete each class:
    
    # demo_simple_wrapper()
    # demo_student_class()  
    # demo_bank_account()
    
    # Run exercises
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()