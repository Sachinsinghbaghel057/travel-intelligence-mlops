import requests

BASE_URL = "http://fastapi:8000"


def predict_flight(data: dict):

    response = requests.post(
        f"{BASE_URL}/predict",
        json=data
    )

    response.raise_for_status()

    return response.json()