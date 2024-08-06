import pandas as pd
import datetime
import numpy as np

# Load data
forecast = pd.read_csv(r'Input/forecast.csv', parse_dates=True)
actual = pd.read_csv(r'Input/courierops_actuals - daily.csv')
terminals = pd.read_csv(r'Input/terminals.csv')

# Define date range and threshold
starting_date = datetime.datetime(2024, 7, 21)
ending_date = starting_date + datetime.timedelta(days=6)
number_working_days = 5
thd = 0.151

# Parse dates
forecast['CalendarDate'] = pd.DatetimeIndex(forecast['CalendarDate'])
actual['CalendarDate'] = pd.DatetimeIndex(actual['CalendarDate'])

# Filter data by date range
forecast = forecast[(forecast['CalendarDate'] >= starting_date) & (forecast['CalendarDate'] <= ending_date)]
actual = actual[(actual['CalendarDate'] >= starting_date) & (actual['CalendarDate'] <= ending_date)]

# Calculate total delivery stops
actual_stops = actual[["Terminal", "Total Del Stops"]].groupby('Terminal')['Total Del Stops'].sum().reset_index()
forecast_stops = forecast[["Terminal", "Forecast-Total Del Stops"]].groupby('Terminal')['Forecast-Total Del Stops'].sum().reset_index()
df_stops = forecast_stops.merge(actual_stops, on='Terminal', how='left')
df_stops['TDS Error'] = df_stops['Total Del Stops'] / df_stops['Forecast-Total Del Stops'] - 1
df_stops = df_stops.merge(terminals[['Terminal', 'Terminal Name', 'Terminal Type']], on='Terminal', how='left')

# Print stops data
print('Stops ------------------------------------------------------------------------------------------------')
stops_above_A = list(df_stops[(df_stops['Terminal Type'] == 'A') & (df_stops['TDS Error'] > thd)]['Terminal Name'])
stops_above_B = list(df_stops[(df_stops['Terminal Type'] == 'B') & (df_stops['TDS Error'] > thd)]['Terminal Name'])
stops_above_C = list(df_stops[(df_stops['Terminal Type'] == 'C') & (df_stops['TDS Error'] > thd)]['Terminal Name'])

df_stops_tt = df_stops.groupby('Terminal Type')[['Forecast-Total Del Stops', 'Total Del Stops']].sum().reset_index()
df_stops_tt['TDS Error'] = round((df_stops_tt['Total Del Stops'] / df_stops_tt['Forecast-Total Del Stops'] - 1) * 100, 1)
df_stops_tt['TDS Error'] = df_stops_tt['TDS Error'].apply(lambda x: f"+{x}%" if x > 0 else f"{x}%")
df_stops_tt['Avg.Delta'] = round((df_stops_tt['Total Del Stops'] - df_stops_tt['Forecast-Total Del Stops']) / (1000 * number_working_days), 1)
df_stops_tt['Avg.Delta'] = df_stops_tt['Avg.Delta'].apply(lambda x: f"+{x}K" if x > 0 else f"{x}K")

print(df_stops_tt)

stops_below_A = list(df_stops[(df_stops['Terminal Type'] == 'A') & (df_stops['TDS Error'] < -1 * thd)]['Terminal Name'])
stops_below_B = list(df_stops[(df_stops['Terminal Type'] == 'B') & (df_stops['TDS Error'] < -1 * thd)]['Terminal Name'])
stops_below_C = list(df_stops[(df_stops['Terminal Type'] == 'C') & (df_stops['TDS Error'] < -1 * thd)]['Terminal Name'])

# Replace empty lists with 'None'
stops_above_A = stops_above_A if stops_above_A else ['None']
stops_below_A = stops_below_A if stops_below_A else ['None']
stops_above_B = stops_above_B if stops_above_B else ['None']
stops_below_B = stops_below_B if stops_below_B else ['None']
stops_above_C = stops_above_C if stops_above_C else ['None']
stops_below_C = stops_below_C if stops_below_C else ['None']

print('above A terminals: ' + ', '.join(stops_above_A))
print('below A terminals: ' + ', '.join(stops_below_A))
print('-' * 5)
print('above B terminals: ' + ', '.join(stops_above_B))
print('below B terminals: ' + ', '.join(stops_below_B))
print('-' * 5)
print('above C terminals: ' + ', '.join(stops_above_C))
print('below C terminals: ' + ', '.join(stops_below_C))

# Calculate total delivery pieces
actual_pcs = actual[["Terminal", "Total Del Pcs"]].groupby('Terminal')['Total Del Pcs'].sum().reset_index()
forecast_pcs = forecast[["Terminal", "Forecast-Total Del Pcs"]].groupby('Terminal')['Forecast-Total Del Pcs'].sum().reset_index()
df_pcs = forecast_pcs.merge(actual_pcs, on='Terminal', how='left')
df_pcs['TDS Error'] = df_pcs['Total Del Pcs'] / df_pcs['Forecast-Total Del Pcs'] - 1
df_pcs = df_pcs.merge(terminals[['Terminal', 'Terminal Name', 'Terminal Type']], on='Terminal', how='left')

print('PCS --------------------------------------------------------------------------------------------------')
pcs_above_A = list(df_pcs[(df_pcs['Terminal Type'] == 'A') & (df_pcs['TDS Error'] > thd)]['Terminal Name'])
pcs_above_B = list(df_pcs[(df_pcs['Terminal Type'] == 'B') & (df_pcs['TDS Error'] > thd)]['Terminal Name'])
pcs_above_C = list(df_pcs[(df_pcs['Terminal Type'] == 'C') & (df_pcs['TDS Error'] > thd)]['Terminal Name'])

df_pcs_tt = df_pcs.groupby('Terminal Type')[['Forecast-Total Del Pcs', 'Total Del Pcs']].sum().reset_index()
df_pcs_tt['TDS Error'] = round((df_pcs_tt['Total Del Pcs'] / df_pcs_tt['Forecast-Total Del Pcs'] - 1) * 100, 1)
df_pcs_tt['TDS Error'] = df_pcs_tt['TDS Error'].apply(lambda x: f"+{x}%" if x > 0 else f"{x}%")
df_pcs_tt['Avg.Delta'] = round((df_pcs_tt['Total Del Pcs'] - df_pcs_tt['Forecast-Total Del Pcs']) / (1000 * number_working_days), 1)
df_pcs_tt['Avg.Delta'] = df_pcs_tt['Avg.Delta'].apply(lambda x: f"+{x}K" if x > 0 else f"{x}K")

print(df_pcs_tt)

pcs_below_A = list(df_pcs[(df_pcs['Terminal Type'] == 'A') & (df_pcs['TDS Error'] < -1 * thd)]['Terminal Name'])
pcs_below_B = list(df_pcs[(df_pcs['Terminal Type'] == 'B') & (df_pcs['TDS Error'] < -1 * thd)]['Terminal Name'])
pcs_below_C = list(df_pcs[(df_pcs['Terminal Type'] == 'C') & (df_pcs['TDS Error'] < -1 * thd)]['Terminal Name'])

# Replace empty lists with 'None'
pcs_above_A = pcs_above_A if pcs_above_A else ['None']
pcs_below_A = pcs_below_A if pcs_below_A else ['None']
pcs_above_B = pcs_above_B if pcs_above_B else ['None']
pcs_below_B = pcs_below_B if pcs_below_B else ['None']
pcs_above_C = pcs_above_C if pcs_above_C else ['None']
pcs_below_C = pcs_below_C if pcs_below_C else ['None']

print('above A terminals: ' + ', '.join(pcs_above_A))
print('below A terminals: ' + ', '.join(pcs_below_A))
print('-' * 5)
print('above B terminals: ' + ', '.join(pcs_above_B))
print('below B terminals: ' + ', '.join(pcs_below_B))
print('-' * 5)
print('above C terminals: ' + ', '.join(pcs_above_C))
print('below C terminals: ' + ', '.join(pcs_below_C))
