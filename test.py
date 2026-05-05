import requests

BASE_URL = "http://localhost:1111"


# ---------------------------
# 1. Test root endpoint
# ---------------------------
def test_index():
    try:
        res = requests.get(f"{BASE_URL}/")
        print("\n🔹 Testing / (GET)")
        print("Status:", res.status_code)
        print("Response:", res.json())
    except Exception as e:
        print("❌ Index test failed:", str(e))


# ---------------------------
# 2. Test predict GET
# ---------------------------
def test_predict_get():
    try:
        res = requests.get(f"{BASE_URL}/predict")
        print("\n🔹 Testing /predict (GET)")
        print("Status:", res.status_code)
        print("Response:", res.json())
    except Exception as e:
        print("❌ Predict GET failed:", str(e))


# ---------------------------
# 3. Test predict POST (image upload)
# ---------------------------
def test_predict_post(image_path):
    try:
        print("\n🔹 Testing /predict (POST)")

        with open(image_path, "rb") as f:
            files = {"file": f}
            res = requests.post(f"{BASE_URL}/predict", files=files)

        print("Status:", res.status_code)
        print("Response:", res.json())

    except Exception as e:
        print("❌ Predict POST failed:", str(e))


# ---------------------------
# RUN ALL TESTS
# ---------------------------
if __name__ == "__main__":
    print("🚀 Starting API Tests...\n")

    test_index()
    test_predict_get()

    # 🔥 Change this to your test image path
    test_image_path = r"E:\DATASETS\archive (4)\train\images\00d9148d-582c852c09941d0b0a67b921_pan_jpg.rf.264cf417587b97fb8c630ffbb5deede9.jpg"
    test_predict_post(test_image_path)

    print("\n✅ Testing completed")