import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction App")
st.write("Fill the details below to estimate house price")

st.divider()

# 🎨 Better UI using sliders (more user-friendly)

MedInc = st.slider("Median Income", 0.0, 15.0, 3.0)
HouseAge = st.slider("House Age", 1, 50, 20)
AveRooms = st.slider("Average Rooms", 1.0, 10.0, 5.0)
AveBedrms = st.slider("Average Bedrooms", 1.0, 5.0, 1.0)

Population = st.slider("Population", 0, 5000, 1000)
AveOccup = st.slider("Average Occupancy", 1.0, 10.0, 3.0)
Latitude = st.slider("Latitude", 32.0, 42.0, 34.0)
Longitude = st.slider("Longitude", -125.0, -114.0, -118.0)

st.divider()

# Predict button
if st.button("🔍 Predict Price"):
    input_data = np.array([[
        MedInc, HouseAge, AveRooms, AveBedrms,
        Population, AveOccup, Latitude, Longitude
    ]])

    prediction = model.predict(input_data)

    st.success(f"🏡 Estimated House Price: ${prediction[0]:,.2f}")