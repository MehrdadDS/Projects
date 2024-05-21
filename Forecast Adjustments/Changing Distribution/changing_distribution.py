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
df = pd.read_excel('C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet.xlsx',sheet_name='Forecast')
distributions = pd.read_excel('C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\May 7\ForecastResults-Check- April 25th- Checking 2024.xlsm',sheet_name="Actual")


df.columns = ['Division', 'District', 'Terminal', 'Terminal.Name', 'Province', 'Year','Quarter', 'Period.Number','Week'
              , 'PCL.Del.Pcs.N','PCL.Del.Stops.N', 'PCL.PU.Pcs.N', 'PCL.PU.Stops.N', 'Agent.Del.Pcs.N',
              'Agent.PU.Pcs.N', 'Total.Del.Stops.N', 'Total.PU.Stops.N']

 
distributions = distributions.iloc[:,:17]
distributions.columns = df.columns 

#-----------------------------------------------------------------------------
#Changing distribution
distributions = distributions[distributions['Year']==2024]
adjusting_variables = ['PCL.Del.Pcs.N','PCL.Del.Stops.N','Agent.Del.Pcs.N','Total.Del.Stops.N']
#col_adj = {'PCL.Del.Pcs.N':'PCL Pcs','PCL.Del.Stops.N':'Stops','Agent.Del.Pcs.N':'Agent Pcs','Total.Del.Stops.N':'Stops'}


df_NEW = df
for var in adjusting_variables:
    
    dis =  distributions.query(" `Week` in (47,48,49,50,51,52)")
    
    print(var)
    #i = 'PCL.Del.Pcs.N'
    dff_r = df[['Terminal','Year','Week'] + [var]].query("`Week` not in (47,48,49,50,51,52)")
    dff_r.columns = ['Terminal','Year','Week']+[var]
    dff = df[['Terminal','Year','Week'] + [var]].query("`Week` in (47,48,49,50,51,52)")
    dff.columns = ['Terminal','Year','Week']+[var]
    dff_groupby = pd.DataFrame(dff.groupby(['Year','Terminal'])[var].sum()).reset_index()
    dff_groupby.columns = ['Year','Terminal','Total']
    dff = pd.merge(dff,dff_groupby[['Year','Terminal','Total']])
    
    dis = dis[['Year','Terminal','Week'] + [var]]
    dis_groupby = dis.groupby(['Year','Terminal'])[var].sum().reset_index()
    dis = pd.merge(dis, dis_groupby,on=['Year','Terminal'])
    dis['dis'] = dis[var+"_x"]/dis[var+"_y"]
    dis.columns =['Year', 'Terminal','Week']+[var]+['Total', 'dis']
    
    dfg = pd.merge(dff, dis[['Year','Week','Terminal','dis']],on=['Year','Week','Terminal'])
    dfg['New_value'] = dfg['dis']*dfg['Total']
    #df_final = pd.merge(dfg,dis[['Year','Week', 'Terminal']+[var]],on=['Year','Week', 'Terminal'])
    #df_final = pd.concat([df_final,dff_r],axis=0)
    df_final = dfg.sort_values(by=['Terminal','Week','Year'])
    
    #df_final.loc[df_final['New_value'].isnull(),'New_value'] = df_final.loc[df_final['New_value'].isnull(),var]
    df_NEW = pd.merge(df_NEW,df_final[['Terminal', 'Year', 'Week', 'New_value']],on=['Terminal', 'Year', 'Week'])  
    df_NEW = df_NEW.drop(var,axis=1)
    df_NEW = df_NEW.rename(columns={'New_value':var+'_EDITED'})


df_output = df_NEW[['Division', 'District', 'Terminal', 'Terminal.Name', 'Province', 'Year','Quarter', 'Period.Number', 'Week',
                    'PCL.Del.Pcs.N_EDITED','PCL.Del.Stops.N_EDITED','PCL.PU.Pcs.N', 'PCL.PU.Stops.N', 'Agent.Del.Pcs.N_EDITED',
                    'Agent.PU.Pcs.N','Total.Del.Stops.N_EDITED', 'Total.PU.Stops.N']]
df_output.to_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_edited_usingPython.xlsx')

#df.to_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_modified.xlsx')
