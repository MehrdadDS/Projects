import pandas as pd
import numpy as np

# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Calculate weekly percentage change
data = data[data['Master Client']== "Columbia Sportswear Ltd - Master Client"]

data['Pct_Change'] = data.groupby('Master Client')['Pieces'].pct_change()

# Calculate 4-week moving average
data['Moving_Avg'] = data.groupby('Master Client')['Pieces'].transform(lambda x: x.rolling(window=4).mean())

# Calculate volatility (standard deviation of the last 4 weeks)
data['Volatility'] = data.groupby('Master Client')['Pieces'].transform(lambda x: x.rolling(window=4).std())

# Define churn: Label instances where the volume drops below a threshold
threshold = 0.5
data['Churn'] = data['Pct_Change'].apply(lambda x: 1 if x < -threshold else 0)

# Example features: Weekly change, Moving average, Volatility
features = data[['Pct_Change', 'Moving_Avg', 'Volatility']]
labels = data['Churn']

# Handle missing values
features = features.fillna(0)


