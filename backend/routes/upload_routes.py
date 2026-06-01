from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/upload")
def read_csv():

    try:
        path = "/Users/indrapal/enterprise_ai_platform/datasets/Sample - Superstore.csv"

        df = pd.read_csv(path, encoding="latin1")

        return {
            "message": "CSV loaded successfully",
            "shape": df.shape,
            "columns": list(df.columns),
           
        }

    except Exception as e:
        return {
            "error": str(e)
        }