# Git Command Quick Reference
## CSC 242 - Computer Science II

### Initial Setup (One Time Only)
```bash
# Set your identity
git config --global user.name "Your Full Name"
git config --global user.email "your.email@student.depaul.edu"

# Set default branch name
git config --global init.defaultBranch main

# Check your configuration
git config --list
```

### SSH Key Setup
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@student.depaul.edu"

# Display public key (copy this to GitHub)
# Windows:
type ~/.ssh/id_ed25519.pub
# Mac/Linux:
cat ~/.ssh/id_ed25519.pub

# Test SSH connection
ssh -T git@github.com
```

### Daily Workflow Commands

#### Getting Started with an Assignment
```bash
# Clone repository from GitHub Classroom
git clone git@github.com:csc242-depaul/assignment-name-yourusername.git

# Navigate into the project directory
cd assignment-name-yourusername

# Check current status
git status
```

#### Working on Your Code
```bash
# Check what files have changed
git status

# Add specific files to staging
git add filename.py

# Add all changed files to staging
git add .

# Commit your changes with a message
git commit -m "Descriptive message about what you changed"

# Push changes to GitHub
git push origin main
```

#### Checking Your Work
```bash
# View recent commits
git log --oneline

# See detailed changes in files
git diff

# Check if you have any uncommitted changes
git status

# Pull latest changes from GitHub (if working with others)
git pull origin main
```

### Common Situations and Solutions

#### "I forgot to add a file to my last commit"
```bash
# Add the forgotten file
git add forgotten_file.py

# Amend the previous commit
git commit --amend --no-edit

# Push with force (only if you haven't shared the commit yet)
git push origin main --force
```

#### "I want to undo my last commit but keep the changes"
```bash
# Undo commit but keep files staged
git reset --soft HEAD~1

# Undo commit and unstage files (but keep changes in files)
git reset HEAD~1
```

#### "I want to see what changed in a specific commit"
```bash
# Show changes in the most recent commit
git show

# Show changes in a specific commit (replace abc123 with actual hash)
git show abc123
```

#### "I want to ignore certain files"
```bash
# Create a .gitignore file
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".DS_Store" >> .gitignore

# Add and commit the .gitignore file
git add .gitignore
git commit -m "Add .gitignore file"
```

### Good Commit Message Examples
- ✅ `"Add Pet class with constructor and make_sound method"`
- ✅ `"Fix bug in calculate_average function"`
- ✅ `"Complete exercise 2 - implement bank account withdrawal"`
- ✅ `"Update README with project description"`
- ✅ `"Refactor code to improve readability"`

### Poor Commit Message Examples
- ❌ `"stuff"`
- ❌ `"fixed it"`
- ❌ `"homework"`
- ❌ `"changes"`
- ❌ `"asdf"`

### Emergency Commands (Use with Caution)

#### "I want to completely undo all uncommitted changes"
```bash
# This will permanently delete all uncommitted changes!
git reset --hard HEAD

# For a specific file only
git checkout HEAD -- filename.py
```

#### "I want to delete the last commit completely"
```bash
# This will permanently delete the last commit!
git reset --hard HEAD~1
git push origin main --force
```

### Getting Help

#### Built-in Help
```bash
# Get help for any git command
git help commit
git help status
git help push

# Quick help
git commit --help
```

#### Check Repository Information
```bash
# Show remote repository URL
git remote -v

# Show current branch
git branch

# Show last few commits
git log --oneline -5
```

### Troubleshooting Common Errors

#### Error: "fatal: not a git repository"
**Solution**: You're not in a Git repository directory. Use `cd` to navigate to your project folder.

#### Error: "Permission denied (publickey)"
**Solution**: SSH key not set up correctly. Check that your SSH key is added to GitHub.

#### Error: "Your branch is ahead of 'origin/main'"
**Solution**: You have commits that aren't pushed yet. Run `git push origin main`.

#### Error: "Please tell me who you are"
**Solution**: Set up your Git identity with the config commands at the top of this sheet.

#### Error: "refusing to merge unrelated histories"
**Solution**: Usually happens when repositories get out of sync. Contact instructor for help.

### Best Practices

1. **Commit Often**: Make small, logical commits rather than huge ones
2. **Meaningful Messages**: Write commit messages that explain what and why
3. **Check Status**: Always run `git status` before committing
4. **Pull Before Push**: If working with others, pull changes before pushing
5. **Review Changes**: Use `git diff` to review what you're about to commit
6. **Backup**: Your code is backed up on GitHub, but commit regularly
7. **Ask for Help**: Don't struggle alone - ask questions early

### Resources
- **GitHub Documentation**: [docs.github.com](https://docs.github.com)
- **Interactive Git Tutorial**: [learngitbranching.js.org](https://learngitbranching.js.org)
- **Git Handbook**: [guides.github.com/introduction/git-handbook](https://guides.github.com/introduction/git-handbook)
- **Office Hours**: When you're stuck, come get help!
