# Week 1: Git/GitHub Essentials and Object-Oriented Programming in Python
## Student Reference Guide for CSC 242

---

## Table of Contents
1. [Course Overview and Prerequisites](#course-overview-and-prerequisites)
2. [Git and GitHub Fundamentals](#git-and-github-fundamentals)
3. [GitHub Classroom Workflow](#github-classroom-workflow)
4. [Review: Essential Python Concepts](#review-essential-python-concepts)
5. [Understanding Python Objects](#understanding-python-objects)
6. [Introduction to Classes](#introduction-to-classes)
7. [Namespaces and Variable Scope](#namespaces-and-variable-scope)
8. [Example Code Files](#example-code-files)
9. [Practice Exercises](#practice-exercises)

---

## Course Overview and Prerequisites

### What You Should Already Know
Before diving into CSC 242, ensure you're comfortable with:

- **Python Fundamentals**: Variables, data types, control structures (if/else, loops)
- **Functions**: Definition, parameters, return values, local vs global scope
- **Data Structures**: Lists, dictionaries, tuples, sets
- **File Processing**: Reading from and writing to files
- **Exception Handling**: Try/except blocks
- **Basic Problem Solving**: Algorithms for searching, sorting, counting

### What We'll Learn This Semester
- **Git and GitHub**: Professional version control and collaboration tools
- **Object-Oriented Programming (OOP)**: Classes, objects, inheritance, encapsulation
- **Graphical User Interfaces (GUIs)**: Building interactive applications
- **Recursion**: Advanced problem-solving technique
- **Internet Programming**: Client-server applications
- **Database Integration**: Working with data persistence

---

## Git and GitHub Fundamentals

### Why Version Control?

Version control is essential for professional software development. It helps you:

- **Track Changes**: See what changed, when, and why
- **Collaborate**: Work with others without conflicts
- **Backup**: Never lose your work
- **History**: Revert to previous versions if needed
- **Branching**: Work on features independently

### Git vs GitHub

- **Git**: The version control system (software on your computer)
- **GitHub**: Cloud service that hosts Git repositories and adds collaboration features

Think of Git as Microsoft Word's "Track Changes" feature, and GitHub as Google Drive for sharing those documents.

### Essential Git Commands

#### Initial Setup (One Time Only)
```bash
# Configure your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@student.depaul.edu"

# Set default branch name
git config --global init.defaultBranch main
```

#### Daily Workflow Commands
```bash
# Clone a repository from GitHub to your computer
git clone git@github.com:username/repository-name.git

# Check the status of your repository
git status

# Add files to staging area (prepare for commit)
git add filename.py          # Add specific file
git add .                    # Add all changed files

# Commit changes with a message
git commit -m "Add Pet class with make_sound method"

# Push changes to GitHub
git push origin main

# Pull latest changes from GitHub
git pull origin main
```

#### Useful Information Commands
```bash
# View commit history
git log --oneline

# See what files have changed
git status

# See specific changes in files
git diff
```

### SSH Key Setup

SSH keys provide secure authentication without passwords. Here's how to set them up:

#### 1. Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your.email@student.depaul.edu"
```
- Press Enter to accept default file location
- Press Enter twice to skip passphrase (for simplicity)

#### 2. Copy Public Key
**Windows:**
```bash
type ~/.ssh/id_ed25519.pub
```

**Mac/Linux:**
```bash
cat ~/.ssh/id_ed25519.pub
```

#### 3. Add to GitHub
1. Go to GitHub.com → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Paste your public key
4. Give it a descriptive title (e.g., "CSC 242 Laptop")

#### 4. Test Connection
```bash
ssh -T git@github.com
```
You should see a message like "Hi username! You've successfully authenticated..."

### Common Git Issues and Solutions

#### Problem: "Git command not found"
**Solution**: Install Git from [git-scm.com](https://git-scm.com/)

#### Problem: "Permission denied (publickey)"
**Solutions**:
1. Verify SSH key is added to GitHub
2. Make sure you're using the SSH URL (starts with `git@github.com`)
3. Regenerate SSH key if needed

#### Problem: "Your branch is ahead of origin/main"
**Solution**: You have uncommitted changes. Run `git push origin main`

#### Problem: "Please tell me who you are"
**Solution**: Set up your Git identity with the config commands above

---

## GitHub Classroom Workflow

### Understanding GitHub Classroom

GitHub Classroom is a tool that:
- Creates individual repositories for each student
- Distributes assignment templates automatically
- Provides instructors with easy access for grading
- Maintains assignment history and submissions

### Assignment Acceptance Process

1. **Click Assignment Link**: Provided by instructor
2. **Accept Assignment**: GitHub creates your personal repository
3. **Clone Repository**: Download to your computer
4. **Complete Work**: Edit files and write code
5. **Commit and Push**: Submit your work
6. **Verify Submission**: Check that changes appear on GitHub

### Step-by-Step Assignment Workflow

#### Step 1: Accept Assignment
- Click the assignment link provided by instructor
- If prompted, select your name from the roster
- GitHub automatically creates a repository named something like:
  `assignment-1-yourusername`

#### Step 2: Clone Repository
```bash
# Replace with your actual repository URL
git clone git@github.com:csc242-depaul/assignment-1-yourusername.git

# Navigate into the cloned directory
cd assignment-1-yourusername
```

#### Step 3: Complete Your Work
- Open files in your preferred text editor or IDE
- Write your code and make changes
- Save your files frequently

#### Step 4: Submit Your Work
```bash
# Check what files have changed
git status

# Add your changes
git add .

# Commit with a descriptive message
git commit -m "Complete Pet class assignment"

# Push to GitHub
git push origin main
```

#### Step 5: Verify Submission
- Go to your repository on GitHub.com
- Verify your files are there and up-to-date
- Check that the commit timestamp is recent
- Your instructor can now see your submission

### Best Practices for Commits

#### Good Commit Messages
- `"Add Pet class with constructor and make_sound method"`
- `"Fix indentation error in calculate_average function"`
- `"Complete exercise 3 - bank account class"`

#### Poor Commit Messages
- `"stuff"`
- `"fixed it"`
- `"homework"`

#### Commit Frequency
- **Too Often**: After every line of code
- **Too Rare**: Only when assignment is complete
- **Just Right**: After completing a logical unit of work (method, class, exercise)

### Troubleshooting Submissions

#### How to Check if Your Assignment is Submitted
1. Go to your repository on GitHub.com
2. Look for your recent commits in the commit history
3. Verify that your code files are visible and contain your latest changes
4. Check the "last commit" timestamp

#### What to Do if Files Don't Appear on GitHub
1. Run `git status` to check for uncommitted files
2. Run `git add .` to stage all changes
3. Run `git commit -m "Add missing files"`
4. Run `git push origin main`
5. Refresh GitHub page to verify

#### Getting Help
- Check GitHub repository issues for common problems
- Ask classmates (but don't share code solutions)
- Attend office hours
- Email instructor with specific error messages

---

## Review: Essential Python Concepts

### 1. Input Validation with Exception Handling

One of the most common patterns you'll use is validating user input. Here's a robust approach:

```python
def get_valid_integer(prompt):
    """
    Prompts user for an integer and re-prompts until valid input is received.
    
    Args:
        prompt (str): The message to display to the user
        
    Returns:
        int: A valid integer from the user
    """
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
```

**Key Learning Points:**
- Use `while True` loops for input validation
- Handle specific exceptions (like `ValueError`) rather than generic exceptions
- Provide clear error messages to users

### 2. Working with Random Numbers

The `random` module is essential for many programming tasks:

```python
import random

# Generate random integers
random_int = random.randint(1, 10)  # Includes both 1 and 10

# Generate random floats
random_float = random.random()  # Between 0.0 and 1.0

# Choose random elements from a list
colors = ['red', 'blue', 'green', 'yellow']
random_color = random.choice(colors)
```

---

## Understanding Python Objects

### The Three Properties of Every Object

In Python, everything is an object. Each object has three fundamental properties:

1. **Identity**: A unique ID (memory address)
2. **Type**: What kind of object it is
3. **Value**: The data it contains

```python
# Example: Exploring object properties
my_list = [1, 2, 3]

print(f"Identity: {id(my_list)}")     # e.g., 140712234567808
print(f"Type: {type(my_list)}")       # <class 'list'>
print(f"Value: {my_list}")            # [1, 2, 3]
```

### Mutable vs Immutable Objects

Understanding mutability is crucial for avoiding common programming errors:

**Immutable Objects** (cannot be changed after creation):
- Integers, floats, strings, tuples

**Mutable Objects** (can be modified after creation):
- Lists, dictionaries, sets, user-defined objects

```python
# Immutable example - strings
text = "Hello"
text_id = id(text)
text = text + " World"  # Creates a NEW string object
print(id(text) == text_id)  # False - different object!

# Mutable example - lists
numbers = [1, 2, 3]
numbers_id = id(numbers)
numbers.append(4)  # Modifies the SAME list object
print(id(numbers) == numbers_id)  # True - same object!
```

### Parameter Passing: The Full Story

Python passes all arguments by **reference**, but the behavior depends on mutability:

```python
def modify_immutable(x):
    """Attempts to modify an immutable object"""
    x = x + 10  # Creates new object, doesn't affect original
    return x

def modify_mutable(lst):
    """Modifies a mutable object"""
    lst.append(999)  # Modifies the original list

# Test with immutable
num = 5
new_num = modify_immutable(num)
print(f"Original: {num}, Modified: {new_num}")  # Original: 5, Modified: 15

# Test with mutable
my_list = [1, 2, 3]
modify_mutable(my_list)
print(my_list)  # [1, 2, 3, 999] - original list was modified!
```

---

## Introduction to Classes

### Why Do We Need Classes?

As programs grow larger and more complex, we need better ways to organize our code. Classes allow us to:

1. **Group related data and functions together**
2. **Create reusable code templates**
3. **Model real-world entities in our programs**
4. **Encapsulate (hide) implementation details**

### Your First Class

```python
class Student:
    """A simple class to represent a student"""
    
    # Class variable (shared by all instances)
    school_name = "DePaul University"
    
    def __init__(self, name, student_id):
        """Constructor: called when creating a new Student object"""
        self.name = name          # Instance variable
        self.student_id = student_id  # Instance variable
        self.courses = []         # Instance variable
    
    def add_course(self, course_name):
        """Add a course to the student's course list"""
        self.courses.append(course_name)
        print(f"{self.name} enrolled in {course_name}")
    
    def get_course_count(self):
        """Return the number of courses the student is taking"""
        return len(self.courses)
    
    def __str__(self):
        """Return a human-readable string representation"""
        return f"Student: {self.name} (ID: {self.student_id})"
    
    def __repr__(self):
        """Return a string that could recreate the object"""
        return f"Student('{self.name}', '{self.student_id}')"
```

### Using Your Class

```python
# Create student objects
alice = Student("Alice Johnson", "12345")
bob = Student("Bob Smith", "67890")

# Use the methods
alice.add_course("CSC 242")
alice.add_course("MAT 151")
bob.add_course("CSC 242")

# Access properties
print(alice)  # Uses __str__ method
print(f"Alice is taking {alice.get_course_count()} courses")
print(f"Both students attend {Student.school_name}")
```

### Key Class Concepts

**Class vs Instance Variables:**
- **Class variables**: Shared by all objects of the class
- **Instance variables**: Unique to each object

**Special Methods (Magic Methods):**
- `__init__()`: Constructor, called when object is created
- `__str__()`: Human-readable string representation
- `__repr__()`: Developer-friendly string representation

**The `self` Parameter:**
- Always the first parameter in instance methods
- Refers to the specific object calling the method
- Allows access to instance variables and methods

---

## Namespaces and Variable Scope

Understanding namespaces is crucial for writing clean, bug-free code.

### Scope Resolution Order

When Python encounters a variable name, it searches in this order:

1. **Local scope**: Inside the current function
2. **Enclosing scope**: In any enclosing function
3. **Global scope**: At the module level
4. **Built-in scope**: Built-in names like `print`, `len`, etc.

```python
# Global variable
global_var = "I'm global"

def outer_function():
    # Enclosing scope variable
    enclosing_var = "I'm enclosing"
    
    def inner_function():
        # Local variable
        local_var = "I'm local"
        
        # Can access all three scopes
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_var}")
        print(f"Built-in: {len([1, 2, 3])}")  # len is built-in
    
    inner_function()

outer_function()
```

### Class Namespaces

Classes create their own namespaces, and each instance gets its own namespace too:

```python
class Counter:
    # Class namespace
    total_counters = 0
    
    def __init__(self, start_value=0):
        # Instance namespace
        self.value = start_value
        Counter.total_counters += 1
    
    def increment(self):
        self.value += 1

# Each instance has its own namespace
counter1 = Counter(10)
counter2 = Counter(20)

counter1.increment()
print(f"Counter 1: {counter1.value}")  # 11
print(f"Counter 2: {counter2.value}")  # 20
print(f"Total counters: {Counter.total_counters}")  # 2
```

---

## Example Code Files

The following Python files accompany this reference guide:

1. **`math_tutor.py`** - Enhanced version of the addition tutor
2. **`scope_examples.py`** - Demonstrates variable scope concepts
3. **`parameter_passing.py`** - Shows mutable vs immutable parameter passing
4. **`first_classes.py`** - Complete class examples with exercises
5. **`bank_account.py`** - Real-world class example

---

## Practice Exercises

### Exercise 1: Input Validation
Write a function that prompts the user for a number between 1 and 100, re-prompting until valid input is received.

### Exercise 2: Class Design
Design a `Book` class with the following features:
- Properties: title, author, pages, current_page
- Methods: read_pages(), get_progress(), is_finished()

### Exercise 3: Object Interaction
Create a `Library` class that can store multiple `Book` objects and track which books are available.

### Exercise 4: Debugging Challenge
Find and fix the bugs in the provided code examples.

---

## Study Tips

1. **Practice the REPL**: Use Python's interactive shell to experiment with concepts
2. **Draw Memory Diagrams**: Visualize how objects and references work
3. **Read Error Messages Carefully**: Python's error messages are usually helpful
4. **Start Small**: Begin with simple classes and gradually add complexity
5. **Use Docstrings**: Document your classes and methods for better understanding

---

## Common Pitfalls to Avoid

1. **Forgetting `self`**: Always include `self` as the first parameter in instance methods
2. **Mutable Default Arguments**: Don't use mutable objects as default parameter values
3. **Confusing Class and Instance Variables**: Be clear about what should be shared vs unique
4. **Not Understanding Parameter Passing**: Remember that mutable objects can be modified

---

*This reference guide provides the foundation for object-oriented programming in Python. Refer back to it as we build more complex applications throughout the semester.*
