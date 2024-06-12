import pandas as pd 


df = pd.read_csv(r"stocks_historical_data.csv")


# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Define the higher time frame dictionary
higher_time_frame = {
    '5 mins': '15 mins',
    '15 mins': '1 hour',
    '1 hour': '4 hours',
    '4 hours': '1 day',
    '1 day': '1 week',
    '1 week': '1 month'
}

# Initialize the target column with NaN values
df['target'] = float('nan')

# Iterate over each time frame and calculate the target values
db = pd.DataFrame()
for ticker in set(df['Ticker']):
        
    for lower_tf, higher_tf in higher_time_frame.items():
        lower_tf_df = df[(df['Time Frame'] == lower_tf)&(df['Ticker']==ticker)]
        higher_tf_df = df[(df['Time Frame'] == higher_tf)&(df['Ticker']==ticker)][['Date', 'Ticker', 'Tunnel_EMA_Low']].rename(columns={'Tunnel_EMA_Low':'target'})
        
        merged_df = pd.merge_asof(lower_tf_df.sort_values('Date'), 
                                higher_tf_df.sort_values('Date'), 
                                on='Date', 
                                by='Ticker', 
                                direction='backward', 
                                suffixes=('', '_higher'))
        
        buying_condition = (merged_df['Close'] > merged_df['EMA_12_Filter']) &\
                    (merged_df['EMA_12_Filter'] > merged_df['Wave_EMA_Low']) &\
                    (merged_df['EMA_12_Filter'] > merged_df['Tunnel_EMA_High']) &\
                    (merged_df['Close'] < merged_df['target_higher']*0.99)
        
        merged_df['Signal']=""
        merged_df.loc[buying_condition,'Signal'] = "Buy"


        selling_condition = merged_df['High']>=merged_df['target_higher']
        merged_df.loc[selling_condition,'Signal_sell'] = "Sell"


        #df.loc[merged_df.index, 'target'] = merged_df['Tunnel_EMA_Low_higher']
        db = pd.concat([db,merged_df])






# Save the updated DataFrame to a new CSV file
output_file_path = 'stocks_historical_data_with_targets_sell.xlsx'
db.to_excel(output_file_path)

