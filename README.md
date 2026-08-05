# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, subscription details, and billing information.

The application is built using **Logistic Regression** and deployed with **FastAPI** for the backend and **Streamlit** for the frontend.

---

## 🚀 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- FastAPI
- Pydantic
- Streamlit
- Uvicorn

---

## 📌 Project Workflow

1. Collected the Telco Customer Churn dataset.
2. Cleaned the dataset by removing unnecessary columns and duplicate records.
3. Performed Exploratory Data Analysis (EDA) to understand customer behavior and churn patterns.
4. Preprocessed the data using OneHotEncoder and ColumnTransformer.
5. Split the dataset into training and testing sets.
6. Trained multiple machine learning models:
   - Logistic Regression
   - Decision Tree
   - Random Forest
7. Compared model performance using Accuracy, Precision, Recall, and F1-Score.
8. Selected **Logistic Regression** as the final model based on its overall performance.
9. Saved the trained model and preprocessing pipeline using Joblib.
10. Built a FastAPI REST API for real-time predictions.
11. Developed a Streamlit web interface for user-friendly interaction with the model.

---

## 📊 Model Performance

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | **80.36%** |
| Random Forest | 78.22% |
| Decision Tree | 72.03% |

**Final Model:** Logistic Regression

---

## ▶️ Run the Project

### Start FastAPI

```bash
uvicorn app:app --reload
```

### Start Streamlit

```bash
streamlit run ui.py
```

---

## 📥 Input Features

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

---

## 📤 Output

- Customer Will Churn
- Customer Will Stay
- Churn Probability
