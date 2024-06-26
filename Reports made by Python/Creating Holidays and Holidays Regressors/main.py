import pandas as pd
import functions

df = pd.read_excel('Calendar_Holidays_2025.xlsx',sheet_name="Working Days by Week")
#df = df[df['Year']==2025]
required_columns = pd.read_excel('C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Input\ExternalVariables.xlsx')

holiday_dict = functions.create_holidays_province_weekly_dictionary(df.sort_values(by=['Year','Week Number']))
test_result = functions.test_holidays_province_weekly_dictionary(holiday_dict,start_year=2019)


external_variables_regressors = functions.create_external_variables(holiday_dict,start_year=2019)
external_variables_regressors= external_variables_regressors[external_variables_regressors['Year']==2025].rename(columns={'Cyber Week Plus 2':'Cyber+2',
                                                                                                                          'Cyber Week Plus 1':'Cyber+1',
                                                                                                                          'Cyber Week':'Cyber',
                                                                                                                          'Cyber Week Minus 1':'Cyber-1',
                                                                                                                          'Week Number':'Week number',
                                                                                                                          'St. Jean Baptiste':'St Jean Baptiste Day',
                                                                                                                          "New Year's Day":"New Years Day",
                                                                                                                          "Thanksgiving":"Thanksgiving",
                                                                                                                          'Truth and Reconciliation Day':'Truth and Reconcilliation Day'})


sorted_columns = required_columns.drop(['Year','Week number','Province'],axis=1)
external_variables_regressors= external_variables_regressors[['Year','Week number','Province']+ list(sorted_columns.columns)]
external_variables_regressors.to_csv('External Variables.csv',index=False)

