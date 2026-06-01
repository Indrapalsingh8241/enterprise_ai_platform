import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "ml_models" / "profit_prediction_model.pkl"
FEATURES_PATH = BASE_DIR / "ml_models" / "feature_columns.pkl"

model = joblib.load(MODEL_PATH)

feature_columns = joblib.load(FEATURES_PATH)

def predict_profit(data):

    discounted_sales = (
        data.Sales * (1 - data.Discount)
    )

    discount_amount = (
        data.Sales * data.Discount
    )

    price_per_item = (
        data.Sales / data.Quantity
    )

    quarter = 1

    input_df = pd.DataFrame([{

        "Sales": data.Sales,
        "Quantity": data.Quantity,
        "Discount": data.Discount,
        "Shipping Days": data.Shipping_Days,
        "Quarter": quarter,
        "Discounted_Sales": discounted_sales,
        "Price_Per_Item": price_per_item,
        "Discount_Amount": discount_amount,
        "Region": data.Region,
        "Category": data.Category,
        "Sub-Category": data.Sub_Category

    }])

    input_df = pd.get_dummies(input_df)

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(input_df)

    return round(float(prediction[0]), 2)