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
#df_2021 = pd.read_excel('C:\Forecast tools\P&D Forecast\P&D Forecast v2\Excel Output\Actual.xlsx')
#df = df[df_2021['Year']==2021]

df.columns = ['Division', 'District', 'Terminal', 'Terminal.Name', 'Province', 'Year','Quarter', 'Period.Number', 'Week', 'PCL.Del.Pcs.N','PCL.Del.Stops.N', 'PCL.PU.Pcs.N', 'PCL.PU.Stops.N', 'Agent.Del.Pcs.N',
       'Agent.PU.Pcs.N', 'Total.Del.Stops.N', 'Total.PU.Stops.N']


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#Changing distribution
diss = pd.read_excel('C:\My Folder\P&D Forecast\Steps\Files\Changing Distribution.xlsx',sheet_name="dis")
col_adj = {'PCL.Del.Pcs.N':'PCL Pcs','PCL.Del.Stops.N':'Stops','Agent.Del.Pcs.N':'Agent Pcs','Total.Del.Stops.N':'Stops'}


df_NEW = df
for i in col_adj.keys():
    
    dis =  diss.query("Week in (47,48,49,50,51,52)")
    
    print(i)
    #i = 'PCL.Del.Pcs.N'
    dff_r = df[['Terminal','Year','Week'] + [i]].query("`Week` not in (47,48,49,50,51,52)")
    dff_r.columns = ['Terminal','Year','Week']+[i]
    dff = df[['Terminal','Year','Week'] + [i]].query("`Week` in (47,48,49,50,51,52)")
    dff.columns = ['Terminal','Year','Week']+[i]
    dff_groupby = pd.DataFrame(dff.groupby(['Year','Terminal'])[i].sum()).reset_index()
    dff_groupby.columns = ['Year','Terminal','Total']
    dff = pd.merge(dff,dff_groupby[['Year','Terminal','Total']])
    
    dis_groupby = pd.DataFrame(dis[dis['Type']==col_adj[i]].groupby(['Year','Terminal','Type'])['Value'].sum()).reset_index()
    dis_groupby.columns = ['Year','Terminal','Type','Total']
    dis = pd.merge(dis, dis_groupby,on=['Year','Terminal','Type'])
    dis['dis'] = dis['Value']/dis['Total']
    dis2 = dis.copy()
    dis2.columns =['Year', 'Week', 'Terminal', 'Type', 'Value1', 'Total', 'dis']
    
    dfg = pd.merge(dff, dis[['Week','Terminal','Type','dis']],on=['Week','Terminal'])
    dfg['New_value'] = dfg['dis']*dfg['Total']
    df_final = pd.merge(dfg,dis2[['Week', 'Terminal', 'Type', 'Value1']],on=['Week', 'Terminal', 'Type'])
    df_final = pd.concat([df_final,dff_r],axis=0)
    df_final = df_final.sort_values(by=['Terminal','Week','Year'])
    
    df_final.loc[df_final['New_value'].isnull(),'New_value'] = df_final.loc[df_final['New_value'].isnull(),i]
    df_NEW = pd.merge(df_NEW,df_final[['Terminal', 'Year', 'Week', 'New_value']],on=['Terminal', 'Year', 'Week'])  
    names = list(df_NEW.columns)
    names.pop()
    names.append(i+'_EDITED')
    df_NEW.columns = names

df_output = df_NEW[['Division', 'District', 'Terminal', 'Terminal.Name', 'Province', 'Year','Quarter', 'Period.Number', 'Week', 'PCL.Del.Pcs.N_EDITED',
                  'PCL.Del.Stops.N_EDITED','PCL.PU.Pcs.N', 'PCL.PU.Stops.N', 'Agent.Del.Pcs.N_EDITED', 'Agent.PU.Pcs.N',
       'Total.Del.Stops.N_EDITED', 'Total.PU.Stops.N']]
df_output.to_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_edited_usingPython.xlsx')

#df.to_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_modified.xlsx')
