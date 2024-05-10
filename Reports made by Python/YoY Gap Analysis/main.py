import pandas as pd
import numpy as np
import plots
import matplotlib.pyplot as plt
import os
import matplotlib.backends.backend_pdf as pdf



# Importing file
yoy = pd.read_excel(r'C:\My Folder\Python Projects\Reports\YoY Gap Analysis\Input\yoy_gap_analysis_input.xlsx')

yoy_gap_analysis_file = 'yoy_gap_analysis_file.pdf'

holiday_weeks = {2023:[1,8,14],#14
                 2024:[1,8,13]}

replacing_weeks = {13:14}
yoy['Week'] = yoy['Week'].replace(replacing_weeks)


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

region_list = {
                'East':['ATLANTIC','QUEBEC'],
                'Ontario': ['GREATER TORONTO AREA', 'NORTH EASTERN ONTARIO', 'SOUTH WESTERN ONTARIO'],
                'West':  ['PACIFIC', 'PRAIRIES'] 
                }

yoy = yoy.iloc[1:,:]
yoy = yoy[yoy['Dest Division'].isin(list(division_notations.keys()))]
yoy_pivot = yoy.pivot_table(values='Pieces',index=['Dest Division','Week'],columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_pivot['diff'] = np.round(yoy_pivot.iloc[:,3] - yoy_pivot.iloc[:,2])
yoy_pivot['per'] = np.round(( yoy_pivot.iloc[:,3] / yoy_pivot.iloc[:,2] -1  ) * 100)
yoy_pivot['per'].replace([np.inf],100,inplace=True)

def map_division_to_region(division):
    for region, divisions in region_list.items():
        if division in divisions:
            return region
    return 'Other'  # If division doesn't match any region

# Add a new 'Region' column based on the mapping
yoy_pivot['Region'] = yoy_pivot['Dest Division'].apply(map_division_to_region)


yoy_national  = yoy.pivot_table(values='Pieces',index=['Week'],columns='Year',aggfunc='sum').reset_index().fillna(0)
yoy_national['diff'] = np.round(yoy_national.iloc[:,2] - yoy_national.iloc[:,1])
yoy_national['per'] = np.round(( yoy_national.iloc[:,2] / yoy_national.iloc[:,1] -1  ) * 100)
yoy_national['per'].replace([np.inf],100,inplace=True)




"""PLOT"""
# Create a PDF object
pdf_pages = pdf.PdfPages(yoy_gap_analysis_file)
# Iterate over divisions and create plots
fig = plt.figure(figsize=(12, 8))
national_yoy_gap_chart = plots.create_national_line_chart(yoy_national, holiday_weeks, yoy_gap_analysis_file, title_fontsize=18, label_fontsize=14)
pdf_pages.savefig(national_yoy_gap_chart)


#regional_yoy_gap_chart = plots.create_line_charts(yoy_pivot, holiday_weeks, yoy_gap_analysis_file, title_fontsize=18, label_fontsize=14)
divisional_yoy_gap_chart = plots.create_line_charts_by_divisions(yoy_pivot, holiday_weeks,division_list, yoy_gap_analysis_file, title_fontsize=18, label_fontsize=14)
pdf_pages.savefig(divisional_yoy_gap_chart)

pdf_pages.close()
