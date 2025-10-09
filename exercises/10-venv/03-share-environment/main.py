"""
Exercise 3: Share and Recreate Environments
Test script to verify environment was recreated correctly from requirements.txt
"""

import sys


def check_package(package_name):
    """Check if a package is installed and return its version"""
    try:
        module = __import__(package_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"  ✓ {package_name} (version {version}) - installed")
        return True
    except ImportError:
        print(f"  ✗ {package_name} - NOT installed")
        return False


def test_requests():
    """Test that requests package works"""
    try:
        import requests
        response = requests.get("https://httpbin.org/get", timeout=5)
        if response.status_code == 200:
            print("✓ requests: Successfully made API call")
            return True
        else:
            print(f"⚠ requests: API returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"⚠ requests: Error (okay if offline): {e}")
        return False


def test_colorama():
    """Test that colorama package works"""
    try:
        from colorama import Fore, Style, init
        init()
        print(f"✓ colorama: Color formatting works")
        return True
    except Exception as e:
        print(f"✗ colorama: Error - {e}")
        return False


def main():
    """Main verification function"""
    print("=== Environment Recreation Check ===")
    
    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if not in_venv:
        print("✗ No virtual environment detected!")
        print("Please create and activate a virtual environment first.")
        return False
    
    print("✓ Virtual environment is active!")
    
    # Check required packages
    print("✓ Checking required packages...")
    required_packages = ['requests', 'colorama']
    all_installed = all(check_package(pkg) for pkg in required_packages)
    
    if not all_installed:
        print("\n✗ Some packages are missing!")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✓ All required packages are installed!")
    
    # Test package functionality
    print("\nTesting package functionality...")
    test_requests()
    test_colorama()
    
    print("\nSUCCESS: Environment recreated successfully!")
    print("This is how you'd set up a teammate's project on your computer.")
    
    return True


if __name__ == "__main__":
    main()