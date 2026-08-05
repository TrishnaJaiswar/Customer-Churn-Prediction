import joblib

model = joblib.load("customer_churn_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

print("Loaded Successfully")