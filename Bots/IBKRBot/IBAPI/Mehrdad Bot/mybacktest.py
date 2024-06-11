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
for lower_tf, higher_tf in higher_time_frame.items():
    lower_tf_df = df[df['Time Frame'] == lower_tf]
    higher_tf_df = df[df['Time Frame'] == higher_tf][['Date', 'Ticker', 'Tunnel_EMA_Low']]
    
    merged_df = pd.merge_asof(lower_tf_df.sort_values('Date'), 
                              higher_tf_df.sort_values('Date'), 
                              on='Date', 
                              by='Ticker', 
                              direction='backward', 
                              suffixes=('', '_higher'))
    
    df.loc[merged_df.index, 'target'] = merged_df['Tunnel_EMA_Low_higher']

# Save the updated DataFrame to a new CSV file
output_file_path = 'stocks_historical_data_with_targets.csv'
df.to_csv(output_file_path, index=False)

# Display the first few rows of the updated DataFrame to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Updated DataFrame with Targets", dataframe=df)
df.head()
Th