import pandas as pd
import plots
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.backends.backend_pdf as pdf
#import helper_functions as f

pcs_thr_reg = 10000
pcs_per_reg = 0.05

pcs_thr_reg = {'Agriculture':10000,
               'Automotive':5000,
               'Chemicals':5000,
                'Construction':5000,
                'Education':10000,
                'Entertainment':5000,
                'Finance, Insurance and Real Estate':5000,
                'Food and Beverage':5000,
                'Forestry, Wood, Pulp and Paper':5000,
                'Government':5000,
                'Health Care':10000,
                'Industrial Supply':10000,
                'Metals':5000,
                'Oil, Gas, Mining and Utilities':10000,
                'Power Generation':10000,
                'Professional Services':10000,
                'Retail':50000,
                'Technology':10000,
                'Transportation and Logistics':20000,
                'UnAssigned':5000
}

df = pd.read_excel('Input/input.xlsx')
df = df.iloc[1:,:]


# Create a PDF object
pdf_pages = pdf.PdfPages("output_plots.pdf")

yoy_pivot_by_verticals = df.pivot_table(values='Pieces',columns='Year',index='MC Verticals',aggfunc='sum').reset_index()
yoy_pivot_by_verticals['diff'] = yoy_pivot_by_verticals.iloc[:,2] - yoy_pivot_by_verticals.iloc[:,1]
yoy_pivot_by_verticals['per']  = np.round(100*((yoy_pivot_by_verticals.iloc[:,2] / yoy_pivot_by_verticals.iloc[:,1])-1),2)
yoy_pivot_by_verticals = yoy_pivot_by_verticals.sort_values('diff')

yoy_pivot_by_years = df.pivot_table(values='Pieces',columns='Year',aggfunc='sum')
yoy_pivot_by_years['diff'] = yoy_pivot_by_years.iloc[:,1] - yoy_pivot_by_years.iloc[:,0]
yoy_pivot_by_years['per']  = np.round(100*((yoy_pivot_by_years.iloc[:,1] / yoy_pivot_by_years.iloc[:,0])-1),2)
vertical_fig = plots.ploy_yoy_verticals(yoy_pivot_by_verticals,yoy_pivot_by_years, "Vertical Change")
pdf_pages.savefig(vertical_fig)


"YoY Customer Growth by Region"
yoy_pivot_verticalandCus = df.pivot_table(values='Pieces',index=['MC Verticals','Master Client'],columns='Year', aggfunc='sum').reset_index().fillna(0)
yoy_pivot_verticalandCus['diff'] = np.round(yoy_pivot_verticalandCus.iloc[:,3] - yoy_pivot_verticalandCus.iloc[:,2])
yoy_pivot_verticalandCus['per'] = np.round(( yoy_pivot_verticalandCus.iloc[:,3] / yoy_pivot_verticalandCus.iloc[:,2] -1  ) * 100)
yoy_pivot_verticalandCus['per'].replace([np.inf],100,inplace=True)
yoy_pivot_verticalandCus.head()
#condition = ((yoy_pivot_verticalandCus['per'] > pcs_per_reg) & (yoy_pivot_verticalandCus['diff'] > pcs_thr_reg)) | ((yoy_pivot_verticalandCus['per'] < -1 * pcs_per_reg) & (yoy_pivot_verticalandCus['diff'] < -1 * pcs_thr_reg))
#vertical_customer_growth = yoy_pivot_verticalandCus[condition].sort_values(by='diff')

yoy_division_piechart_dic = {i:[yoy_pivot_by_verticals.loc[yoy_pivot_by_verticals['MC Verticals']==i,'per'],yoy_pivot_by_verticals.loc[yoy_pivot_by_verticals['MC Verticals']==i,'diff']] for i in yoy_pivot_by_verticals['MC Verticals'].unique()}



for ver in set(yoy_pivot_verticalandCus['MC Verticals']):
    condition = np.abs(yoy_pivot_verticalandCus['diff'])>pcs_thr_reg[ver]
    yoy_pivot_verticalandCus = yoy_pivot_verticalandCus[condition].sort_values(by='diff')
    yoy_pivot_region_filtered = yoy_pivot_verticalandCus[yoy_pivot_verticalandCus['MC Verticals'] == ver]
    fig = plt.figure(figsize=(12, 8))
    fig = plots.plot_yoy_vertical_and_customers(yoy_pivot_region_filtered,yoy_division_piechart_dic, plot_title=ver, title_fontsize=22, tick_fontsize=19, annotation_fontsize=18)
    pdf_pages.savefig(fig)
    plt.close(fig)



# Close the PDF file
pdf_pages.close()