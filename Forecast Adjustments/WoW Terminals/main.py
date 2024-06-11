#main.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('wow_2.xlsx')
df = df.iloc[1:,:]






# Define the weeks for comparison
# Example: Compare weeks 21 and 22 against weeks 19 and 20
current_weeks = [20]
previous_weeks = [17]

# Filter data for the specified weeks
current_weeks_df = df[df['Week'].isin(current_weeks)]
previous_weeks_df = df[df['Week'].isin(previous_weeks)]

# Calculate total volume for each customer in the specified weeks
volume_current_weeks = current_weeks_df.groupby('Master Client')['Pieces'].sum().reset_index()
volume_current_weeks.columns = ['Master Client', 'Volume_Current_Weeks']

volume_previous_weeks = previous_weeks_df.groupby('Master Client')['Pieces'].sum().reset_index()
volume_previous_weeks.columns = ['Master Client', 'Volume_Previous_Weeks']

# Merge the two dataframes
volume_comparison = pd.merge(volume_current_weeks, volume_previous_weeks, on='Master Client', how='outer').fillna(0)

# Calculate the amount of increase
volume_comparison['Volume_Increase'] = volume_comparison['Volume_Current_Weeks'] - volume_comparison['Volume_Previous_Weeks']

# Filter top 5 customers with volume increase
top_customers_with_increase = volume_comparison.nlargest(5, 'Volume_Increase')

# Filter bottom 8 customers with volume decrease
bottom_customers_with_decrease = volume_comparison.nsmallest(8, 'Volume_Increase')

# Function to plot line chart for a customer
def plot_customer_trend(customer, df):
    customer_data = df[df['Master Client'] == customer]
    plt.figure(figsize=(10, 5))
    plt.plot(customer_data['Week'], customer_data['Pieces'], marker='o')
    plt.title(f'{customer} trend')
    plt.xlabel('Weeks')
    plt.ylabel('Pieces')
    plt.xticks(df['Week'].unique())  # Set xticks to the unique weeks in the dataframe
    plt.grid(True)
    plt.show()

# Plot line charts for top 5 customers with highest increase in volume
for customer in top_customers_with_increase['Master Client']:
    plot_customer_trend(customer, df)

# Plot line charts for bottom 8 customers with highest decline in volume
for customer in bottom_customers_with_decrease['Master Client']:
    plot_customer_trend(customer, df)