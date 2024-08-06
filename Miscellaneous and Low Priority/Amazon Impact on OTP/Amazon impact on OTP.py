import pandas as pd

df = pd.read_excel('Amazon Report var by terminals.xlsx',sheet_name='Sheet1')
df_w0 = df[df['Overall OTP']!=0]

df_before_prime = df_w0[df_w0['week']<29]
df_prime = df_w0[df_w0['week']>=29]



for tr in df_w0['Terminal Name'].unique():
    df_w0_tr = df_w0[df_w0['Terminal Name']==tr]
    Total_corr_value = df_w0_tr.corr()['Overall OTP']['Amazon Stops']


    df_before_prime_tr = df_before_prime[df_before_prime['Terminal Name']==tr]
    before_prime_corr_value = df_before_prime_tr.corr()['Overall OTP']['Amazon Stops']

    df_prime_tr = df_prime[df_prime['Terminal Name']==tr]
    prime_corr_value = df_prime_tr.corr()['Overall OTP']['Amazon Stops']

df_w0.corr()['Overall OTP']
print(df.head())