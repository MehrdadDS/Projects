import pandas as pd
import plots
import functions

last_week_2024 = 27


db = pd.read_excel(r'Input/db.xlsx')
db =db.iloc[1:,:]
db['Master Client'] = db['Master Client'].fillna("No Master Customer")
df_averages = db[(db['Year']==2024) & (db['Week']<=last_week_2024)]

holidays = pd.read_excel(r'C:\My Folder\Forecasts\Holidays_2025.xlsx',sheet_name='Working Days by Week')
holidays = holidays[['Year', 'Week Number','Working Days']].drop_duplicates().rename(columns= {'Week Number':'Week'})

""" Calculating daily average volume for 2024 customers  """
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
db_groupby = merged_db.groupby(['Master Client'])['daily_avg'].mean().reset_index()

customers_list = db_groupby[['Master Client','daily_avg']].sort_values('daily_avg',ascending=False)
import numpy as np

conditions = [
    (customers_list['daily_avg'] >= 20000),
    (customers_list['daily_avg'] < 20000) & (customers_list['daily_avg'] >= 3000),
    (customers_list['daily_avg'] < 3000) & (customers_list['daily_avg'] >= 1000),
    (customers_list['daily_avg'] < 1000) & (customers_list['daily_avg'] >= 100),
    (customers_list['daily_avg'] < 100)
]

choices = ['1', '2', '3', '4', '5']

customers_list['Tier'] = np.select(conditions, choices)


print('Daily averages has been calculated!')

#final_df = merged_db.merge(customers_list[['Master Client','Tier']],on=['Master Client'])

#db = pd.read_excel(r'Input/db.xlsx')
#db = db.iloc[1:,:]
#db['Master Client'] = db['Master Client'].fillna("No Master Customer")

db = db[(db['Year']<2024)|((db['Year']==2024) & (db['Week']<=last_week_2024)) ]
db = db.merge(customers_list[['Master Client','Tier']],on='Master Client',how='left')
db['Tier'] = db['Tier'].fillna('Zero Volume 2024')

plots.plot_tier_pieces_by_week(db, 'Weekly Pieces by Tier and Year', 'Tier')


""" Calculating YoY YTD decline and incline """
#db1 = functions.classify_clients_based_volumes(db,50000,-45000)
#plots.plot_tier_pieces_by_week(db1, 'Weekly Pieces by Group and Year', 'Group')
#plots.plot_tier_pieces_by_week(db1[db1['Group']=='Group C'], 'Weekly Pieces by Group and Year, Focusing on Group C', 'Tier')

db2 = functions.classify_clients_sorted(db,30,30)
plots.plot_tier_pieces_by_week(db2, 'Weekly Delivery Pieces by Customer Group and Year', 'Group')
plots.plot_tier_pieces_by_week(db2[db2['Group']=='Moderate Performers'], 'Weekly Pieces by Group and Year, Focusing on Moderate Performers', 'Tier')

#plots.plot_customers_by_group(db, 'main_title', group_column='Tier')

result = functions.calculate_ytd_changes(db2)
result.to_excel('Inclinersordecliners_basedontop.xlsx', index=False)


print('Excel file needs to be updated!')