# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:52:47 2022

@author: Mehrdad.Dadgar
"""

# IMPORT LIBRARIES ------------------------------------------------------------
import pandas as pd
import mysql.connector as connection
from datetime import datetime,timedelta
import numpy as np
import datetime
from datetime import timedelta


########################################## Import files
# Import Forecast

df = pd.read_excel('C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_modified.xlsx')
distributions = pd.read_excel('C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\May 7\ForecastResults-Check- April 25th- Checking 2024.xlsm',sheet_name="Actual")


df.columns = ['Division', 'District', 'Terminal', 'Terminal.Name', 'Province', 'Year','Quarter', 'Period.Number','Week'
              , 'PCL.Del.Pcs.N','PCL.Del.Stops.N', 'PCL.PU.Pcs.N', 'PCL.PU.Stops.N', 'Agent.Del.Pcs.N',
              'Agent.PU.Pcs.N', 'Total.Del.Stops.N', 'Total.PU.Stops.N']

 
distributions = distributions.iloc[:,:17]
distributions.columns = df.columns 

#-----------------------------------------------------------------------------
#Changing distribution
distributions = distributions[distributions['Year']==2024]
#adjusting_variables = ['PCL.Del.Pcs.N', 'PCL.Del.Stops.N','PCL.PU.Pcs.N', 'PCL.PU.Stops.N',
#                       'Agent.Del.Pcs.N', 'Agent.PU.Pcs.N','Total.Del.Stops.N', 'Total.PU.Stops.N']
adjusting_variables = {'PCL.Del.Pcs.N','PCL.Del.Stops.N','Agent.Del.Pcs.N','Total.Del.Stops.N'}


db_peak     =  df.query("`Week` in (47,48,49,50,51,52) and `Year`==2024")
db_non_peak =  df.query("`Week` not in (47,48,49,50,51,52) or `Year`!=2024")

for var in adjusting_variables:
    
    dis =  distributions.query(" `Week` in (47,48,49,50,51,52)")
    
    print(var)
    #i = 'PCL.Del.Pcs.N'
    df_non_peak = df[['Terminal','Year','Week'] + [var]].query("`Week` not in (47,48,49,50,51,52) or `Year`!=2024")
    df_non_peak.columns = ['Terminal','Year','Week']+[var]
    df_peak = df[['Terminal','Year','Week'] + [var]].query("`Week` in (47,48,49,50,51,52) and `Year`==2024")
    df_peak.columns = ['Terminal','Year','Week']+[var]
    df_peak_groupby = pd.DataFrame(df_peak.groupby(['Year','Terminal'])[var].sum()).reset_index()
    df_peak_groupby.columns = ['Year','Terminal','Total']
    df_peak = pd.merge(df_peak,df_peak_groupby[['Year','Terminal','Total']])
    
    dis = dis[['Year','Terminal','Week'] + [var]]
    dis_groupby = dis.groupby(['Year','Terminal'])[var].sum().reset_index()
    dis = pd.merge(dis, dis_groupby,on=['Year','Terminal'])
    dis['dis'] = dis[var+"_x"]/dis[var+"_y"]
    dis.columns =['Year', 'Terminal','Week']+[var]+['Total', 'dis']
    
    df_peak_new = pd.merge(df_peak, dis[['Year','Week','Terminal','dis']],on=['Year','Week','Terminal'])
    df_peak_new['New_value'] = df_peak_new['dis']*df_peak_new['Total']
    #df_final = pd.merge(df_peak_new,dis[['Year','Week', 'Terminal']+[var]],on=['Year','Week', 'Terminal'])
    #df_final = pd.concat([df_final,df_non_peak],axis=0)
    df_peak_new = df_peak_new.sort_values(by=['Terminal','Week','Year'])
    
    #df_final.loc[df_final['New_value'].isnull(),'New_value'] = df_final.loc[df_final['New_value'].isnull(),var]
    db_peak = pd.merge(db_peak,df_peak_new[['Terminal', 'Year', 'Week', 'New_value']],on=['Terminal', 'Year', 'Week'])  
    db_peak['New_value'] = db_peak['New_value'].fillna(0)
    db_peak = db_peak.drop(var,axis=1)
    db_peak = db_peak.rename(columns={'New_value':var+'_EDITED'})


db_peak = db_peak[['Division', 'District', 'Terminal', 'Terminal.Name', 'Province', 'Year','Quarter', 'Period.Number', 'Week',
                    'PCL.Del.Pcs.N_EDITED','PCL.Del.Stops.N_EDITED','PCL.PU.Pcs.N', 'PCL.PU.Stops.N', 'Agent.Del.Pcs.N_EDITED',
                    'Agent.PU.Pcs.N','Total.Del.Stops.N_EDITED', 'Total.PU.Stops.N']]

db_non_peak.columns = db_peak.columns

finalized_db = pd.concat([db_non_peak,db_peak],axis=0)
finalized_db = finalized_db.sort_values(by=['Terminal','Year','Week'])

finalized_db.to_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_edited_usingPython_version.xlsx')

#df.to_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_modified.xlsx')
