
import pandas as pd
import numpy as np


# Load the data
data = pd.read_excel('Amazon Report var by terminals.xlsx',sheet_name='Sheet1')
data = data[data['Terminal Name']!="NHO"]

# Data Cleaning
data_cleaned = data[(data['Overall OTP'] != 0) & (data['Amazon Stops']!=0)]
data_cleaned = data_cleaned.sort_values(['date'])
data_cleaned['date'] = pd.to_datetime(data_cleaned['date'])
# Filter Data for Weeks 29 and 30
prime_data                  =   data_cleaned[data_cleaned['date'].isin(['2024-07-17','2024-07-18','2024-07-19'])]
before_prime_data           =   data_cleaned[data_cleaned['date']<"2024-07-17"]
# Calculate Correlation
prime_correlation           =   round(prime_data[['Amazon Stops', 'Overall OTP']].corr().iloc[0,1],2)
print(f"correlation for termianls Prime:{prime_correlation}")
before_prime_correlation    =   round(before_prime_data[['Amazon Stops', 'Overall OTP']].corr().iloc[0,1],2)
print(f"correlation for termianls before Prime:{before_prime_correlation}")


terminals_correlation   = {}
for terminal in prime_data['Terminal Name'].unique():
    df = prime_data[prime_data['Terminal Name']==terminal]
    prime_tr_correlation        = df[['Amazon Stops', 'Overall OTP']].corr().iloc[0,1]
    
    df_before_prime    = before_prime_data[before_prime_data['Terminal Name']==terminal]
    before_prime_tr_correlation = df_before_prime[['Amazon Stops', 'Overall OTP']].corr().iloc[0,1]
    
    prime_portion = round(np.mean(df['Amazon Stops'].sum()/df['Total Del Stops'].sum()),1)
    before_prime_portion = round(np.mean(df_before_prime['Amazon Stops'].sum()/df_before_prime['Total Del Stops'].sum()),1)



    terminals_correlation[terminal] = [prime_tr_correlation,before_prime_tr_correlation,prime_portion,before_prime_portion]


terminals_correlation_db = pd.DataFrame.from_dict(terminals_correlation,orient='index',columns=['Prime corrolation','Before Prime Correlation','Avg of Amazon Portion - Prime','Avg of Amazon Portion - Before Prime'])
terminals_correlation_db = terminals_correlation_db.rename_axis('Terminal Name').reset_index()
terminals_correlation_db['Change of OTP'] = terminals_correlation_db['Prime corrolation'] - terminals_correlation_db['Before Prime Correlation']

terminals_correlation_db.to_excel('terminals_correlation_db.xlsx')
#print(terminals_correlation)    
