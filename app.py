from fastapi import FastAPI
from pydantic import BaseModel, Field , computed_field
from typing import Literal , Annotated
import pandas as pd
import joblib

# loading model
model = joblib.load("customer_churn_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")
print("Loaded Successfully")

app = FastAPI()

#pydantic model to validate incoming data

class UserInput(BaseModel):

    gender: Annotated[
        Literal["Male", "Female"],
        Field(..., description="Customer gender")
    ]

    SeniorCitizen: Annotated[
        int,
        Field(..., description="0 = No, 1 = Yes", ge=0, le=1)
    ]

    Partner: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Has a partner?")
    ]

    Dependents: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Has dependents?")
    ]

    tenure: Annotated[
        int,
        Field(..., description="Customer tenure in months", ge=0, le=72)
    ]

    PhoneService: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Phone service")
    ]

    MultipleLines: Annotated[
        Literal["Yes", "No", "No phone service"],
        Field(..., description="Multiple phone lines")
    ]

    InternetService: Annotated[
        Literal["DSL", "Fiber optic", "No"],
        Field(..., description="Internet service type")
    ]

    OnlineSecurity: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Online security service")
    ]

    OnlineBackup: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Online backup service")
    ]

    DeviceProtection: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Device protection service")
    ]

    TechSupport: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Technical support service")
    ]

    StreamingTV: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Streaming TV service")
    ]

    StreamingMovies: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Streaming Movies service")
    ]

    Contract: Annotated[
        Literal["Month-to-month", "One year", "Two year"],
        Field(..., description="Contract type")
    ]

    PaperlessBilling: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Paperless billing")
    ]

    PaymentMethod: Annotated[
        Literal[
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ],
        Field(..., description="Payment method")
    ]

    MonthlyCharges: Annotated[
        float,
        Field(..., description="Monthly charges", gt=0)
    ]

    TotalCharges: Annotated[
        float,
        Field(..., description="Total charges", ge=0)
    ]

@app.get('/')
def home():
    return {
        'message':'Customer Churn Prediction API is running successfully'
    }

@app.post("/predict")
def predict(data: UserInput):

    input_data  = data.model_dump()
    input_df = pd.DataFrame([input_data])
    processed_data = preprocessor.transform(input_df)
    prediction = model.predict(processed_data)[0]
    probability = model.predict_proba(processed_data)[0][1]

    return {
        "Prediction": "Customer Will Churn" if prediction == 1 else "Customer Will Stay",
        "Churn Probability": f"{probability*100:.2f}%"
    }