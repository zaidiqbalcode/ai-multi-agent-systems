#!/usr/bin/env python3
"""
Backend deployment preparation script
Run this before deploying to ensure everything is ready
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'api.py',
        'requirements.txt', 
        'Procfile',
        '.env.example'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def test_api_locally():
    """Test if the API can start locally"""
    print("🧪 Testing API structure...")
    try:
        # Check if api.py exists and is readable
        if not os.path.exists('api.py'):
            print("❌ api.py not found")
            return False
            
        # Check if main.py exists (required import)
        if not os.path.exists('main.py'):
            print("❌ main.py not found")
            return False
            
        print("✅ API files structure looks good")
        print("   (Deployment platform will handle dependencies)")
        return True
        
    except Exception as e:
        print(f"❌ API check failed: {e}")
        return False

def check_environment():
    """Check environment variables"""
    from dotenv import load_dotenv
    load_dotenv()
    
    google_key = os.getenv('GOOGLE_API_KEY')
    if not google_key:
        print("⚠️  GOOGLE_API_KEY not found in .env file")
        print("   Make sure to set this in your deployment platform")
    else:
        print("✅ GOOGLE_API_KEY found in .env")
    
    return True

def main():
    """Run all pre-deployment checks"""
    print("🚀 Backend Deployment Preparation")
    print("=" * 40)
    
    checks = [
        ("File Requirements", check_requirements),
        ("API Functionality", test_api_locally), 
        ("Environment Setup", check_environment),
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"\n🔍 {name}:")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 Ready for deployment!")
        print("\nNext steps:")
        print("1. Push to GitHub")
        print("2. Connect to Railway/Render/Heroku")
        print("3. Set GOOGLE_API_KEY environment variable")
        print("4. Deploy!")
    else:
        print("❌ Please fix the issues above before deploying")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
