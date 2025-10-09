# Exercise 3: Share and Recreate Environments

Learn how to share your project setup with others and recreate environments from requirements files.

## Before You Start

**IMPORTANT: Complete Exercise 2 first!**

Before attempting this exercise, make sure you have:
- Completed Exercise 1 and 2
- Read **Chapter 10: Virtual Environments with `venv`**
- Understood how `requirements.txt` works
- Know how to install from a requirements file

This exercise simulates sharing a project with a teammate who needs to set up the same environment.

## Goal

Recreate a Python environment from a provided `requirements.txt` file and verify that the project works correctly.

## What You'll Learn

- How to install dependencies from a requirements file
- Why `requirements.txt` is essential for team collaboration
- How to verify that an environment matches the project's needs
- The workflow for setting up a shared project

## Instructions

This exercise includes a pre-made `requirements.txt` file that specifies the packages needed for the project.

1. **Navigate to this exercise folder**:
   ```bash
   cd exercises/10-venv/03-share-environment
   ```

2. **Examine the requirements file**:
   Open `requirements.txt` to see what packages are needed.

3. **Create a new virtual environment**:
   - Create: `python3 -m venv .venv` (or `py -m venv .venv` on Windows)
   - Activate: `source .venv/bin/activate` (or `.venv\Scripts\Activate.ps1` on Windows)

4. **Install all dependencies at once**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Verify the installation**:
   ```bash
   pip list
   ```
   Check that all packages from requirements.txt are installed.

6. **Run the program**:
   ```bash
   python main.py
   ```
   This will verify that all required packages are working.

7. **Compare your environment**:
   ```bash
   pip freeze
   ```
   The output should match the requirements.txt file.

## Expected Output

When you run `python main.py`, you should see:

```
=== Environment Recreation Check ===
✓ Virtual environment is active!
✓ Checking required packages...
  ✓ requests (version X.XX.X) - installed
  ✓ colorama (version X.X.X) - installed
✓ All required packages are installed!

Testing package functionality...
✓ requests: Successfully made API call
✓ colorama: Color formatting works

SUCCESS: Environment recreated successfully!
This is how you'd set up a teammate's project on your computer.
```

## Hints

- The `-r` flag tells pip to install from a requirements file
- All packages and their dependencies will be installed automatically
- Your teammate's exact package versions will be installed
- This ensures everyone has the same development environment
- Always create a fresh venv before installing from requirements.txt

## Real-World Scenario

This is exactly what happens when you:
- Clone a project from GitHub
- Join a team working on an existing project
- Deploy your code to a server
- Share your project with a teacher for grading

The `requirements.txt` file ensures everyone can run your code with the correct dependencies.

## Challenge

After completing the exercise, try this workflow:

1. Create your own project in a new folder
2. Create a venv and activate it
3. Install 2-3 packages of your choice
4. Create a requirements.txt with `pip freeze`
5. Share the requirements.txt with a classmate
6. Have them recreate your environment

## Success Criteria

Once your program works, you've successfully:
- Created a virtual environment from scratch
- Installed dependencies from a requirements file
- Verified that all packages work correctly
- Understood the workflow for collaborative projects
- Learned how to reproduce environments across computers

Congratulations! You now know how to work with virtual environments like a professional Python developer!