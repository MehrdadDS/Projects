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

### For those that dont have Agent pcs but diferent PCL and Total Stops
condition_del = (df['Agent.Del.Pcs.N']==0) & (df['PCL.Del.Pcs.N']>0) & (df['PCL.Del.Stops.N'] != df['Total.Del.Stops.N'])
df.loc[ condition_del   ,'PCL.Del.Stops.N']=df.loc[ condition_del   ,'Total.Del.Stops.N']
df.columns
#
   
### For those that dont have Agent pcs but diferent PCL and Total Stops
condition_pu = (df['Agent.PU.Pcs.N']==0) & (df['PCL.PU.Pcs.N']>0) &   (df['PCL.PU.Stops.N'] != df['Total.PU.Stops.N'])
df.loc[ condition_pu   ,'PCL.PU.Stops.N']=df.loc[ condition_pu   ,'Total.PU.Stops.N']


#-----------------------------------------------------------------------------
# For special terminals with same stops
ter_del =  {
    30: 5,
    130: 5,
    191: 5,
    194: 5,
    480: 5,
    491: 5,
    490: 5,
    492: 5,
    503: 10,
    511: 7,
    523: 5,
    558: 5,
    560: 11,
}

ter_pu = {
    30: 5,
    40: 5,
    51: 5,
    101: 20,
    130: 5,
    170: 15,
    171: 5,
    191: 5,
    194: 5,
    480: 5,
    490: 5,
    491: 5,
    503: 5,
    511: 7,
    516: 10,
    518: 15,
    519: 5,
    522: 5,
    523: 5,
    557: 18,
}

for i in ter_del.keys():
    df.loc[df['Terminal']==i,'PCL.Del.Stops.N'] = df.loc[df['Terminal']==i,'Total.Del.Stops.N'] - ter_del[i]
    

for j in ter_pu : 
    df.loc[df['Terminal']==j,'PCL.PU.Stops.N'] = df.loc[df['Terminal']==j,'Total.PU.Stops.N'] - ter_pu[j]

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
df['Agent Del Stops'] =df['Total.Del.Stops.N'] - df['PCL.Del.Stops.N']
df[df['Agent Del Stops']<0]['Terminal'].unique()
df['pcs/stop_agent'] = abs( df['Agent.Del.Pcs.N']/(df['Total.Del.Stops.N']-df['PCL.Del.Stops.N'])).fillna(1)
df.loc[df['Agent Del Stops']<0,'PCL.Del.Stops.N'] = df.loc[df['Agent Del Stops']<0,'Total.Del.Stops.N'] - ((df.loc[df['Agent Del Stops']<0,'Agent.Del.Pcs.N'])/df.loc[df['Agent Del Stops']<0,'pcs/stop_agent'])
df.drop(['pcs/stop_agent','Agent Del Stops'],axis=1,inplace=True)
#df.columns
#
#df_2021.columns
df['Agent pu Stops'] =df['Total.PU.Stops.N'] - df['PCL.PU.Stops.N']
df[df['Agent pu Stops']<0]['Terminal'].unique()
df['pcs/stop_agent'] = abs( df['Agent.PU.Pcs.N']/(df['Total.PU.Stops.N']-df['PCL.PU.Stops.N'])).fillna(1)
df.loc[df['Agent pu Stops']<0,'PCL.PU.Stops.N'] = df.loc[df['Agent pu Stops']<0,'Total.PU.Stops.N'] - ((df.loc[df['Agent pu Stops']<0,'Agent.PU.Pcs.N'])/df.loc[df['Agent pu Stops']<0,'pcs/stop_agent'])
df.drop(['pcs/stop_agent','Agent pu Stops'],axis=1,inplace=True)


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
