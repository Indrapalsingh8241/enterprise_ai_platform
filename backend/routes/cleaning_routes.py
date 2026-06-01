from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/summary")
def data_summary():

    try:

        path = "/Users/indrapal/enterprise_ai_platform/datasets/Sample - Superstore.csv"

        df = pd.read_csv(path, encoding="latin1")

        return {

            "message": "Data summary generated successfully",

            "shape": df.shape,

            "total_rows": len(df),

            "total_columns": len(df.columns),

            "columns": list(df.columns),

            "missing_values": df.isnull().sum().to_dict(),

            "duplicate_rows": int(df.duplicated().sum()),

            "data_types": df.dtypes.astype(str).to_dict(),

            "numerical_summary": df.describe().to_dict()

        }

    except Exception as e:

        return {
            "error": str(e)
        }
    
@router.get("/clean-data")
def clean_data():

    try:

        path = "/Users/indrapal/enterprise_ai_platform/datasets/Sample - Superstore.csv"

        df = pd.read_csv(path, encoding="latin1")

        # Store original shape
        original_shape = df.shape

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Fill missing numeric values with mean
        numeric_columns = df.select_dtypes(include=["number"]).columns

        for col in numeric_columns:
            df[col].fillna(df[col].mean(), inplace=True)

        # Fill missing object/string values
        object_columns = df.select_dtypes(include=["object"]).columns

        for col in object_columns:
            df[col].fillna("Unknown", inplace=True)

        # Save cleaned dataset
        output_path = "/Users/indrapal/enterprise_ai_platform/datasets/cleaned_superstore.csv"

        df.to_csv(output_path, index=False)

        return {

            "message": "Data cleaned successfully",

            "original_shape": original_shape,

            "cleaned_shape": df.shape,

            "duplicates_removed": int(original_shape[0] - df.shape[0]),

            "cleaned_file": "cleaned_superstore.csv"

        }

    except Exception as e:

        return {
            "error": str(e)
        }
    