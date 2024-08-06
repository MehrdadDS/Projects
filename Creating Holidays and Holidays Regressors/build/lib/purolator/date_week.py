import pandas as pd


df = pd.read_excel(r'Calendar_Holidays_2025.xlsx')
print(df.head(10))

date_week_db = df[['CalendarDate','Year','Week Number']].rename(columns={'CalendarDate':'Date','Week Number':'Week'}).drop_duplicates()