import pandas as pd
import numpy as np
import plots
yoy = pd.read_excel(r'C:\My Folder\Python Projects\Reports\Amazon Analysis\Input\pitney_yoy.xlsx')
output_folder = r'C:\My Folder\Python Projects\Reports\Amazon Analysis'
customer_name="Pitney Bows"
division_list = ['ATLANTIC','QUEBEC' ,'GREATER TORONTO AREA', 'NORTH EASTERN ONTARIO', 'SOUTH WESTERN ONTARIO','PACIFIC', 'PRAIRIES']

division_notations= {
                    'ATLANTIC':"ATL",
                    'QUEBEC':"QBC" ,
                    'GREATER TORONTO AREA':"GTA",
                    'NORTH EASTERN ONTARIO':"NEO",
                    'SOUTH WESTERN ONTARIO':"SWO",
                    'PACIFIC':"PAC",
                    'PRAIRIES':"PRA"
                    }

#yoy = yoy[yoy['Dest Division']=='GREATER TORONTO AREA']
yoy_pivot = yoy.pivot_table(values='Pieces',index=['Week','Low Dens','Dest Division','Dest Terminal','Mode of Transport'] ,columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_pivot['diff'] = np.round(yoy_pivot.iloc[:,6] - yoy_pivot.iloc[:,5])

#YoY National
yoy_pivot_national = yoy.pivot_table(values='Pieces',columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_pivot_national['diff'] = yoy_pivot_national.iloc[:,2] - yoy_pivot_national.iloc[:,1]
yoy_pivot_national['per'] = np.round(((yoy_pivot_national.iloc[:,2] / yoy_pivot_national.iloc[:,1]) - 1)*100,1)


# YOY Division
yoy_pivot_by_destination_division = yoy_pivot.groupby(['Dest Division'])[[2023,2024]+['diff']].sum().reset_index()
yoy_pivot_by_destination_division['per'] = np.round(((yoy_pivot_by_destination_division.iloc[:,2] / yoy_pivot_by_destination_division.iloc[:,1]) - 1)*100,1)
yoy_pivot_by_destination_division = yoy_pivot_by_destination_division[yoy_pivot_by_destination_division['Dest Division'].isin(division_list)]

# YOY Division
yoy_pivot_by_destination_termianl = yoy_pivot.groupby(['Dest Division','Dest Terminal'])[[2023,2024]+['diff']].sum().reset_index()
yoy_pivot_by_destination_termianl['per'] = np.round(((yoy_pivot_by_destination_termianl.iloc[:,3] / yoy_pivot_by_destination_termianl.iloc[:,2]) - 1)*100,1)
yoy_pivot_by_destination_termianl = yoy_pivot_by_destination_termianl.sort_values(by=['diff'])

#YOY WEEKLY TREND
yoy_weekly_trend = yoy.groupby(['Year','Week'])['Pieces'].sum().reset_index().fillna(0)
plots.plot_yoy_weekly_trend(yoy_weekly_trend, output_folder, customer_name,)


plots.plot_top_dest_terminals(yoy_pivot_by_destination_termianl, output_folder, customer_name, title_fontsize=16, label_fontsize=15, terminal_fontsize=15)
#plots.plot_top_dest_divisions(yoy_pivot_by_destination_division, output_folder, customer_name, title_fontsize=16, label_fontsize=20, terminal_fontsize=12)
plots.draw_diff_chart(yoy_pivot_by_destination_division, output_folder, customer_name,title='', title_fontsize=14)