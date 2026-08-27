import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_xgboost_pipeline.joblib")

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊"
)

st.title("📊 Customer Churn Predictor")
st.write("Predict whether a customer is likely to churn.")

st.divider()

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

if st.button("Predict Churn"):

    input_data = pd.DataFrame([{
        "Contract": contract,
        "tenure": tenure,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "TechSupport": tech_support,
        "MonthlyCharges": monthly_charges,
        "PaymentMethod": payment_method
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High churn risk — this customer may leave.")
    else:
        st.success("✅ Low churn risk — this customer is likely to stay.")