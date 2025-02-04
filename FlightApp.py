
import joblib
import pandas as pd
import numpy as np
import streamlit as st

# تحميل النموذج والمدخلات
Model = joblib.load("FlightPricePredictor.pkl")
Inputs = joblib.load("inputs.pkl")

def prediction(Airline, Source, Destination, Total_Stops, Additional_Info, journey_day, journey_month, Dep_Time_hour, Dep_Time_minute, Arrival_Time_hour, Arrival_Time_minute, Duration_minutes):
    # تجهيز المدخلات
    df = pd.DataFrame(columns=Inputs)
    df.at[0, "Airline"] = Airline
    df.at[0, "Source"] = Source
    df.at[0, "Destination"] = Destination
    df.at[0, "Total_Stops"] = Total_Stops
    df.at[0, "Additional_Info"] = Additional_Info
    df.at[0, "journey_day"] = journey_day
    df.at[0, "journey_month"] = journey_month
    df.at[0, "Dep_Time_hour"] = Dep_Time_hour
    df.at[0, "Dep_Time_minute"] = Dep_Time_minute
    df.at[0, "Arrival_Time_hour"] = Arrival_Time_hour
    df.at[0, "Arrival_Time_minute"] = Arrival_Time_minute
    df.at[0, "Duration_minutes"] = Duration_minutes
    result = Model.predict(df)[0]
    return result

def Main():
    st.title("Flight Price Prediction")

    Airline = st.selectbox("Airline", ["IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara", "GoAir", "Multiple carriers"])
    Source = st.selectbox("Source", ["Delhi", "Kolkata", "Banglore", "Mumbai", "Chennai"])
    Destination = st.selectbox("Destination", ["Cochin", "Delhi", "New Delhi", "Banglore", "Hyderabad", "Kolkata"]) #
    Total_Stops = st.selectbox("Total Stops", ["0", "1", "2", "3", "4"])
    Additional_Info = st.selectbox("Additional Info", ["No info", "In-flight meal not included", "No check-in baggage included", "Long layover", "Change airports", "Business class"])
    journey_day = st.slider("Journey Day", min_value=1, max_value=31, step=1, value=15)
    journey_month = st.slider("Journey Month", min_value=1, max_value=12, step=1, value=5)
    Dep_Time_hour = st.slider("Departure Hour", min_value=0, max_value=23, step=1, value=10)
    Dep_Time_minute = st.slider("Departure Minute", min_value=0, max_value=59, step=1, value=30)
    Arrival_Time_hour = st.slider("Arrival Hour", min_value=0, max_value=23, step=1, value=14)
    Arrival_Time_minute = st.slider("Arrival Minute", min_value=0, max_value=59, step=1, value=15)
    Duration_minutes = st.slider("Duration (Minutes)", min_value=30, max_value=1500, step=10, value=120)

    if st.button("Predict"):
        result = prediction(Airline, Source, Destination, Total_Stops, Additional_Info, journey_day, journey_month, Dep_Time_hour, Dep_Time_minute, Arrival_Time_hour, Arrival_Time_minute, Duration_minutes)
        st.text(f"Predicted Flight Price: ₹{result:.2f}")

Main()
