# Chapter 10: Virtual Environments with `venv`

## Learning Objectives

By the end of this chapter, you will be able to:
- Understand what virtualization is and why it matters in programming
- Create and activate Python virtual environments using `venv`
- Install and manage project-specific packages
- Integrate virtual environments with VS Code
- Share your project setup with others using `requirements.txt`

## Introduction

Before we can start installing third-party libraries like `requests`, `pygame`, or `numpy`, we must first learn how to create isolated **virtual environments**. This isn't just a "best practice" anymore—it's **required** on modern systems.

In the past, you could install Python packages globally without major issues. Today, that approach often fails or breaks your system. Virtual environments solve this problem by creating isolated spaces for each project's dependencies.

### Why Virtual Environments Matter

Modern Python development requires virtual environments for several reasons:

1. **System Protection**: Many operating systems use Python internally. Installing packages globally can break system tools.
2. **Dependency Isolation**: Different projects can use different versions of the same package without conflicts.
3. **Reproducibility**: You can share exact package versions with teammates or recreate environments on other computers.
4. **Clean Organization**: Each project has its own dependencies, making debugging easier.

## Core Concepts

### What is Virtualization?

**Virtualization** means creating an isolated environment on top of something else so it behaves like its own system—without changing the host machine.

There are different levels of virtualization:

- **Machine/OS virtualization** (e.g., VirtualBox): A complete guest operating system running inside your computer
- **Containerization** (e.g., Docker): Lightweight isolated packages that share the same OS kernel
- **Language virtualization** (e.g., Python `venv`, Node `nvm`): Isolated project environments for libraries and dependencies

### Understanding Through Analogies

**The Kitchen Analogy**: Everyone cooks in the same kitchen (your computer), but each group uses its own ingredient box (virtual environment) with the correct spices (packages). This way, one group using curry powder doesn't accidentally affect another group making Italian food.

**The Library Analogy**: The library building is your operating system. Your study cubicle is your virtual environment—you only bring the books (packages) you need for your specific assignment. Other students' books don't clutter your space.

### What is a Python Virtual Environment?

A **virtual environment** (venv) is a self-contained directory that includes:

- Its own installed Python packages (in a `site-packages` folder)
- Its own scripts (like `black`, `pytest`, etc.)
- An activation mechanism that updates your `PATH` so the correct Python and pip are used

**Important**: `venv` does not install a new Python interpreter from scratch. It reuses your system's Python installation but isolates the packages per project.

### Creating Your First Virtual Environment

Let's walk through the complete workflow step by step.

#### Step 1: Choose a Project Folder

First, decide where your project will live. Create a dedicated folder and navigate to it:

```bash
# Example: Create a project folder
mkdir my_app
cd my_app
```

#### Step 2: Create the Virtual Environment

Run this command in your project directory:

**Linux/macOS:**
```bash
python3 -m venv .venv
```

**Windows:**
```bash
py -m venv .venv
```

This creates a folder named `.venv` containing your isolated Python environment. The dot makes it hidden on Linux/macOS systems.

The name `.venv` is a convention. You could use any name (`venv`, `env`, etc.), but `.venv` is recommended as it's automatically recognized by most tools.

#### Step 3: Activate the Virtual Environment

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows PowerShell:**
```bash
.venv\Scripts\Activate.ps1
```

**Windows CMD:**
```bash
.venv\Scripts\activate.bat
```

When activated, you'll see a prefix in your terminal prompt:

```bash
(.venv) user@computer:~/my_app$
```

You need to activate the environment every time you open a new terminal window for this project.

#### Step 4: Install Packages

Now that your virtual environment is active, you can install packages:

```bash
pip install requests
pip install pytest
```

Verify the installation:

```bash
pip list
```

You should see only the packages you installed, plus `pip` and `setuptools`.

#### Step 5: Save Dependencies

Create a `requirements.txt` file to track all installed packages:

```bash
pip freeze > requirements.txt
```

This creates a file like:

```txt
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
requests==2.31.0
urllib3==2.0.4
```

This file allows you to recreate the exact environment on another computer.

#### Step 6: Deactivate When Done

When you're finished working on the project:

```bash
deactivate
```

This returns you to your system's global Python environment.

### Integrating with VS Code

VS Code has excellent support for Python virtual environments. Here's how to configure it:

1. Open your project folder in VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
3. Type "Python: Select Interpreter"
4. Choose the interpreter from your `.venv` folder:
   - Linux/macOS: `.venv/bin/python`
   - Windows: `.venv\Scripts\python.exe`

Once configured, VS Code will:

- Automatically activate the venv when you open a terminal
- Use the correct Python for running files
- Show package versions in IntelliSense
- Run the debugger with the correct environment

### Recreating an Environment

When you or a teammate need to set up the project on another computer:

```bash
# Navigate to project folder
cd /path/to/my_app

# Create new venv
python3 -m venv .venv  # or py -m venv .venv on Windows

# Activate it
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows

# Install all dependencies
pip install -r requirements.txt
```
### Version Control and .gitignore

When sharing your project through version control systems like Git, it's crucial to understand what should and shouldn't be included in your repository.

#### What is .gitignore?

A `.gitignore` file tells Git which files and folders to ignore when tracking changes. This prevents unnecessary or problematic files from being added to your repository.

#### Why Not Include Virtual Environments?

Virtual environments should **never** be committed to version control for several reasons:

1. **Large Size**: A `.venv` folder can contain hundreds of megabytes of files, making your repository bloated and slow to clone.

2. **Platform-Specific**: Virtual environments contain platform-specific binaries that won't work across different operating systems. A Windows venv won't work on macOS or Linux.

3. **Unnecessary**: Anyone can recreate your exact environment using `requirements.txt`, which is tiny in comparison.

4. **Security**: Virtual environments may contain cached credentials or sensitive information.

#### Creating a .gitignore File

Create a file named `.gitignore` in your project root with these essential entries:

```
# Virtual environments
.venv/
venv/
env/

# Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd

# IDE settings
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```

#### What TO Include in Version Control

You should commit these files:

- **requirements.txt**: List of dependencies
- **Source code**: Your `.py` files
- **README.md**: Project documentation
- **Configuration files**: Settings, but not secrets

#### The Correct Workflow

When sharing a project:

1. **Developer A**:
   - Creates project with venv
   - Installs packages
   - Creates `requirements.txt` with `pip freeze`
   - Adds `.venv/` to `.gitignore`
   - Commits code and `requirements.txt` to Git

2. **Developer B**:
   - Clones the repository
   - Creates their own venv
   - Installs from `requirements.txt`
   - Starts working

This ensures everyone has a working environment without transferring gigabytes of unnecessary files.


### Why Virtual Environments Are Required Today

In the past, you could install Python packages globally without issues. Today, several factors make this approach problematic:

**System Python Protection**: Modern Linux systems (like Raspberry Pi OS, Ubuntu, Mint) rely on Python internally for tools like `apt`, `bluetoothctl`, and `NetworkManager`. Installing packages globally can break your system.

You may encounter errors like:

```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
```

**PEP 668 Standard**: Since Python 3.11, systems include a file called `EXTERNALLY-MANAGED` that prevents global `pip install` by default. Virtual environments are now the official Python standard practice.

**Platform-Specific Dependencies**: Packages may require different compiled binaries on different platforms. Virtual environments handle this automatically.

**Shared Environments**: In computer labs, one student's global install can affect another's project. Virtual environments ensure isolation.

### Other Virtualization Tools

As you advance in Python, you'll encounter other tools:

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **venv** | Isolates packages for a project | Every Python project (recommended for beginners) |
| **pyenv** | Manages multiple Python versions | Need Python 3.9, 3.10, 3.11, etc. |
| **virtualenv** | Older venv alternative | Legacy projects |
| **Docker** | Full OS-level environment | Complex apps, deployment |
| **conda** | Manages Python + non-Python dependencies | Data science, scientific computing |

For this course, stick with `venv`. It's built into Python, simple to use, and covers all your needs as a beginner.

## Common Mistakes

### Forgetting to Activate the Virtual Environment

```bash
# Wrong: Installing without activating venv
pip install requests

# Correct: Activate first
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows
pip install requests
```

Check for the `(.venv)` prefix in your terminal prompt to confirm activation.

### Using sudo with pip

Never use `sudo pip install`. This installs packages globally and can break your system. Always use a virtual environment instead.

### Mixing pip and pip3

Once your venv is active, use `pip` (not `pip3`). You can verify which pip you're using:

```bash
# Linux/macOS
which pip

# Windows
where pip
```

The path should be inside your `.venv` directory.

### Wrong VS Code Interpreter

If your code can't find installed packages, check that VS Code is using the correct interpreter. Look at the bottom-left status bar or use `Ctrl+Shift+P` → "Python: Select Interpreter".

### Committing Virtual Environments to Git

Never commit the `.venv` folder to version control. Add it to your `.gitignore` file:

```
# .gitignore
.venv/
__pycache__/
*.pyc
```

Only commit the `requirements.txt` file, which others can use to recreate the environment.

### Windows PowerShell Execution Policy

On Windows, you may encounter an error when activating:

```
.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled
```

Fix this by running PowerShell as administrator and executing:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Practice

Try these exercises to practice what you've learned:

1. Create a new project folder for a practice app
2. Create a virtual environment using `venv`
3. Activate the environment
4. Install the `requests` package
5. Create a `requirements.txt` file using `pip freeze`
6. Verify your setup using the diagnostic commands below
7. Deactivate the environment

### Verification Commands

Use these commands to verify your setup:

```bash
# Check which Python you're using
which python    # Linux/macOS
where python    # Windows

# Check which pip you're using
which pip       # Linux/macOS
where pip       # Windows

# Full diagnostic
python -c "import sys, site; print('Python:', sys.executable); print('Packages:', site.getsitepackages())"
```

All paths should point inside your `.venv` directory when the environment is activated.

## Summary

In this chapter, you learned:

- Virtual environments create isolated spaces for project dependencies
- `venv` is Python's built-in tool for creating virtual environments
- Modern systems require virtual environments due to PEP 668 and system protection
- Always activate your venv before installing packages
- Use `requirements.txt` to share your project setup with others
- VS Code can be configured to automatically use your virtual environment

**The Golden Rule**: One project → One folder → One venv → One requirements.txt

Virtual environments aren't optional anymore—they're how Python stays stable, portable, and safe on modern systems. Now you're ready to safely install and use third-party libraries in your projects.

## Quick Reference

### Creating and Activating

```bash
# Create venv
python3 -m venv .venv        # Linux/macOS
py -m venv .venv             # Windows

# Activate
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\Activate.ps1   # Windows PowerShell
.venv\Scripts\activate.bat   # Windows CMD

# Deactivate
deactivate
```

### Managing Packages

```bash
# Install packages
pip install package_name
pip install -r requirements.txt

# Save dependencies
pip freeze > requirements.txt

# List installed packages
pip list

# Uninstall a package
pip uninstall package_name
```

### Checklist for New Projects

- [ ] Create a dedicated project folder
- [ ] Create `.venv` in project root
- [ ] Activate `.venv` before installing anything
- [ ] Install packages with `pip install`
- [ ] Save dependencies with `pip freeze > requirements.txt`
- [ ] Select correct interpreter in VS Code
- [ ] Add `.venv/` to your `.gitignore` file
- [ ] Include `requirements.txt` in version control

In the next chapters, we'll explore popular Python packages and build projects using the virtual environments you've learned to create.