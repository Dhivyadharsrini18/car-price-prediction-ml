import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="centered")

st.title("🚗 Car Price Prediction Model")
st.markdown("Predict the selling price of a used car using Machine Learning.")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.markdown("### Enter Car Details")

present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, step=0.01, value=5.0)
kms_driven = st.number_input("Driven Kilometers", min_value=0, step=1000, value=20000)
car_age = st.slider("Car Age", min_value=0, max_value=20, value=3)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

if st.button("Predict Price"):
    input_df = pd.DataFrame([
        {
            "Present_Price": present_price,
            "Kms_Driven": kms_driven,
            "Fuel_Type": fuel_type,
            "Seller_Type": seller_type,
            "Transmission": transmission,
            "Owner": owner,
            "Car_Age": car_age,
        }
    ])

    prediction = model.predict(input_df)[0]

    st.success("✅ Prediction Successful")
    st.success(f"💰 Estimated Selling Price\n₹ {prediction:.2f} Lakhs")
