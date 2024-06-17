import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymannkendall as mk

# Load your dataset
db = pd.read_excel(r'Input/your_dataset.xlsx')#,nrows=1000)
db =db.iloc[1:,:]
holidays = pd.read_excel(r'C:\My Folder\Forecasts\Holidays_2025.xlsx',sheet_name='Working Days by Week')
holidays = holidays[['Year', 'Week Number','Working Days']].drop_duplicates().rename(columns= {'Week Number':'Week'})
db['Master Client'] = db['Master Client'].fillna("No Master Customer")

years = db['Year'].unique()
weeks = range(1, int(max(db['Week'])))  # Assuming weeks 1 to 52
master_clients = db['Master Client'].unique()
complete_weeks = pd.MultiIndex.from_product([years, weeks, master_clients], names=['Year', 'Week', 'Master Client'])
complete_weeks_df = pd.DataFrame(index=complete_weeks).reset_index()
# Group by and sum
grouped_db = db.groupby(['Year', 'Week', 'Master Client'])['Pieces'].sum().reset_index()

# Merge complete weeks with the grouped data
merged_db = complete_weeks_df.merge(grouped_db, on=['Year', 'Week', 'Master Client'], how='left')
# Fill NaN values with 0
merged_db['Pieces'] = merged_db['Pieces'].fillna(0)


merged_db = merged_db.merge(holidays,on=['Year','Week'])
merged_db['daily_avg'] = round(merged_db['Pieces']/merged_db['Working Days'],1)
merged_db = merged_db.sort_values(['Master Client','Year','Week'])

customer_total = merged_db.groupby('Master Client')['daily_avg'].mean().reset_index()
customer_list = sorted(list(customer_total[customer_total['daily_avg']>=20]['Master Client']))

result_db = {}
for cus in customer_list:
    print(f'start working on {cus}')
    data = merged_db[merged_db['Master Client'] == cus]
    data = data[data['Year'] >= 2024]

    # Calculate weekly percentage change
    data['Pct_Change'] = data.groupby('Master Client')['daily_avg'].pct_change()
    data['Pct_Change'].fillna(0, inplace=True)

    # Calculate rolling 4-weeks and 8-weeks
    data['4Moving_Avg'] = round(data.groupby('Master Client')['Pct_Change'].transform(lambda x: x.rolling(window=4).sum()), 2)
    data['8Moving_Avg'] = round(data.groupby('Master Client')['Pct_Change'].transform(lambda x: x.rolling(window=8).sum()), 2)
    data['CumMoving_Avg'] = round(data.groupby('Master Client')['Pct_Change'].cumsum(), 2)

    # Mann-Kendall test
    result = mk.original_test(data['daily_avg'])

    """
    # Plotting the chart
    plt.figure(figsize=(12, 8))
    for year in data['Year'].unique():
        subset = data[data['Year'] == year]
        plt.plot(subset['Week'], subset['CumMoving_Avg'], marker='o', label='Cumulative')
        plt.plot(subset['Week'], subset['4Moving_Avg'], marker='o', label='4weeks')
        plt.plot(subset['Week'], subset['8Moving_Avg'], marker='o', label='8weeks')
    
    plt.xlabel('Week')
    plt.title(f'{cus} - {"Uptrend" if result.trend == "increasing" else "Downtrend"} (p-value: {result.p:.2f})')
    plt.xticks(data['Week'])
    plt.title(f'{cus}')
    plt.legend(title='Year')
    plt.ylabel("%_change")
    plt.grid(True)
    
    #plt.show()

    # Plotting daily_avg
    plt.figure(figsize=(12, 8))
    plt.plot(data['Week'], data['daily_avg'], marker='o')
    plt.xlabel('Week')
    plt.xticks(data['Week'])
    plt.ylabel('daily_avg')
    plt.grid(True)
    #plt.show()

    # Additional metric: Rolling standard deviation
    data['Rolling_Std'] = round(data.groupby('Master Client')['Pct_Change'].transform(lambda x: x.rolling(window=8).std()), 2)
    
    # Visualization of rolling standard deviation
    plt.figure(figsize=(12, 8))
    plt.plot(data['Week'], data['Rolling_Std'], marker='o', color='purple')
    plt.xlabel('Week')
    plt.xticks(data['Week'])
    plt.ylabel('Rolling Std Dev of % Change')
    plt.title(f'{cus} - Rolling Std Dev of % Change')
    plt.grid(True)
    #plt.show()
"""
    # Print Mann-Kendall test result
    #print(f"Mann-Kendall Test for {cus}: Trend: {result.trend}, P-value: {result.p:.2f}, Significance: {'Significant' if result.p < 0.05 else 'Not Significant'}")
    result_db[cus] = [result.trend,result.p,'Significant' if result.p < 0.05 else 'Not Significant',round(customer_total[customer_total['Master Client']==cus].iloc[0,1],0)]
    #print(f'{cus} is done')


result_db = pd.DataFrame.from_dict(result_db, orient='index',columns=['trend','p_value','Sig_or_NotSig','magnitude of daily_avg'])
result_db.to_excel('res.xlsx')