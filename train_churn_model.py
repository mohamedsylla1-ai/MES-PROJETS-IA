import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

np.random.seed(42)
n_samples = 1000

data = {
    'tenure': np.random.randint(0, 72, n_samples),
    'MonthlyCharges': np.random.uniform(20, 120, n_samples),
    'TotalCharges': np.random.uniform(100, 8600, n_samples),
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples),
    'InternetService': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples),
    'OnlineSecurity': np.random.choice(['Yes', 'No'], n_samples),
    'TechSupport': np.random.choice(['Yes', 'No'], n_samples),
    'PhoneService': np.random.choice(['Yes', 'No'], n_samples),
    'StreamingTV': np.random.choice(['Yes', 'No'], n_samples),
}

churn = []
for i in range(n_samples):
    churn_score = 0
    if data['Contract'][i] == 'Month-to-month':
        churn_score += 0.4
    if data['InternetService'][i] == 'Fiber optic':
        churn_score += 0.2
    if data['OnlineSecurity'][i] == 'No':
        churn_score += 0.1
    if data['tenure'][i] < 6:
        churn_score += 0.3
    if data['MonthlyCharges'][i] > 100:
        churn_score += 0.1
    
    churn_score += np.random.normal(0, 0.1)
    churn.append('Yes' if churn_score > 0.5 else 'No')

data['Churn'] = churn
df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

binary_cols = ['OnlineSecurity', 'TechSupport', 'PhoneService', 'StreamingTV']
labelencoder = LabelEncoder()
for col in binary_cols:
    df[col] = labelencoder.fit_transform(df[col])

multi_cat_cols = ['Contract', 'InternetService']
df = pd.get_dummies(df, columns=multi_cat_cols, drop_first=True)

scaler = StandardScaler()
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

joblib.dump(model, 'churn_model.pkl')
joblib.dump(scaler, 'churn_scaler.pkl')
joblib.dump(X.columns.tolist(), 'churn_features.pkl')

print("✅ Modèle de churn entraîné et sauvegardé")
print(f"📊 Accuracy: {model.score(X_test, y_test):.2%}")
