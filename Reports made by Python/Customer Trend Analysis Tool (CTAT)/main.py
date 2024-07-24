import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymannkendall as mk
from functions import process_excel
from plots import plot_trend_lines
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

last_week_2024 = 29
starting_year =2023
ending_year = 2024
# Load your dataset
path = r'Input/your_dataset.xlsx'
db = process_excel(path)

condition = ((db['Year']<ending_year)&(db['Year']>=starting_year)) |((db['Year']==ending_year) & (db['Week']<=last_week_2024))
db = db[condition]
db['Master Client'] = db['Master Client'].fillna("No Master Customer")


holidays = pd.read_excel(r'C:\My Folder\Forecasts\Holidays_2025.xlsx',sheet_name='Working Days by Week')
holidays = holidays[['Year', 'Week Number','Working Days']].drop_duplicates().rename(columns= {'Week Number':'Week'})

years = db['Year'].unique()
weeks = range(1, int(max(db['Week'])))  # Assuming weeks 1 to 52
master_clients = db['Master Client'].unique()
complete_weeks = pd.MultiIndex.from_product([years, weeks, master_clients], names=['Year', 'Week', 'Master Client'])
complete_weeks_df = pd.DataFrame(index=complete_weeks).reset_index()
condition = ((complete_weeks_df['Year']<ending_year)&(complete_weeks_df['Year']>=starting_year)) |((complete_weeks_df['Year']==ending_year) & (complete_weeks_df['Week']<=last_week_2024))
complete_weeks_df = complete_weeks_df[condition]
# Group by and sum
grouped_db = db.groupby(['Year', 'Week', 'Master Client'])['Pieces'].sum().reset_index()

# Merge complete weeks with the grouped data
merged_db = complete_weeks_df.merge(grouped_db, on=['Year', 'Week', 'Master Client'], how='left')
# Fill NaN values with 0
merged_db['Pieces'] = merged_db['Pieces'].fillna(0)


merged_db = merged_db.merge(holidays,on=['Year','Week'])
merged_db['daily_avg'] = round(merged_db['Pieces']/merged_db['Working Days'],1)
merged_db = merged_db.sort_values(['Master Client','Year','Week'])

customer_total = merged_db[merged_db['Year']>=2024].groupby('Master Client')['daily_avg'].mean().reset_index()
customer_total = customer_total.sort_values('daily_avg',ascending=False)
customer_list = list(customer_total[customer_total['daily_avg']>=100]['Master Client'])
result_db = {}
# Create a PDF object
pdf_pages = PdfPages("Customer Trend Analysis_2023.pdf")


for cus in customer_list:
    print(f'start working on {cus}')
    data = merged_db[merged_db['Master Client'] == cus]
    #data = data[data['Year'] >= 2024]

    # Calculate weekly percentage change
    data['Pct_Change'] = data.groupby('Master Client')['daily_avg'].pct_change()
    data['Pct_Change'].fillna(0, inplace=True)

    # Calculate rolling 4-weeks and 8-weeks
    #data['4Moving_Avg'] = round(data.groupby('Master Client')['Pct_Change'].transform(lambda x: x.rolling(window=4).sum()), 2)
    #data['8Moving_Avg'] = round(data.groupby('Master Client')['Pct_Change'].transform(lambda x: x.rolling(window=8).sum()), 2)
    #data['CumMoving_Avg'] = round(data.groupby('Master Client')['Pct_Change'].cumsum(), 2)

    # Mann-Kendall test
    result = mk.original_test(data['daily_avg'])
    # Print Mann-Kendall test result
    #print(f"Mann-Kendall Test for {cus}: Trend: {result.trend}, P-value: {result.p:.2f}, Significance: {'Significant' if result.p < 0.05 else 'Not Significant'}")
    result_db[cus] = [result.trend,result.p,'Significant' if result.p < 0.05 else 'Not Significant',round(customer_total[customer_total['Master Client']==cus].iloc[0,1],0)]
    
    #customer_fig = plot_trend_lines(data, result_db, "Customer Trend Analysis_2023.pdf", last_week_2024)
    #pdf_pages.savefig(customer_fig)
    #print(f'{cus} is done')

pdf_pages.close()
result_db = pd.DataFrame.from_dict(result_db, orient='index',columns=['trend','p_value','Sig_or_NotSig','magnitude of daily_avg'])
result_db.to_excel('result_2023_1.xlsx')

