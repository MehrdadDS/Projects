# IMPORT LIBRARIES ------------------------------------------------------------
import pandas as pd
import mysql.connector as connection
from datetime import datetime,timedelta
import numpy as np
import datetime
from datetime import timedelta
import os

########################################## Import files
# Import Forecast
folder_path =r"C:\My Folder\Forecasts\CG Forecast\CG EID\Output"
db = pd.read_excel(os.path.join(folder_path,'ForecastResults.xlsx'),sheet_name='Forecast')
distributions = pd.read_excel(os.path.join(folder_path,'ForecastResults - distribution.xlsx'),sheet_name="Forecast")

peak_weeks = (47,48,49,50,51,52)
print(f"the script redistribute {peak_weeks}")

# calculating total volume for peak period by terminals and customers
df = db.query(f" `Week` in {peak_weeks}")
df_total = df.groupby(['Year','Customer','Terminal'])['Pieces'].sum().reset_index()
df = df.merge(df_total,on=['Year','Customer','Terminal'],how='left')


# Calculating % based on distribution file
dis = distributions.query(f" `Week` in {peak_weeks}")
dis_total = dis.groupby(['Year','Customer','Terminal'])['Pieces'].sum().reset_index()
dis = dis.merge(dis_total,on=['Year','Customer','Terminal'],how='left')
dis['weekly distribution'] = dis['Pieces_x']/dis['Pieces_y']
dis['weekly distribution'] = dis['weekly distribution'].fillna(0)


# Calculating new peak distribuion
df = df.merge(dis[['Year','Week','Terminal','Customer','weekly distribution']],how='left',on=['Year','Week','Terminal','Customer'])
df['New Pieces'] = df['weekly distribution']*df['Pieces_y']
df_new_peak = df[['Year','Week','Customer','Terminal','New Pieces']].rename(columns={'New Pieces':'Pieces'})

df_rest_year = db.query(f" `Week` not in {peak_weeks}")

final_result = pd.concat([df_new_peak,df_rest_year]).sort_values(by=['Year','Week','Customer','Terminal'])

final_result.to_csv(os.path.join(folder_path,"forecast_result_after_redistribution.csv"),index=False)