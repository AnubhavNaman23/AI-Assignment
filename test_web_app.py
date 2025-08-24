# LQT AI Assignment - Web Application Test

import requests
import json
from datetime import datetime

# Test configuration
BASE_URL = "http://localhost:5000"
API_URL = f"{BASE_URL}/api"

def test_health_check():
    """Test API health endpoint"""
    try:
        response = requests.get(f"{API_URL}/health")
        print(f"✅ Health Check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Status: {data['status']}")
            print(f"   Service: {data['service']}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health Check failed: {e}")
        return False

def test_data_generation():
    """Test data generation endpoint"""
    try:
        payload = {"samples": 1000}
        response = requests.post(f"{API_URL}/generate_data", json=payload)
        print(f"✅ Data Generation: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Success: {data['success']}")
            print(f"   Shape: {data['stats']['shape']}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Data Generation failed: {e}")
        return False

def test_model_training():
    """Test model training endpoint"""
    try:
        response = requests.post(f"{API_URL}/train_models")
        print(f"✅ Model Training: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Success: {data['success']}")
            print(f"   Models: {list(data['results'].keys())}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Model Training failed: {e}")
        return False

def test_prediction():
    """Test prediction endpoint"""
    try:
        sample_data = {
            "age": 30,
            "income": 55000,
            "education_years": 16,
            "experience": 8.5,
            "satisfaction_score": 7.5,
            "performance_rating": 4
        }
        response = requests.post(f"{API_URL}/predict", json=sample_data)
        print(f"✅ Prediction: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Success: {data['success']}")
            print(f"   Predictions: {len(data['predictions'])}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Prediction failed: {e}")
        return False

def test_visualization():
    """Test visualization endpoints"""
    viz_types = ['correlation', 'distribution', 'pairplot', 'performance']
    results = []
    
    for viz_type in viz_types:
        try:
            response = requests.get(f"{API_URL}/visualize/{viz_type}")
            success = response.status_code == 200
            print(f"{'✅' if success else '❌'} Visualization ({viz_type}): {response.status_code}")
            results.append(success)
        except Exception as e:
            print(f"❌ Visualization ({viz_type}) failed: {e}")
            results.append(False)
    
    return all(results)

def test_web_pages():
    """Test web page endpoints"""
    pages = ['/', '/dashboard']
    results = []
    
    for page in pages:
        try:
            response = requests.get(f"{BASE_URL}{page}")
            success = response.status_code == 200
            print(f"{'✅' if success else '❌'} Page ({page}): {response.status_code}")
            results.append(success)
        except Exception as e:
            print(f"❌ Page ({page}) failed: {e}")
            results.append(False)
    
    return all(results)

def run_full_test():
    """Run complete test suite"""
    print("🧪 Starting LQT AI Assignment Web Application Tests")
    print("=" * 60)
    
    tests = [
        ("Web Pages", test_web_pages),
        ("Health Check", test_health_check),
        ("Data Generation", test_data_generation),
        ("Model Training", test_model_training),
        ("Prediction", test_prediction),
        ("Visualization", test_visualization),
    ]
    
    results = {}
    for test_name, test_func in tests:
        print(f"\n🔬 Testing {test_name}...")
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test suite failed: {e}")
            results[test_name] = False
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print("=" * 60)
    
    passed = 0
    total = len(tests)
    
    for test_name, passed_test in results.items():
        status = "PASS" if passed_test else "FAIL"
        icon = "✅" if passed_test else "❌"
        print(f"{icon} {test_name}: {status}")
        if passed_test:
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"📈 Overall Results: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")
    
    if passed == total:
        print("🎉 All tests passed! Web application is ready for deployment.")
    else:
        print("⚠️  Some tests failed. Please check the Flask application.")
    
    return passed == total

if __name__ == "__main__":
    print("🚀 LQT AI Assignment - Web Application Test Suite")
    print("📅 Run Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("🌐 Target URL:", BASE_URL)
    print("\n⚠️  Make sure the Flask application is running before executing tests!")
    print("   Command: python src/api/app.py\n")
    
    input("Press Enter to start testing... ")
    
    success = run_full_test()
    
    if success:
        print("\n✨ Testing completed successfully!")
    else:
        print("\n🔧 Testing completed with issues. Check the logs above.")
