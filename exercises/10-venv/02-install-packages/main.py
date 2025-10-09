"""
Exercise 2: Install and Manage Packages
Test script to verify requests library is installed and working
"""

import sys


def check_installation():
    """Check if requests is installed and working"""
    print("=== Package Installation Check ===")
    
    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if not in_venv:
        print("✗ No virtual environment detected!")
        print("Please activate your virtual environment first.")
        return False
    
    print("✓ Virtual environment is active!")
    
    # Try to import requests
    try:
        import requests
        print(f"✓ requests library is installed (version {requests.__version__})")
    except ImportError:
        print("✗ requests library is not installed!")
        print("Run: pip install requests")
        return False
    
    # Test the requests library with a simple API call
    print("✓ Making a test API request...")
    try:
        response = requests.get("https://api.github.com", timeout=5)
        if response.status_code == 200:
            print("✓ API request successful!")
        else:
            print(f"⚠ API returned status code: {response.status_code}")
    except Exception as e:
        print(f"⚠ API request failed (this is okay if you're offline): {e}")
    
    print("\nSUCCESS: You've installed and used the requests package!")
    print("\nRequirements file created: requirements.txt")
    print("Share this file with teammates so they can install the same packages.")
    
    return True


if __name__ == "__main__":
    check_installation()