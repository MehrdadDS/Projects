import pandas as pd


vt1 = pd.read_excel(r'VT Input\Jan-Feb.xlsx', engine='openpyxl')
vt2 = pd.read_excel(r'VT Input\Mar-Apr.xlsx', engine='openpyxl')
vt = pd.concat([vt1,vt2])
vt['AccountID'] = pd.to_numeric( vt['AccountID'], errors='coerce')
vt = vt[~vt['AccountID'].isna()]
vt.to_parquet('vt.parquet')
#customer_names = pd.read_excel('customer_names.xlsx')

# Read all sheets into a dictionary of DataFrames
all_sheets = pd.read_excel('SMB BRP to BRPP Final Migration - Q1 2024.xlsx', sheet_name=None)
# Concatenate all DataFrames
sales = pd.concat(all_sheets.values(), ignore_index=True)
sales['ACCOUNT'] = pd.to_numeric( sales['ACCOUNT'], errors='coerce')




df = vt.merge(sales[['ACCOUNT','BRPCurrentSavings','Segment_SMB']],left_on='AccountID',right_on="ACCOUNT",how='left')
volume_sales = df[~df['ACCOUNT'].isna()]

print(volume_sales.head())