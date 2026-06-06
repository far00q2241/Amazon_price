import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("Amazon_Big_Sales_Dataset_2026_model.pkl")

st.title("📦 Product Prediction App")

st.sidebar.header("Product Details")

# Inputs
rating = st.sidebar.number_input(
    "Rating",
    min_value=0.0,
    max_value=5.0,
    value=5.0,
    step=0.1
)

review_count = st.sidebar.number_input(
    "Review Count",
    min_value=0,
    value=5000,
    step=100
)

freq_product_name = st.sidebar.number_input(
    "Product Name Frequency",
    min_value=0,
    value=1,
    step=1
)

category_electronics = st.sidebar.selectbox(
    "Is Electronics Category?",
    ["No", "Yes"]
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        'Rating': [rating],
        'Review_Count': [review_count],
        'freq_Product_Name': [freq_product_name],
        'Category_Electronics': [
            1 if category_electronics == "Yes" else 0
        ]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Prediction: {prediction}")
