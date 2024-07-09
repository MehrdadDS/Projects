import pandas as pd

new_names = pd.read_excel('new MC names.xlsx')

cg_edd = pd.read_csv(r'C:\My Folder\Python Projects\Customer Provided Forecast\Output\VT\CG Forecast - EDD.csv')
cg_eid = pd.read_csv(r'C:\My Folder\Python Projects\Customer Provided Forecast\Output\VT\CG Forecast - EID.csv')

cg_edd_by_customers = pd.read_csv(r'C:\My Folder\Python Projects\Customer Provided Forecast\Output\VT\CG Forecast by Customers - EDD.csv')
cg_eid_by_customers = pd.read_csv(r'C:\My Folder\Python Projects\Customer Provided Forecast\Output\VT\CG Forecast by Customers - EID.csv')



new_cg_edd = cg_edd.merge(new_names,left_on=cg_edd['ID'].str.lower(),right_on=new_names['Legacy_MasterClientId'].str.lower(),how='left')
new_cg_edd = new_cg_edd[['Terminal','MasterClientName','Date','Purolator Forecast','Customer Forecast','Level','MasterClientId']].rename(
                        columns={'MasterClientName':'Customer','MasterClientId':'ID'})
new_cg_edd['Code'] = new_cg_edd['Customer'] + "=" + new_cg_edd['ID'].astype(str)

new_cg_edd.to_csv('CG Forecast - EDD.csv',index=False)

new_cg_eid = cg_eid.merge(new_names,left_on=cg_eid['ID'].str.lower(),right_on=new_names['Legacy_MasterClientId'].str.lower(),how='left')
new_cg_eid = new_cg_eid[['Terminal','MasterClientName','Date','Purolator Forecast','Customer Forecast','Level','MasterClientId']].rename(
                        columns={'MasterClientName':'Customer','MasterClientId':'ID'})
new_cg_eid['Code'] = new_cg_eid['Customer'] + "=" + new_cg_eid['ID'].astype(str)


new_cg_eid.to_csv('CG Forecast - EID.csv',index=False)


new_cg_edd_by_customers = cg_edd_by_customers.merge(new_names,left_on=cg_edd_by_customers['ID'].str.lower(),right_on=new_names['Legacy_MasterClientId'].str.lower(),how='left')
new_cg_edd_by_customers['Code'] = new_cg_edd_by_customers['MasterClientName'] + "=" + new_cg_edd_by_customers['MasterClientId'].astype(str)
new_cg_edd_by_customers = new_cg_edd_by_customers[['MasterClientName','Date','Level','MasterClientId','Code','Purolator Forecast','Customer Forecast']].rename(
                        columns={'MasterClientName':'Customer','MasterClientId':'ID'})

new_cg_edd_by_customers.to_csv('CG Forecast by Customers - EDD.csv')

new_cg_eid_by_customers = cg_eid_by_customers.merge(new_names,left_on=cg_eid_by_customers['ID'].str.lower(),right_on=new_names['Legacy_MasterClientId'].str.lower(),how='left')
new_cg_eid_by_customers['Code'] = new_cg_eid_by_customers['MasterClientName'] + "=" + new_cg_eid_by_customers['MasterClientId'].astype(str)
new_cg_eid_by_customers = new_cg_eid_by_customers[['MasterClientName','Date','Level','MasterClientId','Code','Purolator Forecast','Customer Forecast']].rename(
                        columns={'MasterClientName':'Customer','MasterClientId':'ID'})

new_cg_eid_by_customers.to_csv('CG Forecast by Customers - EID.csv')