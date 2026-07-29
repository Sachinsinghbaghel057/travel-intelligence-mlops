import streamlit as st
import pandas as pd
from datetime import date
from pathlib import Path

from src.pipeline.hotel_prediction_pipeline import HotelPredictionPipeline


# Project Root
BASE_DIR = Path(__file__).resolve().parents[2]

# Data Path
HOTEL_DATA_PATH = BASE_DIR / "data" / "processed" / "hotels_processed.csv"


@st.cache_data
def load_hotels():
    df = pd.read_csv(HOTEL_DATA_PATH)
    return df[["name", "place"]].drop_duplicates().sort_values("name")


def hotel_prediction_page():

    st.title("🏨 Hotel Price Prediction")
    st.write("Predict the total hotel booking cost.")

    hotels = load_hotels()

    hotel_name = st.selectbox(
        "Select Hotel",
        hotels["name"].unique()
    )

    place = hotels.loc[
        hotels["name"] == hotel_name,
        "place"
    ].iloc[0]

    st.text_input(
        "Destination",
        value=place,
        disabled=True
    )

    stay_date = st.date_input(
        "Check-in Date",
        value=date.today()
    )

    days = st.number_input(
        "Number of Nights",
        min_value=1,
        max_value=30,
        value=1
    )

    if st.button("Predict Total Cost", use_container_width=True):

        stay_weekday = stay_date.strftime("%A")

        input_data = {
            "name": hotel_name,
            "place": place,
            "stay_weekday": stay_weekday,
            "days": int(days),
            "stay_year": stay_date.year,
            "stay_month": stay_date.month,
            "stay_day": stay_date.day
        }

        try:

            pipeline = HotelPredictionPipeline()

            prediction = pipeline.predict(input_data)

            st.success("Prediction Completed")

            st.metric(
                label="Estimated Total Hotel Cost",
                value=f"₹ {prediction:,.2f}"
            )

        except Exception as e:

            st.error(f"Prediction Failed: {e}")