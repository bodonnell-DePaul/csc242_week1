"""
Week 1 Practice Assignment: Getting Started with Git and Classes
CSC 242 - Computer Science II

This is your first GitHub Classroom assignment. The goals are to:
1. Practice the Git workflow (clone, add, commit, push)
2. Verify your development environment is working
3. Review Python class basics
4. Get comfortable with assignment submission process

IMPORTANT: This assignment is for practice. Focus on learning the process,
not just getting the right answer.
"""


class Pet:
    """
    A class representing a pet with basic properties and behaviors.
    
    TODO: Complete the methods marked with TODO comments below.
    """
    
    def __init__(self, name, species, age):
        """
        Initialize a new Pet instance.
        
        TODO: Set the instance variables for name, species, and age.
        Also initialize a hunger_level to 5 (on a scale of 1-10).
        
        Args:
            name (str): The pet's name
            species (str): The type of animal (e.g., "Dog", "Cat", "Bird")
            age (int): The pet's age in years
        """
        # TODO: Implement this method
        pass
    
    def __str__(self):
        """
        Return a string representation of the pet.
        
        TODO: Return a string in the format:
        "Buddy is a 3-year-old Dog"
        
        Returns:
            str: A description of the pet
        """
        # TODO: Implement this method
        pass
    
    def make_sound(self):
        """
        Return the sound this pet makes.
        
        TODO: Return different sounds based on the species:
        - "Dog": "Woof!"
        - "Cat": "Meow!"
        - "Bird": "Tweet!"
        - Any other species: "..."
        
        Returns:
            str: The sound the pet makes
        """
        # TODO: Implement this method
        pass
    
    def feed(self):
        """
        Feed the pet, reducing their hunger level.
        
        TODO: Decrease hunger_level by 2, but don't let it go below 1.
        Return a message about feeding the pet.
        
        Returns:
            str: A message like "You fed Buddy. Hunger level is now 3."
        """
        # TODO: Implement this method
        pass
    
    def play(self):
        """
        Play with the pet, increasing their hunger level.
        
        TODO: Increase hunger_level by 1, but don't let it go above 10.
        Return a message about playing with the pet.
        
        Returns:
            str: A message like "You played with Buddy. Hunger level is now 6."
        """
        # TODO: Implement this method
        pass
    
    def is_hungry(self):
        """
        Check if the pet is hungry.
        
        TODO: Return True if hunger_level is 7 or higher, False otherwise.
        
        Returns:
            bool: True if the pet is hungry, False otherwise
        """
        # TODO: Implement this method
        pass


def main():
    """
    Test function to demonstrate your Pet class.
    
    TODO: Create a pet, demonstrate all the methods, and show the output.
    This function should:
    1. Create a Pet instance with your choice of name, species, and age
    2. Print the pet using str() method
    3. Make the pet make a sound
    4. Feed the pet a couple times
    5. Play with the pet
    6. Check if the pet is hungry
    
    Feel free to be creative with your pet's name and species!
    """
    print("=== Pet Class Demo ===")
    
    # TODO: Create a pet instance
    # Example: my_pet = Pet("Fluffy", "Cat", 2)
    
    # TODO: Demonstrate the pet's methods
    # Print information about your pet
    # Make sounds, feed, play, etc.
    
    print("Demo complete!")


if __name__ == "__main__":
    main()


# =============================================================================
# ASSIGNMENT INSTRUCTIONS
# =============================================================================

"""
STEP 1: COMPLETE THE PET CLASS
- Fill in all the TODO sections in the Pet class above
- Test your code frequently as you work
- Make sure to handle edge cases (hunger level boundaries)

STEP 2: CUSTOMIZE THE MAIN FUNCTION
- Create an interesting pet (creative name and species welcome!)
- Demonstrate all the methods you implemented
- Show the output so we can see your pet in action

STEP 3: GIT WORKFLOW PRACTICE
Make multiple commits as you work. For example:
1. First commit: "Add Pet class constructor"
2. Second commit: "Implement make_sound method"
3. Third commit: "Add feed and play methods"
4. Final commit: "Complete main function demo"

Use meaningful commit messages that describe what you changed!

STEP 4: VERIFY YOUR SUBMISSION
1. Run your code to make sure it works: python week1_practice.py
2. Check git status to ensure all changes are committed
3. Push your final changes: git push origin main
4. Go to GitHub and verify your files are updated

STEP 5: ADD A PERSONAL TOUCH
In the space below, write a brief comment about:
- Your pet's "personality"
- Any creative methods you added (optional)
- What you learned from this assignment
- Any challenges you faced

YOUR REFLECTION:
(Write your reflection here - this will help us understand your experience)

"""

# =============================================================================
# GRADING CRITERIA
# =============================================================================

"""
This assignment will be graded on:

FUNCTIONALITY (60%):
- Pet class constructor works correctly
- All methods are implemented and return correct values
- Edge cases are handled (hunger level limits)
- Main function demonstrates all methods

CODE QUALITY (25%):
- Code is well-commented and readable
- Variable names are descriptive
- Proper Python style and indentation
- No syntax errors

GIT WORKFLOW (15%):
- Multiple meaningful commits
- All changes pushed to GitHub
- Repository is up-to-date at deadline
- Follows assignment submission process

BONUS POINTS:
- Creative or humorous pet implementation
- Additional methods beyond requirements
- Especially clear code documentation
- Help classmates with Git issues (mention in reflection)

Remember: This is a learning exercise! Ask questions if you get stuck.
The goal is to practice the workflow and review Python classes.
"""
