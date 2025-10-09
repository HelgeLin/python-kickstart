# Exercise 2: Install and Manage Packages

Learn to install packages in your virtual environment and create a requirements file.

## Before You Start

**IMPORTANT: Complete Exercise 1 first!**

Before attempting this exercise, make sure you have:
- Completed Exercise 1 (creating and activating a venv)
- Read **Chapter 10: Virtual Environments with `venv`**
- Understood how to use `pip install` in a virtual environment
- Learned about `requirements.txt` files

This exercise will help you practice installing packages and managing dependencies.

## Goal

Install the `requests` library in a virtual environment, use it in a program, and create a requirements file for sharing.

## What You'll Learn

- How to install packages using pip in a venv
- How to verify installed packages with `pip list`
- How to create a `requirements.txt` file
- How to use an installed package in your code
- The importance of isolating dependencies per project

## Instructions

1. **Navigate to this exercise folder**:
   ```bash
   cd exercises/10-venv/02-install-packages
   ```

2. **Create and activate a virtual environment**:
   - Create: `python3 -m venv .venv` (or `py -m venv .venv` on Windows)
   - Activate: `source .venv/bin/activate` (or `.venv\Scripts\Activate.ps1` on Windows)

3. **Install the requests package**:
   ```bash
   pip install requests
   ```

4. **Verify the installation**:
   ```bash
   pip list
   ```
   You should see `requests` and its dependencies.

5. **Create a requirements file**:
   ```bash
   pip freeze > requirements.txt
   ```

6. **Run the program**:
   ```bash
   python main.py
   ```
   This will test if the requests library is working correctly.

7. **Examine the requirements file**:
   Open `requirements.txt` and see all installed packages with their versions.

## Expected Output

When you run `python main.py`, you should see:

```
=== Package Installation Check ===
✓ Virtual environment is active!
✓ requests library is installed (version X.XX.X)
✓ Making a test API request...
✓ API request successful!

SUCCESS: You've installed and used the requests package!

Requirements file created: requirements.txt
Share this file with teammates so they can install the same packages.
```

## Hints

- Make sure your venv is activated before installing packages
- The `requests` library is used for making HTTP requests
- `pip freeze` saves all installed packages and their exact versions
- The requirements file can be used to recreate the environment later
- Check that `(.venv)` appears in your terminal prompt

## Challenge

After completing the basic exercise, try this:

1. Deactivate your venv: `deactivate`
2. Create a new folder called `test-recreation`
3. Create a new venv in that folder
4. Activate it
5. Install packages from your requirements file: `pip install -r ../02-install-packages/requirements.txt`
6. Verify that the same packages are installed

## Success Criteria

Once your program works, you've successfully:
- Created a virtual environment for a project
- Installed a third-party package using pip
- Used the installed package in a Python program
- Created a requirements.txt file
- Understood how to share dependencies with others

Ready for the next exercise? Great work!