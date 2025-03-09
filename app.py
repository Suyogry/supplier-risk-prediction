import streamlit as st
import pandas as pd
import joblib

def load_model():
    """Load the trained supplier risk model."""
    return joblib.load('supplier_risk_model.pkl')

def predict_risk(avg_delivery_delay, defect_ratio, transaction_consistency):
    """Predict supplier risk category based on user inputs."""
    model = load_model()
    prediction = model.predict([[avg_delivery_delay, defect_ratio, transaction_consistency]])
    return prediction[0]

# Streamlit UI
st.title("Supplier Risk Prediction Dashboard")

st.sidebar.header("Input Supplier Data")

avg_delivery_delay = st.sidebar.number_input("Average Delivery Delay (days)", value=0.0)
defect_ratio = st.sidebar.number_input("Defect Ratio", value=0.0)
transaction_consistency = st.sidebar.number_input("Transaction Consistency Score", value=0.0)

if st.sidebar.button("Predict Risk"):
    risk_category = predict_risk(avg_delivery_delay, defect_ratio, transaction_consistency)
    st.write(f"Predicted Supplier Risk Category: **{risk_category}**")
