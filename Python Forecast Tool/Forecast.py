# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:47:24 2023

@author: Mehrdad.Dadgar
"""

import pandas as pd
import os


import functions

# ----------- Import datasets --------------------------------------------------------------------- 
dir_folder = "C:/Forecast tools/Python Projects/New Model/"

start= "01-01-2021"
finish = "01-21-2023"
horizon = 52-functions.returning_weeknumber(finish)[1]  


# Load datasets
CustomerData = pd.read_parquet("Freight_input.parquet")


""" Normalizing data """
df_weekly_normalized , df_weekly = functions.preprocessing_data(CustomerData, 
                                    start=start, finish = finish)


terminal_list = sorted(df_weekly.Terminal.unique())

# --------------------------------------------------------------------------------
forecast_result = pd.DataFrame()

for terminal in terminal_list :
    
    terminal_data = functions.slicing_customer_terminal(df_weekly_normalized,customer=None,terminal=terminal)
    customer_list = terminal_data.Customer.unique()
    for customer in customer_list :
        
        
        print(terminal,customer)
        dataset = functions.slicing_customer_terminal(df_weekly_normalized,customer=customer,terminal=terminal)
        
        
        
        """ Forecast Part """
        values = dataset[['Pieces']]
        values_without_missing_data = functions.filling_missing_values(values,start,finish)

        
        forecasts = functions.stepwise_forecast_model(values_without_missing_data,horizon)
        #forecasts = functions.combination_stepwise_STLF(values_without_missing_data,horizon)
        
        
        
        
        # appending actuals and forecast
        output = functions.appending_actuals_forecast(dataset, forecasts,customer=customer,terminal=terminal,finish=finish)
        output = functions.graph_checkings(output)
        output = functions.denormalize_data(output)
        functions.plot_weekly_yoy(output)
        
        
        # Save forecast results
        forecast_result = forecast_result.append(output)    
            
            


forecast_result.to_parquet('Forecast Result.parquet')









