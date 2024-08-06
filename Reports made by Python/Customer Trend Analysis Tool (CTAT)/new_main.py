import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymannkendall as mk
from functions import process_excel
from plots import plot_trend_lines
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

last_week_2024 = 29
starting_year = 2023
ending_year = 2024
daily_avg_threshold = 50

# Load your dataset
path = r'Input/db.xlsx'
db = process_excel(path)

# Filter the data
condition = ((db['Year'] < ending_year) & (db['Year'] >= starting_year)) | ((db['Year'] == ending_year) & (db['Week'] <= last_week_2024))
db = db[condition]
db['Master Client'] = db['Master Client'].fillna("No Master Customer")

holidays = pd.read_excel(r'C:\\My Folder\\Forecasts\\Holidays_2025.xlsx', sheet_name='Working Days by Week')
holidays_on = holidays[holidays['Province']=="ON"]
holidays = holidays_on[['Year', 'Week Number', 'Working Days']].drop_duplicates().rename(columns={'Week Number': 'Week'})

years = db['Year'].unique()
weeks = range(1, int(max(db['Week'])))  # Assuming weeks 1 to 52
master_clients = db['Master Client'].unique()
complete_weeks = pd.MultiIndex.from_product([years, weeks, master_clients], names=['Year', 'Week', 'Master Client'])
complete_weeks_df = pd.DataFrame(index=complete_weeks).reset_index()
condition_2 = ((complete_weeks_df['Year'] < ending_year) & (complete_weeks_df['Year'] >= starting_year)) | ((complete_weeks_df['Year'] == ending_year) & (complete_weeks_df['Week'] <= last_week_2024))
complete_weeks_df = complete_weeks_df[condition_2]

# Group by and sum
grouped_db = db.groupby(['Year', 'Week', 'Master Client'])['Pieces'].sum().reset_index()

# Merge complete weeks with the grouped data
merged_db = complete_weeks_df.merge(grouped_db, on=['Year', 'Week', 'Master Client'], how='left')
merged_db['Pieces'] = merged_db['Pieces'].fillna(0)
merged_db = merged_db.merge(holidays, on=['Year', 'Week'])
merged_db['daily_avg'] = round(merged_db['Pieces'] / merged_db['Working Days'], 2)

# Functions to calculate daily averages per customer
def calculate_daily_average_2023_ytd(db):
    return db[(db['Year'] == 2023) & (db['Week'] <= last_week_2024)].groupby('Master Client')['daily_avg'].mean()

def calculate_daily_average_2023_full_year(db):
    return db[db['Year'] == 2023].groupby('Master Client')['daily_avg'].mean()

def calculate_daily_average_2024_ytd(db):
    return db[(db['Year'] == 2024) & (db['Week'] <= last_week_2024)].groupby('Master Client')['daily_avg'].mean()

avg_2023_ytd = calculate_daily_average_2023_ytd(merged_db)
avg_2023_full_year = calculate_daily_average_2023_full_year(merged_db)
avg_2024_ytd = calculate_daily_average_2024_ytd(merged_db)


customer_total = merged_db[merged_db['Year'] >= 2024].groupby('Master Client')['daily_avg'].mean().reset_index()
customer_total = customer_total.sort_values('daily_avg', ascending=False)
customer_list = list(customer_total[customer_total['daily_avg'] >= daily_avg_threshold]['Master Client'])
result_db = {}

# Create a PDF object
#pdf_pages = PdfPages("Customer Trend Analysis_2023.pdf")
for cus in customer_list:
    print(f'start working on {cus}')
    data = merged_db[merged_db['Master Client'] == cus]

    data = data.sort_values(['Year','Week'])

    # Calculate weekly percentage change
    data['Pct_Change'] = data.groupby('Master Client')['daily_avg'].pct_change()
    data['Pct_Change'].fillna(0, inplace=True)

    # Mann-Kendall test
    result = mk.original_test(data['daily_avg'])
    result_db[cus] = [result.trend, result.p, 'Significant' if result.p < 0.05 else 'Not Significant', round(avg_2024_ytd[cus],0),round(avg_2023_ytd[cus],0),round(avg_2023_full_year[cus],0)]

#pdf_pages.close()
result_db = pd.DataFrame.from_dict(result_db, orient='index', columns=['Trend', 'P_value', 'Sig_or_NotSig', '2024 YTD Daily Avg','2023 YTD Daily Avg','2023 Full Year Daily Avg'])
result_db = result_db.rename_axis('Master Client').reset_index()
result_db['Change in Daily Avg'] = result_db['2024 YTD Daily Avg'] - result_db['2023 YTD Daily Avg']
result_db['% Change'] = round(result_db['2024 YTD Daily Avg'] / result_db['2023 YTD Daily Avg'] - 1 ,1)
result_db['% Change'].replace([np.inf],1,inplace=True)


conditions = [
    (result_db['2024 YTD Daily Avg'] >= 20000),
    (result_db['2024 YTD Daily Avg'] < 20000) & (result_db['2024 YTD Daily Avg'] >= 3000),
    (result_db['2024 YTD Daily Avg'] < 3000) & (result_db['2024 YTD Daily Avg'] >= 1000),
    (result_db['2024 YTD Daily Avg'] < 1000) & (result_db['2024 YTD Daily Avg'] >= 100),
    (result_db['2024 YTD Daily Avg'] < 100)
]

choices = ['1', '2', '3', '4', '5']

result_db['Tier'] = np.select(conditions, choices)
result_db['Tier'] = result_db['Tier'].astype(int)

Final_df = merged_db.merge(result_db[['Master Client','Tier']],on='Master Client',how='left')
Final_df = Final_df[Final_df['Master Client'].isin(customer_list)]
Final_df.to_excel(f'Output\weekly_data_more_than_{daily_avg_threshold}_daily_avg_pcs.xlsx')


result_db.to_excel(r'Output\Customer Trend Analysis Tool (CTAT) output.xlsx')