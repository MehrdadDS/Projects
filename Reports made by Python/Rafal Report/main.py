import pandas as pd

df_averages = pd.read_excel(r'Input/customers_averages.xlsx')
df_averages =df_averages.iloc[1:,:]
df_averages['Master Client'] = df_averages['Master Client'].fillna("No Master Customer")


holidays = pd.read_excel(r'C:\My Folder\Forecasts\Holidays_2025.xlsx',sheet_name='Working Days by Week')
holidays = holidays[['Year', 'Week Number','Working Days']].drop_duplicates().rename(columns= {'Week Number':'Week'})


years = df_averages['Year'].unique()
weeks = range(1, int(max(df_averages['Week'])))  # Assuming weeks 1 to 52
master_clients = df_averages['Master Client'].unique()
complete_weeks = pd.MultiIndex.from_product([years, weeks, master_clients], names=['Year', 'Week', 'Master Client'])
complete_weeks_df = pd.DataFrame(index=complete_weeks).reset_index()
# Group by and sum
grouped_db = df_averages.groupby(['Year', 'Week', 'Master Client'])['Pieces'].sum().reset_index()

# Merge complete weeks with the grouped data
merged_db = complete_weeks_df.merge(grouped_db, on=['Year', 'Week', 'Master Client'], how='left')
# Fill NaN values with 0
merged_db['Pieces'] = merged_db['Pieces'].fillna(0)

merged_db = merged_db.merge(holidays,on=['Year','Week'])
merged_db['daily_avg'] = round(merged_db['Pieces']/merged_db['Working Days'],1)
merged_db = merged_db.sort_values(['Master Client','Year','Week'])