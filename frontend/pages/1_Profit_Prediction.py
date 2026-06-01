import streamlit as st
import requests

st.title("💰 Profit Prediction")

sales = st.number_input(
    "Sales",
    min_value=0.0,
    value=1000.0
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    value=2
)

discount = st.slider(
    "Discount",
    0.0,
    1.0,
    0.1
)

region = st.selectbox(
    "Region",
    ["East", "West", "South", "Central"]
)

category = st.selectbox(
    "Category",
    [
        "Furniture",
        "Office Supplies",
        "Technology"
    ]
)

sub_category = st.text_input(
    "Sub Category",
    "Phones"
)

shipping_days = st.number_input(
    "Shipping Days",
    min_value=1,
    value=3
)

if st.button("Predict Profit"):

    payload = {
        "Sales": sales,
        "Quantity": quantity,
        "Discount": discount,
        "Region": region,
        "Category": category,
        "Sub_Category": sub_category,
        "Shipping_Days": shipping_days
    }

    response = requests.post(
        "http://127.0.0.1:8000/prediction",
        json=payload
    )

    result = response.json()

    st.success(
        f"Predicted Profit: ₹{result['predicted_profit']}"
    )