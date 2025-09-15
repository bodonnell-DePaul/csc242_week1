# GitHub Classroom Student Guide
## CSC 242 - Computer Science II

### What is GitHub Classroom?

GitHub Classroom is a tool that helps instructors distribute coding assignments and collect student work. When you accept an assignment through GitHub Classroom:

1. **Individual Repository Created**: You get your own private copy of the assignment
2. **Template Code Provided**: Assignments often include starter files and instructions
3. **Automatic Grading**: Some assignments have automated tests
4. **Submission Tracking**: Instructors can see your progress and final submission

---

## Step-by-Step Assignment Process

### Step 1: Accepting an Assignment

1. **Click the Assignment Link**
   - Your instructor will provide a link like: `https://classroom.github.com/a/ABC123`
   - This link is unique to each assignment

2. **Authorize GitHub Classroom** (First time only)
   - You may need to grant GitHub Classroom permission to access your account
   - This is safe and necessary for the system to work

3. **Select Your Name** (If prompted)
   - Choose your name from the class roster
   - This links your GitHub account to your student identity

4. **Repository Creation**
   - GitHub automatically creates a repository named something like:
   - `assignment-1-yourusername` or `week1-exercises-yourusername`
   - This repository is private to you and the instructor

### Step 2: Cloning Your Assignment Repository

**Important**: Each assignment creates a NEW repository. You'll clone a different repository for each assignment.

```bash
# Example - replace with your actual repository URL
git clone git@github.com:csc242-depaul/assignment-1-johndoe.git

# Navigate into the cloned directory
cd assignment-1-johndoe

# Look at what files are provided
ls -la
```

### Step 3: Understanding the Assignment Structure

Most assignments will contain:

```
assignment-1-johndoe/
├── README.md              # Assignment instructions
├── requirements.txt       # What you need to implement
├── starter_code.py        # Template code to modify
├── test_assignment.py     # Automated tests (don't modify)
└── .gitignore            # Files Git should ignore
```

**Always read the README.md first!** It contains:
- Assignment objectives
- Specific requirements
- Due dates
- Grading criteria
- Submission instructions

### Step 4: Working on Your Assignment

1. **Read All Instructions**
   ```bash
   # View the README file
   cat README.md
   # or open in your text editor
   ```

2. **Make Changes Incrementally**
   - Don't try to complete everything at once
   - Work on one function or class at a time
   - Test your code frequently

3. **Commit Your Progress Regularly**
   ```bash
   # After completing a function or fixing a bug
   git add .
   git commit -m "Implement calculate_average function"
   git push origin main
   ```

### Step 5: Testing Your Code

Many assignments include automated tests. Run them to check your work:

```bash
# If there's a test file
python test_assignment.py

# Or if using pytest
pytest test_assignment.py

# Some assignments may have other testing instructions
```

### Step 6: Final Submission

**Your submission is whatever is in your GitHub repository at the deadline.**

Before the deadline:

1. **Make Sure Everything is Committed**
   ```bash
   git status
   # Should show "nothing to commit, working tree clean"
   ```

2. **Push All Changes**
   ```bash
   git push origin main
   ```

3. **Verify on GitHub**
   - Go to your repository on GitHub.com
   - Check that all your files are there
   - Verify the last commit time is recent

---

## Common Assignment Types

### Type 1: Code Completion
- You're given starter code with TODO comments
- Fill in missing functions or methods
- Example: Complete a Pet class with specific methods

### Type 2: From Scratch
- You're given requirements but minimal starter code
- Create entire classes or programs
- Example: Design a bank account system

### Type 3: Debug and Fix
- You're given broken code
- Find and fix bugs to make tests pass
- Example: Fix errors in provided calculator class

### Type 4: Extend Existing Code
- Start with working code
- Add new features or methods
- Example: Add withdrawal limits to a bank account class

---

## Assignment Workflow Best Practices

### 1. Start Early
- Don't wait until the last minute
- Read the assignment as soon as it's posted
- Ask questions early if anything is unclear

### 2. Commit Frequently
```bash
# Good commit frequency example:
git commit -m "Add Pet class constructor"
git commit -m "Implement make_sound method for dog"
git commit -m "Add input validation to set_age method"
git commit -m "Fix bug in calculate_dog_years function"
```

### 3. Use Meaningful Commit Messages
- **Good**: `"Fix off-by-one error in loop condition"`
- **Bad**: `"fixed bug"`
- **Good**: `"Add error handling for negative ages"`
- **Bad**: `"stuff"`

### 4. Test Before Submitting
```bash
# Run any provided tests
python test_assignment.py

# Test your code with different inputs
python your_assignment.py

# Make sure there are no syntax errors
python -m py_compile your_assignment.py
```

### 5. Read Error Messages Carefully
- Python error messages tell you exactly what's wrong
- Look at the line number mentioned in the error
- Google error messages if you don't understand them

---

## Troubleshooting Common Issues

### Issue: "I can't see my assignment repository"
**Solutions:**
1. Make sure you clicked the assignment link and accepted it
2. Check that you're logged into the correct GitHub account
3. Look in your GitHub repositories list
4. Email instructor if repository wasn't created

### Issue: "My changes aren't showing up on GitHub"
**Solutions:**
```bash
# Check if you have uncommitted changes
git status

# If files are listed as "modified", commit them
git add .
git commit -m "Add latest changes"

# Make sure to push
git push origin main
```

### Issue: "I accidentally deleted important files"
**Solutions:**
```bash
# If you haven't committed the deletion
git checkout HEAD -- filename.py

# If you committed the deletion
git log --oneline  # Find the commit hash before deletion
git checkout COMMIT_HASH -- filename.py
git commit -m "Restore accidentally deleted file"
```

### Issue: "My code works on my computer but fails tests on GitHub"
**Common Causes:**
1. **Different Python versions**: Make sure you're using Python 3.8+
2. **Missing files**: Ensure all necessary files are committed
3. **Hardcoded paths**: Use relative paths, not absolute ones
4. **Input/Output differences**: Check exact output format requirements

### Issue: "I get merge conflicts"
**Solution:**
```bash
# This usually means you edited files on GitHub web interface
# Pull the changes first
git pull origin main

# Resolve any conflicts in your text editor
# Then commit the resolution
git add .
git commit -m "Resolve merge conflict"
git push origin main
```

---

## Working with Automated Tests

### Understanding Test Output

When you run tests, you might see:

```bash
# All tests pass
......
6 tests passed

# Some tests fail
F.F...
2 tests failed, 4 tests passed

# Specific error information
FAIL: test_calculate_average
AssertionError: Expected 75.0, got 73.5
```

### Reading Test Files

Don't modify test files, but you can read them to understand requirements:

```python
# Example test file content
def test_pet_make_sound():
    dog = Pet("Buddy", "Dog", 3)
    assert dog.make_sound() == "Woof!"
    
def test_pet_age_validation():
    pet = Pet("Fluffy", "Cat", 2)
    with pytest.raises(ValueError):
        pet.set_age(-1)  # Should raise error for negative age
```

This tells you:
- Pet class needs constructor with name, species, age parameters
- make_sound() method should return "Woof!" for dogs
- set_age() method should raise ValueError for negative ages

---

## Getting Help

### When to Ask for Help
- You've been stuck for more than 30 minutes
- Error messages don't make sense
- Tests are failing and you don't understand why
- You're not sure what the assignment is asking for

### How to Ask for Help
1. **Be Specific**: Don't just say "it doesn't work"
2. **Include Error Messages**: Copy and paste the exact error
3. **Show Your Code**: Share the specific function you're working on
4. **Explain What You Tried**: What debugging steps have you taken?

### Where to Get Help
- **Office Hours**: Best place for individual help
- **Class Discussion Forum**: Good for clarifying assignment requirements
- **Classmates**: You can discuss concepts, but don't share code solutions
- **Online Resources**: Stack Overflow, Python documentation

---

## Academic Integrity and GitHub

### What's Allowed
- Looking at your own previous assignments
- Discussing concepts and approaches with classmates
- Using online resources to understand Python concepts
- Getting help from instructor and TAs

### What's NOT Allowed
- Copying code from classmates' repositories
- Sharing your repository link with other students
- Looking up complete solutions online
- Having someone else write your code

### Remember
- Your GitHub repositories for assignments are private
- Only you and the instructor can see your code
- Don't make your assignment repositories public
- Don't share your repository URLs with other students

---

## Final Tips for Success

1. **Read Instructions Carefully**: Most mistakes come from not following directions
2. **Start Simple**: Get basic functionality working before adding complexity
3. **Comment Your Code**: Help yourself and the grader understand your logic
4. **Test Edge Cases**: Try unusual inputs to find bugs
5. **Use Version Control**: Commit often so you can go back if needed
6. **Ask Questions**: Don't suffer in silence - get help when stuck
7. **Plan Your Time**: Don't leave assignments until the last minute

Remember: GitHub Classroom is a tool to help you learn and practice professional development workflows. The skills you learn here (version control, collaboration, testing) are essential in the software industry!
