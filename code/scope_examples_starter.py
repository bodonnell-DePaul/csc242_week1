"""
Variable Scope and Namespaces in Python - Starter Template
CSC 242 - Week 1

Learn about different types of variable scope in Python:
- Local scope
- Enclosing scope  
- Global scope
- Built-in scope

Complete the TODO sections to understand how Python resolves variable names.

Author: Brian O'Donnell
"""


# ============================================================================
# GLOBAL VARIABLES
# ============================================================================

# TODO: Create a global variable called 'global_counter' and set it to 0
global_counter = 0
# TODO: Create a global variable called 'global_message' and set it to "Hello from global scope"
global_message = "Hello from global scope"

def demonstrate_global_scope():
    """Demonstrate global variable access."""
    print("=== GLOBAL SCOPE DEMONSTRATION ===")
    
    def read_global():
        """Function that reads global variables."""
        # TODO: Print both global_counter and global_message
        print('Global Counter: {}'.format(global_counter))
        print('Global Message: {}'.format(global_message))
        # TODO: Print their ids using id() function
        print('Global Counter ID: {}'.format(id(global_counter)))
        print('Global Message ID: {}'.format(id(global_message)))
        pass
    
    def modify_global_wrong():
        """Attempt to modify global variable (this will create local variable)."""
        # TODO: Try to increment global_counter by 1
        global_counter = -5
        global_counter += 1
        # TODO: Print the value and id of global_counter
        print('Global Counter Take Two: {}'.format(global_counter))
        print('Global Counter ID: {}'.format(id(global_counter)))
        pass
    
    def modify_global_correct():
        """Correctly modify global variable using global keyword."""
        # TODO: Use 'global' keyword to declare global_counter as global
        global global_counter
        # TODO: Increment global_counter by 1
        global_counter += 1
        # TODO: Print the value and id of global_counter
        print('Global Global Counter: {}'.format(global_counter))
        print('Global Global Counter ID: {}'.format(id(global_counter)))
        pass
    
    print(f"Initial global_counter: {global_counter}")
    
    
    modify_global_wrong()
    modify_global_correct()
    read_global()
    # TODO: Call read_global()
    # TODO: Call modify_global_wrong()
    # TODO: Print global_counter after wrong modification - did it change?
    # TODO: Call modify_global_correct()
    # TODO: Print global_counter after correct modification - did it change?


# ============================================================================
# LOCAL SCOPE
# ============================================================================

def demonstrate_local_scope():
    """Demonstrate local variable scope."""
    print("\n=== LOCAL SCOPE DEMONSTRATION ===")
    
    def outer_function():
        """Function with local variables."""
        # TODO: Create a local variable 'local_var' with value "I'm local"
        local_var = "I'm local"
        # TODO: Create a local variable 'number' with value 42
        number = 42
        
        def inner_function():
            """Nested function accessing outer function's variables."""
            # TODO: Print local_var and number from outer function
            print('Our outer function variable: {} {}'.format(local_var, number))
            # TODO: Try to create a new local variable 'inner_var' with value "I'm inner"
            inner_var = "I'm inner"
            print('The Inner Variable: {}'.format(inner_var))
            # TODO: Print inner_var
            pass
        
        def inner_modify():
            """Try to modify outer function's variable."""
            # TODO: Try to modify 'number' by adding 10 to it
            number = number + 10
            # TODO: Print the modified number
            print('Modified Number: {}'.format(number))
            # TODO: What will happen? Will this work?
            pass
        
        def inner_modify_correct():
            """Correctly modify outer function's variable using nonlocal."""
            # TODO: Use 'nonlocal' keyword to declare 'number' as nonlocal
            nonlocal number
            number += 10
            # TODO: Add 10 to number
            # TODO: Print the modified number
            pass
        
        print(f"Outer function - local_var: {local_var}")
        print(f"Outer function - number: {number}")
        
        # TODO: Call inner_function()
        # TODO: Try to call inner_modify() - what happens?
        # TODO: Call inner_modify_correct()
        # TODO: Print number after correct modification
        
        # TODO: Try to print inner_var here - what happens? Why?
    
    # TODO: Call outer_function()
    # TODO: Try to print local_var here - what happens? Why?


# ============================================================================
# CLASS SCOPE
# ============================================================================

class ScopeDemo:
    """Class to demonstrate class and instance variable scope."""
    
    # TODO: Create a class variable 'class_var' with value "I'm a class variable"
    # TODO: Create a class variable 'counter' with value 0
    
    def __init__(self, name):
        """Initialize instance."""
        # TODO: Set instance variable 'name' to the provided name
        # TODO: Set instance variable 'instance_var' to "I'm an instance variable"
        # TODO: Increment the class variable 'counter'
        pass
    
    def show_variables(self):
        """Display different types of variables."""
        # TODO: Print self.name (instance variable)
        # TODO: Print self.instance_var (instance variable)
        # TODO: Print self.class_var (class variable accessed through instance)
        # TODO: Print ScopeDemo.class_var (class variable accessed through class)
        # TODO: Print ScopeDemo.counter (class variable)
        pass
    
    def modify_class_var_wrong(self):
        """Incorrectly modify class variable (creates instance variable)."""
        # TODO: Try to modify self.class_var by adding " - modified"
        # TODO: Print self.class_var
        # TODO: Print ScopeDemo.class_var
        # TODO: What's the difference? Why?
        pass
    
    def modify_class_var_correct(self):
        """Correctly modify class variable."""
        # TODO: Modify ScopeDemo.class_var by adding " - correctly modified"
        # TODO: Print self.class_var
        # TODO: Print ScopeDemo.class_var
        pass
    
    @classmethod
    def class_method_demo(cls):
        """Demonstrate class method scope."""
        # TODO: Print cls.class_var
        # TODO: Print cls.counter
        # TODO: Try to access instance variables - what happens?
        pass
    
    @staticmethod
    def static_method_demo():
        """Demonstrate static method scope."""
        # TODO: Print ScopeDemo.class_var
        # TODO: Try to access cls or self - what happens?
        pass


def demonstrate_class_scope():
    """Demonstrate class variable scope."""
    print("\n=== CLASS SCOPE DEMONSTRATION ===")
    
    # TODO: Create two instances of ScopeDemo
    obj1 = ScopeDemo("Object 1")
    obj2 = ScopeDemo("Object 2")
    
    # TODO: Call show_variables() on both objects
    
    # TODO: Call modify_class_var_wrong() on obj1
    # TODO: Call show_variables() on both objects - what changed?
    
    # TODO: Call modify_class_var_correct() on obj2
    # TODO: Call show_variables() on both objects - what changed?
    
    # TODO: Call the class method and static method


# ============================================================================
# LEGB RULE DEMONSTRATION
# ============================================================================

# Global variable
name = "Global"

def demonstrate_legb_rule():
    """Demonstrate the LEGB rule: Local, Enclosing, Global, Built-in."""
    print("\n=== LEGB RULE DEMONSTRATION ===")
    
    # Enclosing variable
    name = "Enclosing"
    
    def outer():
        # Local to outer (enclosing for inner)
        name = "Outer Local"
        
        def inner():
            # TODO: Print the value of 'name' here
            # TODO: Which 'name' will be printed? Why?
            pass
        
        def inner_with_local():
            # Local variable
            name = "Inner Local" 
            # TODO: Print the value of 'name' here
            # TODO: Which 'name' will be printed? Why?
            pass
        
        def inner_with_global():
            # TODO: Use 'global' keyword to access global 'name'
            # TODO: Print the value of 'name'
            # TODO: Which 'name' will be printed? Why?
            pass
        
        def inner_with_nonlocal():
            # TODO: Use 'nonlocal' keyword to access outer's 'name'
            # TODO: Print the value of 'name'
            # TODO: Modify 'name' by adding " - modified"
            # TODO: Print the value of 'name' again
            pass
        
        print(f"Outer function name: {name}")
        
        # TODO: Call all the inner functions
        
        print(f"Outer function name after calls: {name}")
    
    print(f"Enclosing function name: {name}")
    # TODO: Call outer()
    print(f"Enclosing function name after outer(): {name}")


def demonstrate_builtin_scope():
    """Demonstrate built-in scope."""
    print("\n=== BUILT-IN SCOPE DEMONSTRATION ===")
    
    # TODO: Print some built-in functions like len, max, min
    # TODO: These are in the built-in namespace
    
    def shadow_builtin():
        """Function that shadows a built-in name."""
        # TODO: Create a local variable named 'len' with value "I'm not the built-in len!"
        # TODO: Print len
        # TODO: Try to use len() function - what happens?
        pass
    
    # TODO: Call shadow_builtin()
    # TODO: Print len after the function call - what is it?


# ============================================================================
# NAMESPACE INTROSPECTION
# ============================================================================

def demonstrate_namespace_inspection():
    """Demonstrate how to inspect namespaces."""
    print("\n=== NAMESPACE INSPECTION ===")
    
    local_var = "I'm local"
    
    # TODO: Print locals() - shows local namespace
    # TODO: Print globals() - shows global namespace (this will be long!)
    # TODO: Print dir() - shows names in current scope
    # TODO: Print __builtins__ - shows built-in namespace
    
    def inner():
        inner_var = "I'm inner"
        # TODO: Print locals() from inside inner function
        # TODO: What's different?
        pass
    
    # TODO: Call inner()


# ============================================================================
# EXERCISES
# ============================================================================

def exercise_1():
    """Exercise 1: Complete global scope demonstration."""
    print("\n=== EXERCISE 1 ===")
    print("Complete the global scope functions and understand global vs local variables")


def exercise_2():
    """Exercise 2: Complete local scope demonstration."""
    print("\n=== EXERCISE 2 ===")
    print("Complete the local scope functions and understand nested function scoping")


def exercise_3():
    """Exercise 3: Complete class scope demonstration."""
    print("\n=== EXERCISE 3 ===")
    print("Complete the ScopeDemo class and understand instance vs class variables")


def exercise_4():
    """Exercise 4: Complete LEGB rule demonstration."""
    print("\n=== EXERCISE 4 ===")
    print("Complete the LEGB rule functions and understand variable resolution order")


def exercise_5():
    """Exercise 5: Create scope experiments."""
    print("\n=== EXERCISE 5 ===")
    print("Create your own examples that demonstrate:")
    print("1. A function that modifies a global variable")
    print("2. Nested functions with nonlocal variables")
    print("3. A class with both class and instance variables")
    print("4. Variable shadowing examples")


def exercise_6():
    """Exercise 6: Scope debugging."""
    print("\n=== EXERCISE 6 ===")
    print("Debug these scope-related problems:")
    print("1. UnboundLocalError when trying to modify global variables")
    print("2. Unexpected behavior with mutable default arguments")
    print("3. Class vs instance variable confusion")
    print("4. Built-in function shadowing")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("CSC 242 - Variable Scope and Namespaces Starter")
    print("=" * 50)
    
    # Uncomment these as you complete each section:
    
    demonstrate_global_scope()
    # demonstrate_local_scope()
    # demonstrate_class_scope()
    # demonstrate_legb_rule()
    # demonstrate_builtin_scope()
    # demonstrate_namespace_inspection()
    
    # Run exercises
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()