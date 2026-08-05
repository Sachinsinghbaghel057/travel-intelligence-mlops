import os

import requests

from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv(
    "API_URL",
    "http://fastapi:8000"
)


def predict_flight(data: dict):

    response = requests.post(
        f"{BASE_URL}/predict",
        json=data
    )

    response.raise_for_status()

    return response.json()


def predict_hotel(data: dict):

    response = requests.post(
        f"{BASE_URL}/predict/hotel",
        json=data
    )

    response.raise_for_status()

    return response.json()