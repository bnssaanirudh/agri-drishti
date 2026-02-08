import ee
from google.oauth2 import service_account
from app.core.config import settings

# Initialize Earth Engine with your Key
def init_ee():
    try:
        credentials = service_account.Credentials.from_service_account_file(settings.EE_KEY_PATH)
        scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/earthengine'])
        ee.Initialize(credentials=scoped_credentials)
        print("✅ Earth Engine Initialized.")
    except Exception as e:
        print(f"❌ Earth Engine Failed: {e}")

# Call init immediately
init_ee()

def get_vegetation_stats(geometry, start_date, end_date):
    """
    Fetches Mean NDVI for a given geometry (District)
    """
    s2 = ee.ImageCollection("COPERNICUS/S2_SR") \
        .filterBounds(geometry) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))

    def add_ndvi(image):
        ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
        return image.addBands(ndvi)

    dataset = s2.map(add_ndvi)
    
    # Reduce to get mean value
    image = dataset.mean()
    stats = image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=geometry,
        scale=100, # Lower resolution for speed in demo
        maxPixels=1e9
    )
    
    # Return 0 if data missing (cloud cover)
    return stats.get('NDVI').getInfo() or 0.0