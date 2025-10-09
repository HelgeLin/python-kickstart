"""
Exercise 1: Create Your First Virtual Environment
Verification script to check if venv is properly activated
"""

import sys
import site


def check_venv():
    """Check if a virtual environment is active"""
    print("=== Virtual Environment Check ===")
    
    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print("✓ Virtual environment is active!")
        print(f"✓ Python location: {sys.executable}")
        print(f"✓ Package location: {site.getsitepackages()}")
        print("\nSUCCESS: Your virtual environment is working correctly!")
        return True
    else:
        print("✗ No virtual environment detected!")
        print(f"✗ Python location: {sys.executable}")
        print("\nPlease activate your virtual environment and try again.")
        print("Hint: Run 'source .venv/bin/activate' (Linux/macOS)")
        print("      or '.venv\\Scripts\\Activate.ps1' (Windows)")
        return False


if __name__ == "__main__":
    check_venv()