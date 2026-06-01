from fastapi import APIRouter
import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

router = APIRouter()



@router.get("/countplot/{column_name}")
def countplot_graph(column_name: str):

    try:

        path = "/Users/indrapal/enterprise_ai_platform/datasets/cleaned_superstore.csv"

        df = pd.read_csv(path, encoding="latin1")

        # Check column exists
        if column_name not in df.columns:

            return {
                "error": f"{column_name} column not found"
            }

        plt.figure(figsize=(12,6))

        sns.countplot(x=column_name, data=df)

        plt.title(f"{column_name} Countplot", fontsize=18)

        plt.xticks(rotation=45)

        output_path = f"/Users/indrapal/enterprise_ai_platform/visualizations/{column_name}_countplot.png"

        plt.savefig(output_path)

        plt.close()

        return {

            "message": f"{column_name} countplot generated",

            "saved_to": output_path

        }

    except Exception as e:

        return {
            "error": str(e)
        }
    
@router.get("/correlation")
def correlation_heatmap():

    try:

        path = "/Users/indrapal/enterprise_ai_platform/datasets/cleaned_superstore.csv"

        df = pd.read_csv(path, encoding="latin1")

        # Select only numeric columns
        numeric_df = df.select_dtypes(include='number')

        # Correlation matrix
        corr = numeric_df.corr()

        plt.figure(figsize=(14,8))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        plt.title("Correlation Heatmap", fontsize=18)

        output_path = "/Users/indrapal/enterprise_ai_platform/visualizations/correlation_heatmap.png"

        plt.savefig(output_path)

        plt.close()

        return {

            "message": "Correlation heatmap generated",

            "saved_to": output_path

        }

    except Exception as e:

        return {
            "error": str(e)
        }