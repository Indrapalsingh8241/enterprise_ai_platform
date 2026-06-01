from fastapi import APIRouter

from backend.models.prediction_schema import (
    ProfitPredictionRequest
)

from backend.services.prediction_service import (
    predict_profit
)

router = APIRouter(
    prefix="/prediction",
    tags=["Profit Prediction"]
)


@router.post("/")
def predict(data: ProfitPredictionRequest):

    result = predict_profit(data)

    return {
        "predicted_profit": result
    }
@router.get("/model-info")
def model_info():

    return {
        "model": "Random Forest Regressor",
        "r2_score": 0.7412,
        "mae": 4.77,
        "mse": 95.09
    }