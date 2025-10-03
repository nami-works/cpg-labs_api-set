#!/usr/bin/env python3
"""
Test script for the CPG Labs APIs
Run this to test the API locally or after deployment
"""

import requests
import json
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
API_KEY = os.getenv("EDGE_API_KEY", "your-secret-key-here")

def test_health():
    """Test the health endpoint"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"❌ Health check error: {e}")

def test_root():
    """Test the root endpoint"""
    print("\n🔍 Testing root endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/", timeout=10)
        if response.status_code == 200:
            print("✅ Root endpoint passed")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")

def test_generate_blog():
    """Test the blog generation endpoint"""
    print("\n🔍 Testing blog generation...")
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    
    payload = {
        "brand": "Nami Works",
        "topic": "The Future of AI in Content Creation",
        "keywords": ["AI content", "future tech", "content marketing"],
        "language": "en-US",
        "wordCount": 1000,
        "additionalContext": "Focus on benefits for small businesses."
    }
    
    try:
        print(f"Making request to: {API_BASE_URL}/api/seo/generate")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(
            f"{API_BASE_URL}/api/seo/generate", 
            headers=headers, 
            data=json.dumps(payload), 
            timeout=120  # 2 minutes timeout for generation
        )
        
        if response.status_code == 200:
            print("✅ Blog generation request successful")
            result = response.json()
            print(f"Generated HTML length: {len(result.get('html', ''))}")
            print(f"Meta data: {result.get('meta', {})}")
            print(f"Stats: {result.get('stats', {})}")
            print(f"Trace ID: {result.get('traceId', 'N/A')}")
            
            # Save generated content to file
            with open("generated_content.html", "w", encoding="utf-8") as f:
                f.write(result.get('html', ''))
            print("📄 Generated content saved to 'generated_content.html'")
            
        else:
            print(f"❌ Blog generation failed: {response.status_code}")
            print(f"Error response: {response.text}")
            
    except requests.exceptions.Timeout:
        print("❌ Blog generation request timed out (120s)")
    except Exception as e:
        print(f"❌ Blog generation error: {e}")

def test_invalid_api_key():
    """Test with invalid API key"""
    print("\n🔍 Testing invalid API key...")
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "invalid-key"
    }
    
    payload = {
        "brand": "Test Brand",
        "topic": "Test Topic"
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/seo/generate", 
            headers=headers, 
            data=json.dumps(payload), 
            timeout=10
        )
        
        if response.status_code == 401:
            print("✅ Invalid API key correctly rejected")
        else:
            print(f"❌ Expected 401, got {response.status_code}")
            
    except Exception as e:
        print(f"❌ Invalid API key test error: {e}")

def test_missing_fields():
    """Test with missing required fields"""
    print("\n🔍 Testing missing required fields...")
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    
    # Missing required 'topic' field
    payload = {
        "brand": "Test Brand"
    }
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/seo/generate", 
            headers=headers, 
            data=json.dumps(payload), 
            timeout=10
        )
        
        if response.status_code == 422:
            print("✅ Missing fields correctly rejected")
        else:
            print(f"❌ Expected 422, got {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Missing fields test error: {e}")

def main():
    """Run all tests"""
    print("🚀 Starting CPG Labs APIs Test Suite")
    print(f"API Base URL: {API_BASE_URL}")
    print(f"API Key: {'*' * len(API_KEY) if API_KEY != 'your-secret-key-here' else 'NOT SET'}")
    print("=" * 50)
    
    # Run tests
    test_health()
    test_root()
    test_invalid_api_key()
    test_missing_fields()
    test_generate_blog()
    
    print("\n" + "=" * 50)
    print("🏁 Test suite completed!")
    print("\nNext steps:")
    print("1. If all tests pass, your API is working correctly")
    print("2. Check 'generated_content.html' for the generated content")
    print("3. Deploy to Render.com using the deployment guide")
    print("4. Update your frontend to use the deployed API URL")

if __name__ == "__main__":
    main()
