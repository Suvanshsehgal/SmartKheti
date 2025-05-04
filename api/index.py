from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from logic import fertilizer_recommendation, generate_farmer_message

app = FastAPI()

@app.get("/")
def root():
    return {"message": "🌱 Farmer Advisory API is running."}

@app.get("/recommend")
def get_recommendation(
    soil_type: str = Query(...),
    crop_type: str = Query(...),
    land_size: float = Query(...),
    fallow_years: int = Query(...),
    use_my_location: bool = Query(False),
    lat: float = Query(None),
    lon: float = Query(None),
    manual_location: str = Query(None)
):
    result = fertilizer_recommendation(
        soil_type=soil_type,
        crop_type=crop_type,
        land_size=land_size,
        fallow_years=fallow_years,
        use_my_location=use_my_location,
        lat=lat,
        lon=lon,
        manual_location=manual_location
    )
    if "error" in result:
        return JSONResponse(content=result, status_code=400)
    
    message = generate_farmer_message(result)
    return {"recommendation": result, "message": message}
