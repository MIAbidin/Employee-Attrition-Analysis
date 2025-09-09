import pandas as pd
import joblib

best_model = joblib.load("model/best_model.pkl")
scaler = joblib.load("model/scaler.pkl")
columns = joblib.load("model/feature_columns.pkl")

data_baru = {
    "Age": 25,
    "TotalWorkingYears": 3,
    "YearsAtCompany": 1,
    "MonthlyIncome": 3000,
    "JobLevel": 1,
    "DistanceFromHome": 25,
    "OverTime": 1,
    "MaritalStatus_Single": 1,
    "MaritalStatus_Married": 0,
    "JobSatisfaction": 1,
    "EnvironmentSatisfaction": 1,
    "WorkLifeBalance": 1,
    "Department_Sales": 1,
    "Department_Research & Development": 0,
    "JobRole_Sales Representative": 1,
    "JobRole_Research Scientist": 0,
    "BusinessTravel_Travel_Frequently": 1,
    "BusinessTravel_Travel_Rarely": 0,
}

df_new = pd.DataFrame([data_baru])
df_new = df_new.reindex(columns=columns, fill_value=0)

df_new_scaled = pd.DataFrame(
    scaler.transform(df_new), 
    columns=columns
)

y_pred = best_model.predict(df_new_scaled)
y_prob = best_model.predict_proba(df_new_scaled)[:, 1]

print("="*50)
print("EMPLOYEE ATTRITION PREDICTION")
print("="*50)
print(f"Prediction Result : {'ATTRITION' if y_pred[0] == 1 else 'NO ATTRITION'}")
print(f"Probability       : {y_prob[0]:.2%}")
print("="*50)
