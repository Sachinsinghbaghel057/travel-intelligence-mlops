import requests

# ==========================================================
# FastAPI Base URL
# ==========================================================

# Local Development
BASE_URL = "http://127.0.0.1:8000"

# Docker (Uncomment when using Docker Compose)
# BASE_URL = "http://fastapi:8000"


# ==========================================================
# Flight Prediction
# ==========================================================

def predict_flight(data: dict):

    response = requests.post(
        f"{BASE_URL}/predict",
        json=data
    )

    response.raise_for_status()

    return response.json()


# ==========================================================
# Hotel Prediction
# ==========================================================

def predict_hotel(data: dict):

    response = requests.post(
        f"{BASE_URL}/predict/hotel",
        json=data
    )

    response.raise_for_status()

    return response.json()