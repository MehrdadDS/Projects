import pandas as pd
import numpy as np


weekly_forecast_db = pd.read_excel("C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\ForecastResults_onesheet_edited_usingPython.xlsx")
adjustments = pd.read_excel("C:\My Folder\P&D Forecast\Steps\Files\Adjustments.xlsx")
weekly_forecast = weekly_forecast_db.copy(deep=True)

print(weekly_forecast.head())

weekly_forecast.columns = [i.replace("_EDITED","") for i in weekly_forecast.columns ]

global_adjustment = 1

for Tr in set(weekly_forecast['Terminal']):
    pcs_adjustment   = np.array( 1 + (global_adjustment * adjustments.loc[adjustments['Terminal']==Tr,"Del Pcs Adj"])   )
    stops_adjustment = np.array( 1 + (global_adjustment * adjustments.loc[adjustments['Terminal']==Tr,"Del Stops Adj"]) )

    condition = (weekly_forecast['Terminal'] == Tr) & (weekly_forecast['Year'] == 2024)


    # Pcs Adjustments
    weekly_forecast.loc[condition, "PCL.Del.Pcs.N"] = pcs_adjustment * weekly_forecast.loc[condition, "PCL.Del.Pcs.N"]
    weekly_forecast.loc[condition, "Agent.Del.Pcs.N"] = pcs_adjustment * weekly_forecast.loc[condition, "Agent.Del.Pcs.N"]

    # Stops Adjustments
    weekly_forecast.loc[condition, "PCL.Del.Stops.N"] = stops_adjustment * weekly_forecast.loc[condition, "PCL.Del.Stops.N"]
    weekly_forecast.loc[condition, "Total.Del.Stops.N"] = stops_adjustment * weekly_forecast.loc[condition, "Total.Del.Stops.N"]

weekly_forecast.to_excel("C:\My Folder\P&D Forecast\P&D Forecast v2\Excel Output\Weekly Forecast Result using Trend Adjustment tool.xlsx")