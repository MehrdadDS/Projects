import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt


data = pd.read_excel(r'Input\data.xlsx')
data = data.iloc[1:,:]

print(data.head(100))





# Step 1: Aggregate weekly data for each customer and terminal
weekly_data = data.groupby(['Year', 'Week', 'Master Client']).sum().reset_index()
terminal_weekly_data = data.groupby(['Year', 'Week']).sum().reset_index()

# Step 2: Calculate customer volume as a proportion of terminal volume
weekly_data = weekly_data.merge(terminal_weekly_data[['Year', 'Week', 'Pieces']], on=['Year', 'Week'], suffixes=('', '_terminal'))
weekly_data['Proportion'] = weekly_data['Pieces'] / weekly_data['Pieces_terminal']

# Ensure valid data by dropping rows with NaN values
weekly_data = weekly_data.dropna(subset=['Week', 'Proportion'])

# Step 3: Perform trend analysis using linear regression
def detect_trend(group):
    with np.errstate(invalid='ignore'):
        slope, intercept, r_value, p_value, std_err = linregress(group['Week'], group['Proportion'])
    return pd.Series({'slope': slope, 'p_value': p_value, 'trend': 'increasing' if slope > 0 else 'decreasing'})

# Apply the trend analysis to each customer
trend_data = weekly_data.groupby('Master Client').apply(detect_trend).reset_index()

# Step 4: Filter significant trends (e.g., p_value < 0.05)
significant_trends = trend_data[trend_data['p_value'] < 0.05]

# Step 5: Separate the most inclined and declined customers
top_incline = significant_trends[significant_trends['slope'] > 0].nlargest(10, 'slope')
top_decline = significant_trends[significant_trends['slope'] < 0].nsmallest(15, 'slope')

# Plot the trends for the top inclined customers in subplots
fig, axs = plt.subplots(5, 2, figsize=(15, 20))
axs = axs.flatten()

for i, client in enumerate(top_incline['Master Client']):
    client_data = weekly_data[weekly_data['Master Client'] == client]
    axs[i].plot(client_data['Week'], client_data['Pieces'])
    axs[i].set_title(client)
    #axs[i].set_xlabel('Week')
    axs[i].set_ylabel('Pieces')
    axs[i].set_xticks(client_data['Week'])

fig.suptitle('Top 10 Customers with Most Incline in Volume - EDMONTON NORTH', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.subplots_adjust(top=0.92, hspace=0.5)
plt.show()

# Plot the trends for the top declined customers in subplots
fig, axs = plt.subplots(5, 3, figsize=(20, 25))
axs = axs.flatten()

for i, client in enumerate(top_decline['Master Client']):
    client_data = weekly_data[weekly_data['Master Client'] == client]
    axs[i].plot(client_data['Week'], client_data['Pieces'])
    axs[i].set_title(client)
    #axs[i].set_xlabel('Week')
    axs[i].set_ylabel('Pieces')
    axs[i].set_xticks(client_data['Week'])

fig.suptitle('Top 15 Customers with Most Decline in Volume - EDMONTON NORTH', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.subplots_adjust(top=0.92, hspace=0.5)
plt.show()