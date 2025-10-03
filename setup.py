#!/usr/bin/env python3
"""
Setup script for CPG Labs APIs
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("Please use Python 3.8 or higher")
        return False

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing dependencies...")
    
    # Install main requirements
    if not run_command("pip install -r requirements.txt", "Installing main dependencies"):
        return False
    
    # Install SEO Lab requirements
    if not run_command("pip install -r apis/seo_lab/requirements.txt", "Installing SEO Lab dependencies"):
        return False
    
    return True

def create_env_file():
    """Create .env file from template"""
    print("🔧 Setting up environment file...")
    
    env_file = Path(".env")
    env_example = Path("env.example")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if env_example.exists():
        # Copy env.example to .env
        with open(env_example, 'r') as src, open(env_file, 'w') as dst:
            dst.write(src.read())
        print("✅ Created .env file from template")
        print("⚠️  Please edit .env file with your actual API keys")
        return True
    else:
        print("❌ env.example file not found")
        return False

def verify_setup():
    """Verify the setup is working"""
    print("🔍 Verifying setup...")
    
    # Check if main.py exists
    if not Path("main.py").exists():
        print("❌ main.py not found")
        return False
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        return False
    
    # Check if .env exists
    if not Path(".env").exists():
        print("❌ .env file not found")
        return False
    
    print("✅ Setup verification passed")
    return True

def main():
    """Main setup function"""
    print("🚀 CPG Labs APIs Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create environment file
    if not create_env_file():
        print("❌ Failed to create environment file")
        sys.exit(1)
    
    # Verify setup
    if not verify_setup():
        print("❌ Setup verification failed")
        sys.exit(1)
    
    print("\n" + "=" * 40)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file with your API keys")
    print("2. Run 'python test_api.py' to test the API")
    print("3. Run 'python main.py' to start the server")
    print("4. Visit http://localhost:8000/docs for API documentation")

if __name__ == "__main__":
    main()
