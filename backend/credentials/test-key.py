import ee
from google.oauth2 import service_account

KEY_PATH = 'ee-key.json'

try:
    # 1. Authenticate
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/earthengine'])
    ee.Initialize(credentials=scoped_credentials)
    print("✅ Authentication: OK")

    # 2. Test Computation (Does 1 + 1 on Google's servers)
    print("Testing cloud computation...", end=" ")
    result = ee.Number(1).add(1).getInfo()
    
    if result == 2:
        print(f"Success! (1+1={result})")
        print("\n🚀 SYSTEM READY. You can now run 'docker-compose up'")
    else:
        print("Failed logic test.")

except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nIf you see 'Project has not enabled the API', go here:")
    print("https://console.cloud.google.com/apis/library/earthengine.googleapis.com")