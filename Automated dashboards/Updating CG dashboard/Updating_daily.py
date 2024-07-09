import pandas as pd
from datetime import timedelta, date
import sys
import itertools
import calendar
import TeamsFileUploader_cg
import excel

root_folder = r"C:\My Folder\Python Projects\General files"
sys.path.insert(0, root_folder)
import functions
import QVDataGrapper_VT_EidEdd


eid_path = r"C:\My Folder\Github\Automated dashboards\Updating CG dashboard\Output\CG EID actuals daily.csv"
edd_path = r"C:\My Folder\Github\Automated dashboards\Updating CG dashboard\Output\CG EDD actuals daily.csv"
pi_path  = r"C:\My Folder\Github\Automated dashboards\Updating CG dashboard\Output\PI EDD actuals.csv"

file_path = r"https://purolator.sharepoint.com/sites/OperationsForecasts774/Shared%20Documents/Control%20Group%20Customers%20Analysis/Control%20Group%20Dashboard.xlsx"


# EID PART
print('Pulling EID actuals ...')
eid = QVDataGrapper_VT_EidEdd.ControlGroupEIDDataGrapper()[1]
print("EID columns : {}",eid.columns)
eid = eid.iloc[1:,:]
eid = eid[eid['Expected Induction Date']!="-"]
eid['Expected Induction Date']  = pd.to_datetime(eid['Expected Induction Date'])
eid = eid[eid['Expected Induction Date'] >="2023-01-01"]

eid.to_csv(eid_path,index=False)
print('EID actuals data succussfully stored ----------------------------------------------------')      


# EDD PART
print('Pulling EDD actuals ...')
edd = QVDataGrapper_VT_EidEdd.ControlGroupEDDDataGrapper()[1]
#print("EDD columns : {}",edd.columns)

#edd = edd.iloc[1:,:]
#edd['Expected Delivery Date']  = pd.to_datetime(edd['Expected Delivery Date'])
#edd = edd[edd['Expected Delivery Date'] >="2023-01-01"]

edd.to_csv(edd_path,index=False)
print('EDD actuals data succussfully stored ----------------------------------------------------')


# PI PART
print('Pulling PI actuals ...')
pi = QVDataGrapper_VT_EidEdd.PIDataGrapper()[1]
print('PI actuals data succussfully stored ----------------------------------------------------')
TeamsFileUploader_cg.teamFileUpload(eid_path,edd_path,pi_path)
#TeamsFileUploader_cg.teamFileUpload(eid_path,edd_path)


excel.refresh_pivot_table(file_path)
