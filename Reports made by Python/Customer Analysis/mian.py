import pandas as pd
import numpy as np
import plots
import datetime,datetime
###
db = pd.read_excel('Input/amazon.xlsx')
division_list = ['ATLANTIC','QUEBEC' ,'GREATER TORONTO AREA', 'NORTH EASTERN ONTARIO', 'SOUTH WESTERN ONTARIO','PACIFIC', 'PRAIRIES']
output_folder = "output"

# Removing the first row and unnecessary divisions(hubs)
db = db.iloc[1:,:]
db = db[db['Dest Division'].isin(division_list)]
customers_list = set(db['Master Client'])
 

for customer in customers_list:

    df = db[db['Master Client']==customer] 
    # Create a pivot table for divisions
    yoy_pivot_by_division = df.pivot_table(values='Pieces',columns='Year',index='Dest Division',aggfunc='sum').reset_index()
    yoy_pivot_by_division['diff'] = yoy_pivot_by_division.iloc[:,2] - yoy_pivot_by_division.iloc[:,1]
    yoy_pivot_by_division['per'] = np.round(100*((yoy_pivot_by_division.iloc[:,2] / yoy_pivot_by_division.iloc[:,1])-1),2)
    yoy_pivot_by_division = yoy_pivot_by_division.sort_values('diff',ascending=True)
    ## Barplots for division
    plots.plot_diff_division_bar_chart(yoy_pivot_by_division, customer, output_folder,"YoY Division Performance" , title_font_size=16, label_font_size=14, xtick_font_size=10)


    # Create a pivot table for terminals
    yoy_pivot_by_terminal = df.pivot_table(values='Pieces',columns='Year',index='Dest Terminal',aggfunc='sum').reset_index().fillna(0)
    yoy_pivot_by_terminal['diff'] = yoy_pivot_by_terminal.iloc[:,2] - yoy_pivot_by_terminal.iloc[:,1]
    yoy_pivot_by_terminal['per'] = np.round(100*((yoy_pivot_by_terminal.iloc[:,2] / yoy_pivot_by_terminal.iloc[:,1])-1),2)
    yoy_pivot_by_terminal = yoy_pivot_by_terminal.sort_values('diff',ascending=False)
    ## Barplots for terminals
    plots.plot_diff_terminal_bar_chart(yoy_pivot_by_terminal, customer, output_folder, title="", top_positive=15, top_negative=15)


    # Create a linechart for two years of data
    yoy_customer_trend = df.groupby(['Year','Week'])['Pieces'].sum().reset_index()
    plots.plot_yearly_trend(yoy_customer_trend,customer,output_folder, xticks_size=10, graph_title="Yearly Customer Trend", x_label="Week", y_label="Pieces")