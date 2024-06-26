import pandas as pd
import numpy as np


number_wdays1 = 19
number_wdays2 = 20

p1 = pd.read_excel(r'Input\p1_including_returns.xlsx')
p1 = p1.iloc[1:,:]
p2 = pd.read_excel(r'Input\p2_including_returns.xlsx')
p2 = p2.iloc[1:,:]


p1['Period'] = "P1"
p2['Period'] = "P2"

data = pd.concat([p1,p2])

data['n_wdays'] = np.where(data['Period'] == 'P1',number_wdays1,number_wdays2)
data['daily_avg'] = round(data['Pieces']/data['n_wdays'],2)
data['Master Client'] = data['Master Client'].fillna('NA customers')



period_pivot = data.pivot_table(values='daily_avg',index=['Master Client','Dest Division'],columns='Period', aggfunc='sum').reset_index().fillna(0)
period_pivot['diff'] = np.round(period_pivot.iloc[:,3] - period_pivot.iloc[:,2])


print('done!')
period_pivot.to_csv(r'Output\JunevsMay_including_return.csv',index=False)