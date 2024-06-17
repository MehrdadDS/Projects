import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

# Load and prepare your data
df = pd.read_excel('Input\your_dataset.xlsx')
df = df[df['Master Client']== "Columbia Sportswear Ltd - Master Client"]
df = df.sort_values(['Master Client','Year','Week'])

# Feature engineering (example)
df['volume_change'] = df.groupby('Master Client')['Pieces'].pct_change()
df['recency'] = df.groupby('Master Client').cumcount(ascending=False)
df['frequency'] = df.groupby('Master Client')['Pieces'].transform('count')

# Define churn (example)
df['churn'] = df['Pieces'].shift(-1).isna().astype(int)

# Prepare features and target
features = ['volume_change', 'recency', 'frequency']
X = df[features].fillna(0)
y = df['churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_pred_prob))
