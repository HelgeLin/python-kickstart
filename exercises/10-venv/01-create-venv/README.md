# Exercise 1: Create Your First Virtual Environment

Create and activate a Python virtual environment for a new project.

## Before You Start

**IMPORTANT: Read Chapter 10 first!**

Before attempting this exercise, make sure you have:
- Read **Chapter 10: Virtual Environments with `venv`** in the `book/10-venv.md` file
- Understood what virtual environments are and why they matter
- Learned the commands to create and activate a venv
- Know how to verify your venv is active

This exercise will help you practice the fundamental workflow of creating isolated Python environments.

## Goal

Create a virtual environment, activate it, and verify that it's working correctly.

## What You'll Learn

- How to create a virtual environment using the `venv` module
- How to activate and deactivate virtual environments
- How to verify which Python and pip you're using
- The difference between global and virtual environment packages

## Instructions

This is a terminal-based exercise. Follow these steps in order:

1. **Navigate to this exercise folder**:
   ```bash
   cd exercises/10-venv/01-create-venv
   ```

2. **Create a virtual environment**:
   - Linux/macOS: `python3 -m venv .venv`
   - Windows: `py -m venv .venv`

3. **Activate the virtual environment**:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows CMD: `.venv\Scripts\activate.bat`

4. **Verify activation**:
   - Check for `(.venv)` in your terminal prompt
   - Run: `which python` (Linux/macOS) or `where python` (Windows)
   - The path should point inside the `.venv` folder

5. **Check installed packages**:
   ```bash
   pip list
   ```
   You should see only a few default packages (pip, setuptools).

6. **Run the verification script**:
   ```bash
   python main.py
   ```
   This will check if your venv is properly activated.

7. **Deactivate when done**:
   ```bash
   deactivate
   ```

## Expected Output

When you run `python main.py` with your venv activated, you should see:

```
=== Virtual Environment Check ===
✓ Virtual environment is active!
✓ Python location: /path/to/exercises/10-venv/01-create-venv/.venv/bin/python
✓ Package location: ['/path/to/exercises/10-venv/01-create-venv/.venv/lib/python3.x/site-packages']

SUCCESS: Your virtual environment is working correctly!
```

## Hints

- The `.venv` folder will be created in the current directory
- Make sure you're in the exercise folder before creating the venv
- On Windows PowerShell, you may need to adjust execution policy (see Chapter 10)
- The terminal prompt should show `(.venv)` when active
- If verification fails, deactivate and reactivate the environment

## Success Criteria

Once your environment works, you've successfully:
- Created a virtual environment using `venv`
- Activated the environment correctly
- Verified that Python and pip point to the venv
- Understood the difference between global and isolated environments

Ready for the next exercise? Great work!