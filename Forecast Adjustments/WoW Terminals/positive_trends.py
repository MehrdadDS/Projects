#main.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


df = pd.read_excel('wow_2.xlsx')
df = df.iloc[1:,:]

# Fill missing values for the sake of regression analysis
df['Master Client'] = df['Master Client'].fillna('Unknown')

# User-defined threshold for weekly average volume
threshold = 100

# Function to perform linear regression and check if the trend is positive
def check_positive_trend(df, customer):
    customer_data = df[df['Master Client'] == customer]
    if len(customer_data) < 2:
        return False, 0  # Not enough data to determine a trend
    X = customer_data['Week'].values.reshape(-1, 1)
    y = customer_data['Pieces'].values
    model = LinearRegression()
    model.fit(X, y)
    trend = model.coef_[0]  # Slope of the fitted line
    return trend > 0, trend

# Identify customers with a positive trend
positive_trend_customers = []

for customer in df['Master Client'].unique():
    customer_data = df[df['Master Client'] == customer]
    if customer_data['Week'].nunique() == df['Week'].nunique():  # Check if the customer has data for every week
        avg_volume = customer_data['Pieces'].mean()
        if avg_volume >= threshold:  # Check if the weekly average volume is above the threshold
            positive_trend, trend_value = check_positive_trend(df, customer)
            if positive_trend:
                positive_trend_customers.append((customer, trend_value))

# Sort customers by the strength of their positive trend
positive_trend_customers = sorted(positive_trend_customers, key=lambda x: x[1], reverse=True)

# Plot line charts for customers with a positive trend
for customer, trend_value in positive_trend_customers:
    customer_data = df[df['Master Client'] == customer]
    plt.figure(figsize=(10, 5))
    plt.plot(customer_data['Week'], customer_data['Pieces'], marker='o')
    plt.title(f'{customer} trend (Positive Slope: {trend_value:.2f})')
    plt.xlabel('Weeks')
    plt.ylabel('Pieces')
    plt.xticks(df['Week'].unique())  # Set xticks to the unique weeks in the dataframe
    plt.grid(True)
    plt.show()

# Display the names and trend values of customers with positive trends
positive_trend_df = pd.DataFrame(positive_trend_customers, columns=['Master Client', 'Trend Value'])
print(positive_trend_df)