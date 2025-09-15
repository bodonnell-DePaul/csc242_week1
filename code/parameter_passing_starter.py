"""
Parameter Passing in Python - Starter Template
CSC 242 - Week 1

Learn how Python passes arguments to functions and methods.
Understanding the difference between mutable and immutable objects.

Complete the TODO sections to implement and test the concepts.

Author: Brian O'Donnell
"""


# ============================================================================
# BASIC PARAMETER PASSING CONCEPTS
# ============================================================================

def demonstrate_immutable_passing():
    """Demonstrate parameter passing with immutable objects."""
    print("=== IMMUTABLE PARAMETER PASSING ===")
    
    def try_to_modify_number(num):
        """Try to modify a number parameter."""
        print(f"Inside function - before: num = {num}, id = {id(num)}")
        # TODO: Try to modify num (add 10 to it)
        # TODO: Print the new value and id
        return num
    
    def try_to_modify_string(text):
        """Try to modify a string parameter."""
        print(f"Inside function - before: text = '{text}', id = {id(text)}")
        # TODO: Try to modify text (add " modified" to it)
        # TODO: Print the new value and id
        return text
    
    # Test with number
    original_num = 42
    print(f"Original number: {original_num}, id = {id(original_num)}")
    
    # TODO: Call try_to_modify_number with original_num
    # TODO: Print original_num after the function call
    # TODO: What happened to original_num? Why?
    
    print()
    
    # Test with string
    original_text = "Hello"
    print(f"Original string: '{original_text}', id = {id(original_text)}")
    
    # TODO: Call try_to_modify_string with original_text
    # TODO: Print original_text after the function call
    # TODO: What happened to original_text? Why?


def demonstrate_mutable_passing():
    """Demonstrate parameter passing with mutable objects."""
    print("\n=== MUTABLE PARAMETER PASSING ===")
    
    def modify_list(lst):
        """Modify a list parameter."""
        print(f"Inside function - before: lst = {lst}, id = {id(lst)}")
        # TODO: Add an element to the list (e.g., append "new item")
        # TODO: Print the list and id after modification
        return lst
    
    def reassign_list(lst):
        """Try to reassign a list parameter."""
        print(f"Inside function - before: lst = {lst}, id = {id(lst)}")
        # TODO: Reassign lst to a completely new list [100, 200, 300]
        # TODO: Print the list and id after reassignment
        return lst
    
    def modify_dictionary(d):
        """Modify a dictionary parameter."""
        print(f"Inside function - before: d = {d}, id = {id(d)}")
        # TODO: Add a new key-value pair to the dictionary
        # TODO: Print the dictionary and id after modification
        return d
    
    # Test with list
    original_list = [1, 2, 3]
    print(f"Original list: {original_list}, id = {id(original_list)}")
    
    # TODO: Call modify_list with original_list
    # TODO: Print original_list after the function call
    # TODO: What happened to original_list? Why?
    
    print()
    
    # TODO: Reset original_list to [1, 2, 3]
    # TODO: Call reassign_list with original_list
    # TODO: Print original_list after the function call
    # TODO: What happened to original_list? Why is this different from modify_list?
    
    print()
    
    # Test with dictionary
    original_dict = {"name": "Alice", "age": 25}
    print(f"Original dict: {original_dict}, id = {id(original_dict)}")
    
    # TODO: Call modify_dictionary with original_dict
    # TODO: Print original_dict after the function call
    # TODO: What happened to original_dict? Why?


# ============================================================================
# CLASS METHOD PARAMETER PASSING
# ============================================================================

class Student:
    """A student class to demonstrate method parameter passing."""
    
    def __init__(self, name, grades=None):
        """Initialize a student."""
        self.name = name
        # TODO: Set self.grades to grades if provided, otherwise empty list
        # IMPORTANT: Never use mutable default arguments!
        pass
    
    def add_grade(self, grade):
        """Add a grade to the student's grades."""
        # TODO: Append the grade to self.grades
        pass
    
    def modify_grade_list(self, grade_list):
        """Modify an external grade list."""
        # TODO: Add a grade (e.g., 95) to the provided grade_list
        pass
    
    def get_average(self):
        """Calculate the average grade."""
        # TODO: Return the average of all grades
        # Return 0 if no grades
        pass
    
    def __str__(self):
        """Return string representation."""
        # TODO: Return a string like "Student: {name}, Grades: {grades}, Average: {average:.1f}"
        pass


def demonstrate_method_parameter_passing():
    """Demonstrate parameter passing with class methods."""
    print("\n=== METHOD PARAMETER PASSING ===")
    
    # Create student
    student = Student("Bob")
    
    # TODO: Add some grades to the student
    
    # Test modifying external list
    external_grades = [80, 85, 90]
    print(f"External grades before: {external_grades}")
    
    # TODO: Call student.modify_grade_list with external_grades
    # TODO: Print external_grades after the method call
    # TODO: What happened to external_grades? Why?
    
    print(f"Student info: {student}")


# ============================================================================
# DEFAULT ARGUMENT PITFALLS
# ============================================================================

def demonstrate_mutable_default_arguments():
    """Demonstrate the pitfall of mutable default arguments."""
    print("\n=== MUTABLE DEFAULT ARGUMENTS ===")
    
    def bad_function(item, target_list=[]):
        """BAD: Don't use mutable default arguments!"""
        # TODO: Append item to target_list
        # TODO: Return target_list
        pass
    
    def good_function(item, target_list=None):
        """GOOD: Use None and create new list if needed."""
        # TODO: If target_list is None, create a new empty list
        # TODO: Append item to target_list
        # TODO: Return target_list
        pass
    
    print("Testing bad_function (mutable default):")
    # TODO: Call bad_function("first") and print result
    # TODO: Call bad_function("second") and print result
    # TODO: Call bad_function("third") and print result
    # TODO: What's happening? Why are previous items still there?
    
    print("\nTesting good_function (proper implementation):")
    # TODO: Call good_function("first") and print result
    # TODO: Call good_function("second") and print result
    # TODO: Call good_function("third") and print result
    # TODO: What's different? Why does this work correctly?


# ============================================================================
# ADVANCED CONCEPTS
# ============================================================================

def demonstrate_object_identity():
    """Demonstrate object identity vs equality."""
    print("\n=== OBJECT IDENTITY VS EQUALITY ===")
    
    # Integer identity
    a = 256
    b = 256
    print(f"a = {a}, b = {b}")
    print(f"a == b: {a == b}")  # Equality
    print(f"a is b: {a is b}")  # Identity
    print(f"id(a): {id(a)}, id(b): {id(b)}")
    
    # TODO: Try the same with larger numbers (e.g., 1000)
    # TODO: What's different? Why?
    
    # List identity
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    # TODO: Compare list1 == list2, list1 is list2
    # TODO: Compare list1 == list3, list1 is list3
    # TODO: Print the ids of all three lists
    # TODO: Explain the differences


def demonstrate_copy_vs_reference():
    """Demonstrate copying vs referencing."""
    print("\n=== COPY VS REFERENCE ===")
    
    import copy
    
    original = [1, [2, 3], 4]
    
    # Reference (aliasing)
    reference = original
    
    # Shallow copy
    shallow = copy.copy(original)
    # OR: shallow = original.copy()
    # OR: shallow = list(original)
    
    # Deep copy
    deep = copy.deepcopy(original)
    
    print(f"Original: {original}")
    print(f"Reference: {reference}")
    print(f"Shallow: {shallow}")
    print(f"Deep: {deep}")
    
    # TODO: Modify the nested list in original: original[1].append(999)
    # TODO: Print all four lists again
    # TODO: Which ones changed? Why?
    
    # TODO: Modify the top-level list in original: original.append(5)
    # TODO: Print all four lists again
    # TODO: Which ones changed? Why?


# ============================================================================
# EXERCISES
# ============================================================================

def exercise_1():
    """Exercise 1: Parameter passing experiments."""
    print("\n=== EXERCISE 1 ===")
    print("Complete the TODO sections in demonstrate_immutable_passing()")


def exercise_2():
    """Exercise 2: Mutable object experiments."""
    print("\n=== EXERCISE 2 ===")
    print("Complete the TODO sections in demonstrate_mutable_passing()")


def exercise_3():
    """Exercise 3: Complete the Student class."""
    print("\n=== EXERCISE 3 ===")
    print("Complete the Student class and demonstrate_method_parameter_passing()")


def exercise_4():
    """Exercise 4: Default arguments."""
    print("\n=== EXERCISE 4 ===")
    print("Complete demonstrate_mutable_default_arguments() and understand the pitfall")


def exercise_5():
    """Exercise 5: Advanced concepts."""
    print("\n=== EXERCISE 5 ===")
    print("Complete the advanced demonstration functions")


def exercise_6():
    """Exercise 6: Create your own examples."""
    print("\n=== EXERCISE 6 ===")
    print("Create your own functions that demonstrate:")
    print("1. A function that successfully modifies a list")
    print("2. A function that fails to modify an integer")
    print("3. A class method that modifies object state")
    print("4. A function with proper default argument handling")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("CSC 242 - Parameter Passing Starter")
    print("=" * 50)
    
    # Uncomment these as you complete each section:
    
    # demonstrate_immutable_passing()
    # demonstrate_mutable_passing()
    # demonstrate_method_parameter_passing()
    # demonstrate_mutable_default_arguments()
    # demonstrate_object_identity()
    # demonstrate_copy_vs_reference()
    
    # Run exercises
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()