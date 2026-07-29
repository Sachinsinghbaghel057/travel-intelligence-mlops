import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    flights = pd.read_csv("data/processed/flights_processed.csv")
    hotels = pd.read_csv("data/processed/hotels_processed.csv")
    return flights, hotels


def dashboard_page():

    st.title("📊 Travel Intelligence Dashboard")

    flights, hotels = load_data()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Flights", len(flights))

    with col2:
        st.metric("Hotels", len(hotels))

    with col3:
        st.metric(
            "Destinations",
            hotels["place"].nunique()
        )

    with col4:
        st.metric(
            "Hotel Brands",
            hotels["name"].nunique()
        )

    st.divider()

    st.subheader("Top Airlines")
    st.bar_chart(flights["agency"].value_counts())

    st.subheader("Flight Type Distribution")
    st.bar_chart(flights["flightType"].value_counts())

    st.subheader("Most Popular Destinations")
    st.bar_chart(flights["to"].value_counts().head(10))