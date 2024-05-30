# IMPORT LIBRARIES ------------------------------------------------------------
import pandas as pd
import mysql.connector as connection
from datetime import datetime,timedelta
import numpy as np
import datetime
from datetime import timedelta
import os

# First run cg_distribution for EID and then run this

########################################## Import files
# Import Forecast
folder_path =r"C:\My Folder\Forecasts\CG Forecast\CG EID\Output"
edd_folder_path = r"C:\My Folder\Forecasts\CG Forecast\CG EDD\Output"
db = pd.read_excel(os.path.join(folder_path,'ForecastResults.xlsx'),sheet_name='Forecast')
volumes = pd.read_excel(os.path.join(edd_folder_path,'ForecastResults.xlsx'),sheet_name="Forecast")


#peak_weeks = (47,48,49,50,51,52)
peak_weeks = list(np.arange(min(db['Week']),max(db['Week']+1)))
print(f"the script redistribute {peak_weeks}")

# calculating total volume for peak period by terminals and customers
df = db.query(f" `Week` in {peak_weeks}")
total_eid_volume = df.groupby(['Year','Week','Customer'])['Pieces'].sum().reset_index()
df = df.merge(total_eid_volume,on=['Year','Week','Customer'],how='left')
df['terminal distribution'] = df['Pieces_x']/df['Pieces_y']
df['terminal distribution'] = df['terminal distribution'].fillna(0)


total_volumes = volumes.groupby(['Year','Week','Customer'])['Pieces'].sum().reset_index()

df = df.merge(total_volumes,on=['Year','Week','Customer'],how='left',)
df['new pieces'] = df['Pieces']*df['terminal distribution']


df = df[['Year','Week','Customer','Terminal','new pieces']].rename(columns={'new pieces':'Pieces'})
df = df.sort_values(['Year','Week','Customer','Terminal'])
df['Pieces'] = 0.988*df['Pieces']

df.to_csv(os.path.join(folder_path,'coverting_edd_volumes_to_eid.csv'),index=False)