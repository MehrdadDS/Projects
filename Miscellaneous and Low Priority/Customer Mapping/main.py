import pandas as pd

vt = pd.read_csv(r'Input/VT.csv').iloc[1:,:]
vt["Expected Delivery Date"] = pd.to_datetime(vt['Expected Delivery Date'])
test = pd.read_csv(r'Input/Customer_mapping_data.csv').rename(columns=lambda x: "Test Dashboard - " + x).iloc[1:,:]
test['Test Dashboard - Expected Delivery Date'] = pd.to_datetime(test['Test Dashboard - Expected Delivery Date'] )
customer_names = pd.read_excel(r'C:\My Folder\Github\Miscellaneous and Low Priority\Master Clinet New Name\new MC names.xlsx')



vt = vt.merge(customer_names,left_on=vt['Master ClientID'].str.lower(),right_on=customer_names['Legacy_MasterClientId'].str.lower(),how='left').dropna()
vt['MasterClientId']    = vt['MasterClientId'].astype(str)
test['Test Dashboard - Master ClientID']  = test['Test Dashboard - Master ClientID'].astype(str)


vt = vt.merge(test[['Test Dashboard - Expected Delivery Date','Test Dashboard - Master ClientID','Test Dashboard - Pieces']],
              left_on = ['Expected Delivery Date','MasterClientId'],right_on= ['Test Dashboard - Expected Delivery Date','Test Dashboard - Master ClientID'],
              how='left')
