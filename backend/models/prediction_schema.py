from pydantic import BaseModel, Field
from typing import Optional,Literal


class ProfitPredictionRequest(BaseModel):

    Sales: float = Field(
        default=1000.0,
        gt=0,
        description="Total sales amount of the order",
        example=1000.0
    )

    Quantity: int = Field(
        default=2,
        gt=0,
        description="Number of items ordered",
        example=2
    )

    Discount: float = Field(
        default=0.1,
        ge=0,
        le=1,
        description="Discount applied to the order (0 to 1)",
        example=0.1
    )

    Region: Literal[
     "East",
     "West",
     "South",
     "Central"
     ]      = Field(
        default="West",
        description="Sales region",
        
    )

    Category:Literal[ "Furniture",
      "Office Supplies",
        "Technology"] = Field(
        default="Technology",
        description="Product category",
       
    )

    Sub_Category: Optional[str] = Field(
        default="Phones",
        description="Product sub-category",
        example="Phones"
    )

    Shipping_Days: Optional[int] = Field(
        default=3,
        ge=0,
        description="Number of days taken for shipping",
        example=3
    )