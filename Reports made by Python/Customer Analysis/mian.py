import pandas as pd
import numpy as np
import plots
import datetime,datetime
####
db = pd.read_excel('Input/jiayou.xlsx')
ter_type = pd.read_excel('Input/Terminal Type.xlsx')

division_list = ['ATLANTIC','QUEBEC' ,'GREATER TORONTO AREA', 'NORTH EASTERN ONTARIO', 'SOUTH WESTERN ONTARIO','PACIFIC', 'PRAIRIES']
output_folder = "output"

# Removing the first row and unnecessary divisions(hubs)
db = db.iloc[1:,:]
db = db[db['Dest Division'].isin(division_list)]
customers_list = set(db['Master Client'])
 

for customer in customers_list:

    df = db[db['Master Client']==customer]
    print(customer)
    # Create a pivot table for divisions
    yoy_pivot_by_division = df.pivot_table(values='Pieces',columns='Year',index='Dest Division',aggfunc='sum').reset_index().fillna(0)
    try:
        yoy_pivot_by_division['diff'] = yoy_pivot_by_division.iloc[:, 2] - yoy_pivot_by_division.iloc[:, 1]
    except IndexError:
        yoy_pivot_by_division.insert(1,column=2023,value=0)
        yoy_pivot_by_division['diff'] = yoy_pivot_by_division.iloc[:, 2] - yoy_pivot_by_division.iloc[:, 1]    
    yoy_pivot_by_division['per'] = np.round(100*((yoy_pivot_by_division.iloc[:,2] / yoy_pivot_by_division.iloc[:,1])-1),2)
    yoy_pivot_by_division['per'].replace([np.inf],100,inplace=True)
    yoy_pivot_by_division = yoy_pivot_by_division.sort_values('diff',ascending=True)
    ## Barplots for division
    plots.plot_diff_division_bar_chart(yoy_pivot_by_division, customer, output_folder,"YoY YTD Division Performance" , title_font_size=16, label_font_size=15, xtick_font_size=13)


    # Create a pivot table for terminals
    yoy_pivot_by_terminal = df.pivot_table(values='Pieces',columns='Year',index='Dest Terminal',aggfunc='sum').reset_index().fillna(0)
    if 2023 not in yoy_pivot_by_terminal.columns: yoy_pivot_by_terminal.insert(1,column=2023,value=0)
    yoy_pivot_by_terminal['diff'] = yoy_pivot_by_terminal.iloc[:,2] - yoy_pivot_by_terminal.iloc[:,1]
    yoy_pivot_by_terminal['per'] = np.round(100*((yoy_pivot_by_terminal.iloc[:,2] / yoy_pivot_by_terminal.iloc[:,1])-1),2)
    yoy_pivot_by_terminal['per'].replace([np.inf],100,inplace=True)
    yoy_pivot_by_terminal.to_csv(f'yoy_pivot_by_terminal-{customer}.csv')
    yoy_pivot_by_terminal = yoy_pivot_by_terminal.sort_values('diff',ascending=False)
    ## Barplots for terminals
    plots.plot_diff_terminal_bar_chart(yoy_pivot_by_terminal, customer, output_folder, title="", top_positive=15, top_negative=15)


    # Create a linechart for two years of data
    yoy_customer_trend = df.groupby(['Year','Week'])['Pieces'].sum().reset_index()
    plots.plot_yearly_trend(yoy_customer_trend,customer,output_folder, xticks_size=10, graph_title="Weekly Volume", x_label="Week", y_label="Pieces")

    yoy_ter_type = pd.merge(df,ter_type[['Dest Terminal','Terminal Type']],how='left',on='Dest Terminal')
    yoy_ter_type = yoy_ter_type.pivot_table(values='Pieces',columns='Year',index='Terminal Type',aggfunc='sum').reset_index().fillna(0)
    if 2023 not in yoy_ter_type.columns: yoy_ter_type.insert(1,column=2023,value=0)
    
    yoy_ter_type['diff'] = yoy_ter_type.iloc[:,2] - yoy_ter_type.iloc[:,1]
    yoy_ter_type['per'] = np.round(100*((yoy_ter_type.iloc[:,2] / yoy_ter_type.iloc[:,1])-1),2)
    yoy_ter_type['per'].replace([np.inf],100,inplace=True)
    #yoy_ter_type = yoy_ter_type.sort_values('diff',ascending=True)
    plots.plot_diff_terminal_type_bar_chart(yoy_ter_type, customer, output_folder,"YoY YTD Terminal Types Performance Comparison" , title_font_size=28, label_font_size=30, xtick_font_size=40)
