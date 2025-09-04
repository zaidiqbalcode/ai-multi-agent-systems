"""
API Key Setup and Testing Script
This script helps you verify your API keys are working correctly.
"""

import os
from dotenv import load_dotenv

def setup_api_keys():
    """Load and verify API keys from .env file"""
    
    # Load environment variables
    load_dotenv()
    
    print("🔑 API Key Setup for Smart Content Pipeline")
    print("=" * 50)
    
    # Check OpenAI API Key
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key and openai_key != 'your_openai_api_key_here':
        print("✅ OpenAI API Key: Found")
        print(f"   Key Preview: {openai_key[:10]}...{openai_key[-4:]}")
    else:
        print("❌ OpenAI API Key: Not set")
        print("   Get your key from: https://platform.openai.com/api-keys")
    
    # Check Google API Key
    google_key = os.getenv('GOOGLE_API_KEY')
    if google_key and google_key != 'your_google_api_key_here':
        print("✅ Google API Key: Found")
        print(f"   Key Preview: {google_key[:10]}...{google_key[-4:]}")
    else:
        print("❌ Google API Key: Not set")
        print("   Get your key from: https://aistudio.google.com/app/apikey")
    
    print("\n" + "=" * 50)
    return openai_key, google_key

def test_openai_connection():
    """Test OpenAI API connection"""
    try:
        import openai
        openai_key = os.getenv('OPENAI_API_KEY')
        
        if not openai_key or openai_key == 'your_openai_api_key_here':
            print("❌ Cannot test OpenAI - API key not set")
            return False
            
        client = openai.OpenAI(api_key=openai_key)
        
        # Simple test call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API test successful'"}],
            max_tokens=10
        )
        
        print("✅ OpenAI API Test: SUCCESS")
        print(f"   Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API Test: FAILED - {str(e)}")
        return False

def test_google_connection():
    """Test Google Gemini API connection"""
    try:
        import google.generativeai as genai
        google_key = os.getenv('GOOGLE_API_KEY')
        
        if not google_key or google_key == 'your_google_api_key_here':
            print("❌ Cannot test Google - API key not set")
            return False
            
        genai.configure(api_key=google_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Simple test call
        response = model.generate_content("Say 'API test successful'")
        
        print("✅ Google Gemini API Test: SUCCESS")
        print(f"   Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ Google Gemini API Test: FAILED - {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Testing API Key Setup...\n")
    
    # Setup and verify keys
    openai_key, google_key = setup_api_keys()
    
    print("\n🧪 Testing API Connections...")
    print("-" * 30)
    
    # Test connections
    openai_works = test_openai_connection()
    google_works = test_google_connection()
    
    print("\n📋 Summary:")
    print("-" * 20)
    if openai_works or google_works:
        print("✅ At least one API is working - you're ready to go!")
        print("� You can run the full pipeline with: python main.py")
    else:
        print("❌ No working APIs found")
        print("📝 Please add your API keys to the .env file")
        
    print("\n🔗 Where to get API keys:")
    print("   OpenAI: https://platform.openai.com/api-keys")
    print("   Google: https://aistudio.google.com/app/apikey")
