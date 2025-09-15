"""
In-Class Exercises for CSC 242 - Week 1
Git/GitHub Essentials and Object-Oriented Programming Introduction

These exercises are designed to be completed during class time to reinforce
the concepts learned about Git workflows and Python classes.

Author: Brian O'Donnell
IMPORTANT: Practice Git commands as you complete these exercises!
Make a commit after completing each exercise.
"""

import random


# ============================================================================
# GIT PRACTICE CHECKPOINT
# ============================================================================

print("📝 GIT CHECKPOINT: Before starting exercises")
print("=" * 50)
print("Make sure you have:")
print("1. Cloned your assignment repository")
print("2. Navigated to the repository directory")
print("3. Run 'git status' to check current state")
print("4. Ready to make your first commit!")
print()

# TODO: After completing each exercise, make a git commit:
# git add .
# git commit -m "Complete Exercise X: [brief description]"


# ============================================================================
# EXERCISE 1: Fix the Broken Class (10-15 minutes)
# ============================================================================

print("🔧 EXERCISE 1: Debug the Broken Class")
print("=" * 50)
print("The following class has several bugs. Work with a partner to find and fix them!")
print("After fixing, make a commit: git commit -m 'Fix BrokenCalculator class bugs'")

class BrokenCalculator:
    """A calculator class with intentional bugs for students to fix."""
    
    # Bug 1: Missing class variable initialization
    total_calculations = None  # Should be 0
    
    def __init__(self, name):
        # Bug 2: Missing self parameter assignment
        name = name  # Should be self.name = name
        self.history = []
    
    # Bug 3: Missing self parameter
    def add(num1, num2):
        result = num1 + num2
        # Bug 4: Incorrect method call (missing self)
        record_calculation("Addition", num1, num2, result)
        return result
    
    def subtract(self, num1, num2):
        result = num1 - num2
        self.record_calculation("Subtraction", num1, num2, result)
        return result
    
    def record_calculation(self, operation, num1, num2, result):
        # Bug 5: Incorrect class variable access
        total_calculations += 1  # Should be BrokenCalculator.total_calculations += 1
        calculation = f"{operation}: {num1} and {num2} = {result}"
        self.history.append(calculation)
    
    def get_history(self):
        return self.history

# TODO: Students should create a fixed version below
print("Create a FixedCalculator class that corrects all the bugs!")


# ============================================================================
# EXERCISE 2: Quick Class Creation + Git Practice (15 minutes)
# ============================================================================

print("\n🏗️ EXERCISE 2: Create a Pet Class")
print("=" * 50)
print("Create a Pet class with the following requirements:")
print("1. Constructor takes name, species, and age")
print("2. Method: make_sound() - returns appropriate sound based on species")
print("3. Method: have_birthday() - increases age by 1")
print("4. Method: is_adult() - returns True if age >= 2")
print("5. String representation shows name and species")
print()
print("GIT PRACTICE: After completing the Pet class:")
print("git add .")
print("git commit -m 'Add Pet class with basic methods'")
print("git push origin main")

# Students work here - example solution at bottom of file

class Pet:
    """
    TODO: Implement the Pet class according to the requirements above.
    Remember to test your methods after implementing them!
    """
    pass


# ============================================================================
# EXERCISE 3: GitHub Repository Exploration (10 minutes)
# ============================================================================

print("\n📁 EXERCISE 3: GitHub Repository Exploration")
print("=" * 50)
print("Let's explore GitHub repositories to understand how professionals use Git:")
print()
print("1. Go to your assignment repository on GitHub.com")
print("2. Look at the commit history - can you see your commits?")
print("3. Explore the 'Insights' tab - what information is available?")
print("4. Find a classmate's repository (ask for their GitHub username)")
print("5. Compare your Pet class implementations (respectfully!)")
print()
print("Discussion Questions:")
print("- How does seeing commit history help with understanding code changes?")
print("- What makes a good commit message?")
print("- How could this be useful for team projects?")


# ============================================================================
# EXERCISE 4: Object Interaction Challenge (20 minutes)
# ============================================================================

print("\n🎮 EXERCISE 4: Game Character System")
print("=" * 50)
print("Create a simple RPG character system:")

class GameCharacter:
    """Base character class for students to extend."""
    
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.max_health = health
        self.level = 1
    
    def take_damage(self, damage):
        """Character takes damage."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! Health: {self.health}/{self.max_health}")
    
    def heal(self, amount):
        """Character heals."""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {amount}! Health: {self.health}/{self.max_health}")
    
    def is_alive(self):
        """Check if character is alive."""
        return self.health > 0
    
    def __str__(self):
        return f"{self.name} (Level {self.level}, Health: {self.health}/{self.max_health})"

print("Your tasks:")
print("1. Create a Warrior class that inherits from GameCharacter")
print("2. Add an 'attack' method that deals 15-25 damage to another character")
print("3. Create a Mage class with a 'cast_spell' method")
print("4. Create a battle simulation between characters")
print()
print("GIT CHECKPOINT: After completing each class:")
print("git add .")
print("git commit -m 'Add Warrior class with attack method'")
print("git commit -m 'Add Mage class with spell casting'")
print("git commit -m 'Complete battle simulation'")


# ============================================================================
# EXERCISE 5: Collaborative Coding Challenge (15 minutes)
# ============================================================================

print("\n👥 EXERCISE 5: Peer Code Review")
print("=" * 50)
print("Practice collaborative development:")
print()
print("1. Find a partner in class")
print("2. Share your GitHub repository URLs with each other")
print("3. Look at your partner's Pet class implementation")
print("4. Discuss differences in your approaches:")
print("   - Did you implement make_sound() differently?")
print("   - How did you handle the birthday method?")
print("   - What creative touches did each person add?")
print()
print("5. Write constructive feedback in the discussion:")
print("   - What you liked about their implementation")
print("   - One suggestion for improvement")
print("   - One thing you learned from their approach")
print()
print("This simulates real-world code review processes!")


# ============================================================================
# EXERCISE 6: Git Troubleshooting Scenarios (10 minutes)
# ============================================================================

print("\n🔧 EXERCISE 6: Git Troubleshooting")
print("=" * 50)
print("Practice handling common Git situations:")
print()
print("Scenario 1: 'I forgot to commit before making new changes'")
print("Solution: git add . && git commit -m 'Save current work'")
print()
print("Scenario 2: 'My file changes aren't showing up on GitHub'")
print("Check: git status, then git push origin main")
print()
print("Scenario 3: 'I want to see what I changed'")
print("Solution: git diff (before committing) or git log --oneline")
print()
print("Try these commands in your repository:")
print("1. git log --oneline  # See your commit history")
print("2. git status         # Check current status")
print("3. git diff          # See any current changes")
print()
print("Each person try one command and share what you see!")


# ============================================================================
# BONUS EXERCISE: Real-World Modeling (If time permits)
# ============================================================================

print("\n🏫 BONUS: University Course System")
print("=" * 50)
print("For advanced students who finish early:")
print("Model a university course registration system:")

class Course:
    """A university course."""
    
    def __init__(self, course_code, title, credits, max_students=30):
        self.course_code = course_code
        self.title = title
        self.credits = credits
        self.max_students = max_students
        self.enrolled_students = []
    
    def add_student(self, student_name):
        """Add a student to the course."""
        if len(self.enrolled_students) >= self.max_students:
            return False
        if student_name not in self.enrolled_students:
            self.enrolled_students.append(student_name)
            return True
        return False
    
    def drop_student(self, student_name):
        """Remove a student from the course."""
        if student_name in self.enrolled_students:
            self.enrolled_students.remove(student_name)
            return True
        return False
    
    def get_enrollment_count(self):
        """Get current enrollment count."""
        return len(self.enrolled_students)
    
    def is_full(self):
        """Check if course is full."""
        return len(self.enrolled_students) >= self.max_students
    
    def __str__(self):
        return f"{self.course_code}: {self.title} ({self.get_enrollment_count()}/{self.max_students})"

print("Your tasks:")
print("1. Create a CourseSchedule class that manages multiple courses")
print("2. Add methods to find courses by code, list available courses, etc.")
print("3. Create a Student class that tracks enrolled courses")
print("4. Implement enrollment logic with prerequisites")


# ============================================================================
# EXERCISE 5: Quick Debugging Challenge (5-10 minutes)
# ============================================================================

print("\n🐛 EXERCISE 5: Scope and Parameter Mystery")
print("=" * 50)
print("Predict the output of this code, then run it to check your answer!")

def mystery_function():
    x = 10
    y = [1, 2, 3]
    
    def inner_function(a, b):
        a = a + 5
        b.append(4)
        print(f"Inside inner: a={a}, b={b}")
    
    inner_function(x, y)
    print(f"After inner: x={x}, y={y}")

print("What will this print? Discuss with your partner, then uncomment the line below:")
# mystery_function()


# ============================================================================
# EXERCISE 6: Class Design Challenge (Bonus - if time permits)
# ============================================================================

print("\n🏆 BONUS EXERCISE: Library Management System")
print("=" * 50)
print("Design a library management system with the following classes:")
print("1. Book - title, author, ISBN, available status")
print("2. Member - name, member ID, borrowed books list")
print("3. Library - collection of books, member management")
print("Include methods for checking out and returning books!")


# ============================================================================
# SOLUTION EXAMPLES (for instructor reference)
# ============================================================================

def show_solutions():
    """Solutions for the exercises (for instructor use)."""
    
    print("\n" + "="*60)
    print("SOLUTIONS (for instructor reference)")
    print("="*60)
    
    # Exercise 1 Solution
    class FixedCalculator:
        """Corrected version of the broken calculator."""
        
        total_calculations = 0  # Fixed: Initialize to 0
        
        def __init__(self, name):
            self.name = name  # Fixed: Added self
            self.history = []
        
        def add(self, num1, num2):  # Fixed: Added self parameter
            result = num1 + num2
            self.record_calculation("Addition", num1, num2, result)  # Fixed: Added self
            return result
        
        def subtract(self, num1, num2):
            result = num1 - num2
            self.record_calculation("Subtraction", num1, num2, result)
            return result
        
        def record_calculation(self, operation, num1, num2, result):
            FixedCalculator.total_calculations += 1  # Fixed: Proper class variable access
            calculation = f"{operation}: {num1} and {num2} = {result}"
            self.history.append(calculation)
        
        def get_history(self):
            return self.history
    
    # Exercise 2 Solution
    class Pet:
        """A pet with basic behaviors."""
        
        def __init__(self, name, species, age):
            self.name = name
            self.species = species
            self.age = age
        
        def make_sound(self):
            sounds = {
                "dog": "Woof!",
                "cat": "Meow!",
                "bird": "Tweet!",
                "fish": "...", 
            }
            sound = sounds.get(self.species.lower(), "Unknown sound")
            print(f"{self.name} says {sound}")
        
        def have_birthday(self):
            self.age += 1
            print(f"Happy birthday {self.name}! Now {self.age} years old.")
        
        def is_adult(self):
            return self.age >= 2
        
        def __str__(self):
            return f"{self.name} the {self.species}"
    
    # Exercise 3 Solution
    class Warrior(GameCharacter):
        """A warrior character with attack abilities."""
        
        def __init__(self, name):
            super().__init__(name, health=120)
            self.armor = 5
        
        def attack(self, target):
            """Attack another character."""
            if not self.is_alive():
                print(f"{self.name} cannot attack - defeated!")
                return
            
            damage = random.randint(15, 25)
            print(f"{self.name} attacks {target.name}!")
            target.take_damage(damage)
    
    class Mage(GameCharacter):
        """A mage character with spell abilities."""
        
        def __init__(self, name):
            super().__init__(name, health=80)
            self.mana = 50
        
        def cast_spell(self, target):
            """Cast a spell on another character."""
            if not self.is_alive():
                print(f"{self.name} cannot cast spells - defeated!")
                return
            
            if self.mana < 10:
                print(f"{self.name} is out of mana!")
                return
            
            damage = random.randint(20, 30)
            self.mana -= 10
            print(f"{self.name} casts a spell on {target.name}!")
            target.take_damage(damage)
    
    print("Solutions implemented. Run show_solutions() to see the code.")


# ============================================================================
# INTERACTIVE CLASS ACTIVITIES
# ============================================================================

def class_activity_1():
    """Quick think-pair-share activity."""
    print("\n🤔 THINK-PAIR-SHARE: Class vs Instance Variables")
    print("=" * 50)
    print("Look at this code and discuss with your partner:")
    
    code = '''
class Counter:
    total_count = 0
    
    def __init__(self):
        self.my_count = 0
        Counter.total_count += 1
    
    def increment(self):
        self.my_count += 1

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c2.increment()
    '''
    
    print(code)
    print("\nQuestions to discuss:")
    print("1. What will Counter.total_count be?")
    print("2. What will c1.my_count be?") 
    print("3. What will c2.my_count be?")
    print("4. What's the difference between total_count and my_count?")


def class_activity_2():
    """Code prediction activity."""
    print("\n🔮 PREDICT THE OUTPUT")
    print("=" * 50)
    print("What will this code print? Write your prediction, then we'll run it!")
    
    code = '''
def modify_data(num, lst):
    num = num * 2
    lst.append(num)
    return num

x = 10
y = [1, 2, 3]
result = modify_data(x, y)
print(f"x={x}, y={y}, result={result}")
    '''
    
    print(code)
    input("Press Enter after you've made your prediction...")
    
    # Run the actual code
    def modify_data(num, lst):
        num = num * 2
        lst.append(num)
        return num
    
    x = 10
    y = [1, 2, 3]
    result = modify_data(x, y)
    print(f"Actual output: x={x}, y={y}, result={result}")


if __name__ == "__main__":
    print("👨‍🏫 IN-CLASS EXERCISES - CSC 242 Week 1")
    print("Use these exercises during class time to reinforce concepts!")
    print("\nUncomment specific exercises in the main section to run them.")
    
    # Uncomment these to run during class:
    # class_activity_1()
    # class_activity_2()
    # show_solutions()  # For instructor use
