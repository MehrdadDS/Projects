# IMPORT LIBRARIES ------------------------------------------------------------
import pandas as pd
import mysql.connector as connection
from datetime import datetime,timedelta
import numpy as np
import datetime
from datetime import timedelta


########################################## Import files
# Import Forecast
db = pd.read_excel('C:\My Folder\Forecasts\CG Forecast\CG EDD\Output\ForecastResults.xlsx',sheet_name='Forecast')
distributions = pd.read_excel('c:\My Folder\Forecasts\CG Forecast\CG EDD\Output\ForecastResults - distribution.xlsx',sheet_name="Forecast")

# calculating total volume for peak period by terminals and customers
df = db.query(" `Week` in (47,48,49,50,51,52)")
df_total = df.groupby(['Year','Customer','Terminal'])['Pieces'].sum().reset_index()
df = df.merge(df_total,on=['Year','Customer','Terminal'],how='left')


# Calculating % based on distribution file
dis = distributions.query(" `Week` in (47,48,49,50,51,52)")
dis_total = dis.groupby(['Year','Customer','Terminal'])['Pieces'].sum().reset_index()
dis = dis.merge(dis_total,on=['Year','Customer','Terminal'],how='left')