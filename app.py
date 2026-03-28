import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# LOAD MODEL
# ======================
model = pickle.load(open("model.pkl", "rb"))

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="House Price AI Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ======================
# UI STYLE
# ======================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #eef2f3, #8e9eab);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f3b73;
}

.sub {
    text-align: center;
    font-size: 18px;
}

.stButton button {
    background-color: #1f3b73;
    color: white;
    height: 45px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown('<div class="title">🏠 House Price Prediction AI Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Advanced ML Model with Insights & Analytics</div>', unsafe_allow_html=True)
st.markdown("---")

# ======================
# SIDEBAR MENU
# ======================
menu = st.sidebar.selectbox("📌 Menu", ["Prediction", "Analytics", "About"])

# ======================
# PAGE 1 — PREDICTION
# ======================
if menu == "Prediction":

    st.subheader("🏡 Enter Property Details")

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("Area (sq ft)", 500, 10000, 1500)
        bedrooms = st.slider("Bedrooms", 1, 10, 3)
        bathrooms = st.slider("Bathrooms", 1, 10, 2)
        stories = st.slider("Stories", 1, 5, 1)

    with col2:
        parking = st.slider("Parking Spaces", 0, 5, 1)
        mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
        guestroom = st.selectbox("Guest Room", ["Yes", "No"])
        basement = st.selectbox("Basement", ["Yes", "No"])

    # ======================
    # ENCODING
    # ======================
    mainroad = 1 if mainroad == "Yes" else 0
    guestroom = 1 if guestroom == "Yes" else 0
    basement = 1 if basement == "Yes" else 0

    input_data = np.array([[area, bedrooms, bathrooms, stories,
                            parking, mainroad, guestroom, basement]])

    # ======================
    # PREDICTION
    # ======================
    if st.button("🚀 Predict Price", use_container_width=True):

        prediction = model.predict(input_data)[0]

        st.markdown("### 💰 Estimated Price")
        st.success(f"PKR {prediction:,.0f}")

        # ===== Insight Level (OPTION 1) =====
        if prediction > 10000000:
            st.info("🏆 Premium Property")
        elif prediction > 5000000:
            st.warning("🏠 Mid-range Property")
        else:
            st.error("💡 Budget Property")

# ======================
# PAGE 2 — ANALYTICS
# ======================
elif menu == "Analytics":

    st.subheader("📊 Market Insights")

    # Dummy Feature Importance (OPTION 2)
    df = pd.DataFrame({
        "Feature": ["Area", "Bathrooms", "Bedrooms", "Stories", "Parking"],
        "Importance": [0.40, 0.20, 0.15, 0.15, 0.10]
    })

    fig, ax = plt.subplots()
    sns.barplot(x="Importance", y="Feature", data=df, ax=ax)
    st.pyplot(fig)

    st.info("📌 Area is usually the most important factor in house price prediction.")

# ======================
# PAGE 3 — ABOUT
# ======================
elif menu == "About":

    st.subheader("📘 About Project")

    st.write("""
    🏠 House Price Prediction System using Machine Learning.

    ✔ Model: Regression Model  
    ✔ Input: Property details  
    ✔ Output: Price prediction  

    💡 Features:
    - Real-time prediction
    - Price category insight
    - Analytics dashboard
    - Modern UI design
    """)

    st.success("Built for ML Portfolio 🚀")