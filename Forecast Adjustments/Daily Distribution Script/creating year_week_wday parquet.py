import pandas as pd

df = pd.read_excel("C:\My Folder\Forecasts\Holidays_2025.xlsx",sheet_name="Holidays by Day")

DailyHolidayData_source = pd.read_parquet('C:\My Folder\Python Projects\General files\DailyHolidayData.parquet')
DailyHolidayData_source = df[['CalendarDate','Year','Week Number']].rename(columns={'CalendarDate':'Date','Week Number':'Week'})
DailyHolidayData_source  = DailyHolidayData_source.drop_duplicates()
DailyHolidayData_source.to_parquet('DailyHolidayData.parquet')

DailyHolidayData_source = pd.read_parquet('C:\My Folder\Python Projects\General files\DailyHolidayData.parquet')

df = pd.read_excel("C:\My Folder\Forecasts\Holidays_2025.xlsx",sheet_name="Working Days by Week")
HolidayData = pd.read_parquet('C:\My Folder\Python Projects\General files\HolidayData.parquet')
HolidayData = df.to_parquet('HolidayData.parquet')