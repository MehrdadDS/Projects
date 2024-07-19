import pandas as pd

""" This one must be ran after redistribution of the volumes"""
last_week_actual            =   28
current_year                =   2024

actuals = pd.read_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\July 19\Actual.xlsx')
forecast = pd.read_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_redistributed_usingPython.xlsx')


n_weeks                     =   5
threshold                   =   n_weeks - 1
actuals                     =   actuals[actuals['Year']==current_year]
actuals['Agent Del Stops']  =   actuals['Total.Del.Stops.N'] - actuals['PCL.Del.Stops.N']
actuals['Agent PU Stops']   =   actuals['Total.PU.Stops.N'] - actuals['PCL.PU.Stops.N']



fixed_agent_del_stops = {}
fixed_agent_pu_stops  = {}


for tr in actuals['Terminal'].unique() : 
    df = actuals[actuals['Terminal']== tr ]
    df = df.iloc[-n_weeks:,:]
    #if sum(df['Agent Del Stops']==0) >= threshold : 
    #    zero_agent_del_stops[tr]=0

    calculated_mode_del = df['Agent Del Stops'].mode()[0]
    if sum(df['Agent Del Stops']==calculated_mode_del) >= threshold : 
        fixed_agent_del_stops[tr]=calculated_mode_del

    calculated_mode_pu = df['Agent PU Stops'].mode()[0]
    if sum(df['Agent Del Stops']==calculated_mode_pu) >= threshold : 
        fixed_agent_pu_stops[tr]=calculated_mode_pu     


for tr in fixed_agent_del_stops.keys():
    forecast.loc[forecast['Terminal']==tr,'PCL.Del.Stops.N_EDITED'] = forecast.loc[forecast['Terminal']==tr,'Total.Del.Stops.N_EDITED'] - fixed_agent_del_stops[tr]


for tr in fixed_agent_pu_stops.keys():
    forecast.loc[forecast['Terminal']==tr,'PCL.PU.Stops.N_EDITED'] = forecast.loc[forecast['Terminal']==tr,'Total.PU.Stops.N_EDITED'] - fixed_agent_pu_stops[tr]



forecast.to_excel(r'C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\updated_pcl_and_redistributed.xlsx')