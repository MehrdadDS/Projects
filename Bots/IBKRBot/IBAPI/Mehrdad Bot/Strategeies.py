import pandas as pd
import numpy as np


higher_time_frame = {'15 mins':'1 hour',
                     '1 hour':'4 hours',
                     '4 hours':'1 day',
                     '1 day':'1 week'}


def wavy_tunnel_conservative_strategy(df,time_frame,higher_time_frame):
    """
    Checks if the latest closing price is above the specified EMA filters
    and returns True if all conditions are met.

    Args:
    df (pd.DataFrame): DataFrame containing stock data with columns 'Close',
                       'EMA_12_Filter', 'Wave_EMA_High', and 'Tunnel_EMA_High'.

    Returns:
    bool: True if the latest closing price is above all the specified EMA filters,
          False otherwise.
    """
    db = df.copy(deep=True)
    trade_trigger = 'No'

    df = df[df["Time Frame"]==time_frame]
    latest_close = df["Close"].iloc[-1]
    ema_12_filter = df["EMA_12_Filter"].iloc[-1]
    wave_ema_high = df["Wave_EMA_High"].iloc[-1]
    wave_ema_low = df["Wave_EMA_Low"].iloc[-1]
    tunnel_ema_high = df["Tunnel_EMA_High"].iloc[-1]
    tunnel_ema_low = df["Tunnel_EMA_Low"].iloc[-1]

    target = db[db['Time Frame']==target_time_frame]["Tunnel_EMA_Low"].iloc[-1]
     
    if (latest_close > ema_12_filter and ema_12_filter > wave_ema_high and ema_12_filter > tunnel_ema_high and latest_close<target*0.99):        
        stoploss = min(wave_ema_low,tunnel_ema_low)
        target_time_frame = higher_time_frame[time_frame]
    
        entry_point = latest_close
        trade_trigger = 'Yes'
        potential_profit = np.round((target/entry_point)-1,2)*100
        potential_loss   = np.round((entry_point/stoploss)-1,2)*100

        print(f'You receive a trigger in {time_frame} time frame:\n- entry point: {entry_point}$\n- stoploss: {stoploss}$\n- target: {target}$')
        print(f"- Risk/Reward: {potential_profit/potential_loss}\n- Potentioal Loss: {potential_loss}%\n- Potential Profit: {potential_profit}%")
        return trade_trigger,time_frame,entry_point,stoploss,target
    else:
        print('No setup found')
        return trade_trigger,time_frame,None,None,None



#def updating_stoploss(df):

#def updating_target(df):