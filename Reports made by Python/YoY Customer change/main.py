import pandas as pd
from datetime import timedelta, date
import sys
import itertools
import calendar
#import TeamsFileUploader_cg
import numpy as np
import os 
root_folder = r"C:\My Folder\Python Projects\General files"
sys.path.insert(0, root_folder)
#import functions
import yoy_data_grapper,plots
import matplotlib.pyplot as plt
import os
import matplotlib.backends.backend_pdf as pdf
#import helper_functions as f

current_year = 2024
previous_year = 2023

starting_week   = 1
ending_week     = 12

pcs_thr = 65000
pcs_per = 0.1

pcs_thr_reg = 25000
pcs_per_reg = 0.1

#removing_customers = ['Wayfair - Master Client']
removing_customers = []


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




""" Pull VT DATA and preprocess the data"""
#path=r"C:\My Folder\Python Projects\Reports\YoY Customer change\Input\yoy_data.xlsx"
#yoy = yoy_data_grapper.yoy_data_grapper(starting_week, ending_week)[1]
yoy = pd.read_excel(r"Input\yoy_data.xlsx")
#yoy= f.aggregate_excel_sheets(path)
yoy = yoy.iloc[1:,:]
yoy['Pieces'] = yoy['Pieces'].astype(int)
yoy.columns = ['Year','Master Client','Dest Division', 'Pieces']
"""Creating pivot table based on years"""
yoy_pivot_by_years =  yoy.pivot_table(values='Pieces',columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_pivot_by_years['diff'] = np.round(yoy_pivot_by_years.iloc[:,2] - yoy_pivot_by_years.iloc[:,1])
yoy_pivot_by_years['per'] = np.round(( yoy_pivot_by_years.iloc[:,2] / yoy_pivot_by_years.iloc[:,1] -1  ) * 100,1)


yoy = yoy[~yoy['Master Client'].isin(removing_customers)]
yoy = yoy[yoy['Dest Division'].isin(division_list)]
yoy = yoy[yoy['Master Client']!='-']

"""Creating pivot table based on customers"""
yoy_pivot_by_customer = yoy.pivot_table(values='Pieces',index='Master Client',columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_pivot_by_customer['diff'] = np.round(yoy_pivot_by_customer.iloc[:,2] - yoy_pivot_by_customer.iloc[:,1])
yoy_pivot_by_customer['per'] = np.round(( yoy_pivot_by_customer.iloc[:,2] / yoy_pivot_by_customer.iloc[:,1] -1  ) * 100)
yoy_pivot_by_customer['per'].replace([np.inf],100,inplace=True)
yoy.head()


"""Creating pivot table based on divisions"""
yoy_division_piechart = yoy.pivot_table(values='Pieces',index='Dest Division',columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_division_piechart['diff'] = np.round(yoy_division_piechart.iloc[:,2] - yoy_division_piechart.iloc[:,1])
yoy_division_piechart['per'] = np.round((yoy_division_piechart.iloc[:, 2] / yoy_division_piechart.iloc[:, 1] - 1) * 100, decimals=1)
yoy_division_piechart_dic = {i:[yoy_division_piechart.loc[yoy_division_piechart['Dest Division']==i,'per'],yoy_division_piechart.loc[yoy_division_piechart['Dest Division']==i,'diff']] for i in yoy_division_piechart['Dest Division'].unique()}
yoy_division_piechart['Dest Division'] = yoy_division_piechart['Dest Division'].apply(lambda x: division_notations[x] )



""" Filter on Customers meeting condition """
# Assuming yoy_pivot contains the DataFrame with the data
condition = ((yoy_pivot_by_customer['per'] > 0.5) & (yoy_pivot_by_customer['diff'] > pcs_thr)) | ((yoy_pivot_by_customer['per'] < -1 * 0.5) & (yoy_pivot_by_customer['diff'] < -1 * pcs_thr))
yoy_growth = yoy_pivot_by_customer[condition].sort_values(by='diff')
#plots.plot_yoy_growth(yoy_growth,starting_week,ending_week,plot_title="National")




"YoY Customer Growth by Region"
yoy_pivot_region = yoy.pivot_table(values='Pieces',index=['Master Client','Dest Division'],columns='Year', aggfunc='sum').reset_index().fillna(0)
yoy_pivot_region['diff'] = np.round(yoy_pivot_region.iloc[:,3] - yoy_pivot_region.iloc[:,2])
yoy_pivot_region['per'] = np.round(( yoy_pivot_region.iloc[:,3] / yoy_pivot_region.iloc[:,2] -1  ) * 100)
yoy_pivot_region['per'].replace([np.inf],100,inplace=True)
yoy_pivot_region.head()
condition = ((yoy_pivot_region['per'] > pcs_per_reg) & (yoy_pivot_region['diff'] > pcs_thr_reg)) | ((yoy_pivot_region['per'] < -1 * pcs_per_reg) & (yoy_pivot_region['diff'] < -1 * pcs_thr_reg))
region_growth = yoy_pivot_region[condition].sort_values(by='diff')

"""Creating Pie chart based on Customers"""
yoy_customer_piechart = yoy.pivot_table(values='Pieces',index='Master Client',columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_customer_piechart['diff'] = np.round(yoy_customer_piechart.iloc[:,2] - yoy_customer_piechart.iloc[:,1])
yoy_customer_piechart = yoy_customer_piechart[yoy_customer_piechart['diff']<0] 
# Assuming your data is stored in a DataFrame called 'df'
top_negative_clients = yoy_customer_piechart.nsmallest(10, 'diff')['Master Client'].tolist()
other_customers_diff = yoy_customer_piechart.loc[~yoy_customer_piechart['Master Client'].isin(top_negative_clients), 'diff'].sum()
other_customers_row = pd.DataFrame([['Other customers', other_customers_diff]], columns=['Master Client', 'diff'])

# Append 'Other customers' row to the dataframe
yoy_customer_piechart = yoy_customer_piechart.append(other_customers_row, ignore_index=True)

# Filter out rows for the top 12 negative clients
df = yoy_customer_piechart[yoy_customer_piechart['Master Client'].isin(top_negative_clients) | (yoy_customer_piechart['Master Client'] == 'Other customers')]




"""PLOTTING SECTION"""
# Assuming you have already imported the plot_yoy_growth function from plots module
# Create a PDF object
pdf_pages = pdf.PdfPages("output_plots.pdf")

# Iterate over divisions and create plots
fig = plt.figure(figsize=(12, 8))

# National bar chart
national_fig = plots.plot_yoy_growth(yoy_growth,yoy_pivot_by_years,starting_week,ending_week,plot_title="National")
pdf_pages.savefig(national_fig)

# Pie chart
pie_chart = plots.plot_pie_chart(yoy_division_piechart,name="Dest Division", title_fontsize=30, label_fontsize=30)
print(yoy_division_piechart)
pdf_pages.savefig(pie_chart)


#Customer Pie chart
customer_pie_chart = plots.plot_pie_chart(df,name="Master Client",title_fontsize=16, label_fontsize=15)
pdf_pages.savefig(customer_pie_chart)

# Divisional bar charts
for division in division_list:
    yoy_pivot_region_filtered = region_growth[region_growth['Dest Division'] == division]
    fig = plt.figure(figsize=(12, 8))
    fig = plots.plot_yoy_growth_div_trunc(yoy_pivot_region_filtered,yoy_division_piechart_dic, plot_title=division, title_fontsize=22, tick_fontsize=19, annotation_fontsize=18,max_name_length=12)
    pdf_pages.savefig(fig)
    plt.close(fig)

# Close the PDF file
pdf_pages.close()