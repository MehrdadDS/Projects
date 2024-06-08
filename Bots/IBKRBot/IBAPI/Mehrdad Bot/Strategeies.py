# Strategeies.py

import pandas as pd
import numpy as np

class TradingStrategies:
    def __init__(self, data):
        self.data = data
        self.higher_time_frame = {
         '5 mins':'15 mins',
        '15 mins': '1 hour',
        '1 hour': '4 hours',
        '4 hours': '1 day',
        '1 day': '1 week',
        '1 week':'1 month'
    }

    def strategy_two(self, time_frame):
        # Placeholder for actual strategy logic
        df = self.data[self.data['Time Frame'] == time_frame]
        last_row = df.iloc[-1]

        trade_trigger = "Yes" if last_row['MACD_Line'] > last_row['Signal_Line'] else "No"
        entry_price = round(last_row['Close'], 2)
        stop_loss = round(entry_price * 0.98, 2)
        target_price = round(entry_price * 1.02, 2)
        risk_to_reward = round((target_price - entry_price) / (entry_price - stop_loss), 2)

        signal = {
            "ticker": last_row['Ticker'],
            "trade_trigger": trade_trigger,
            "time_frame": time_frame,
            "entry_point": entry_price,
            "stoploss": stop_loss,
            "target": target_price,
            "risk_to_reward": risk_to_reward
        }

        return signal
    

    def wavy_tunnel_conservative_strategy(self, time_frame):
        """
        Checks if the latest closing price is above the specified EMA filters
        and returns True if all conditions are met.

        Args:
        time_frame (str): The time frame to check the strategy against.

        Returns:
        tuple: A tuple containing trade trigger status, time frame, entry point,
               stop loss, and target.
        """
        #try:
        db = self.data.copy(deep=True)
        trade_trigger = 'No'

        df = db[db["Time Frame"] == time_frame]
        last_row = df.iloc[-1]
        ticker = last_row['Ticker']
        print(f"start finding setup for {ticker} in {time_frame}")
        
        if df.empty:
            print(f"No data found for the time frame: {time_frame}")
            return trade_trigger, time_frame, None, None, None

        latest_close        = round(last_row['Close'],2)
        ema_12_filter       = round(last_row["EMA_12_Filter"],2)
        wave_ema_high       = round(last_row["Wave_EMA_High"],2)
        wave_ema_low        = round(last_row["Wave_EMA_Low"],2)
        tunnel_ema_high     = round(last_row["Tunnel_EMA_High"],2)
        tunnel_ema_low      = round(last_row["Tunnel_EMA_Low"],2)
        target_time_frame   = self.higher_time_frame.get(time_frame)

        if target_time_frame!="1 month" :
            #logging.error(f"No higher time frame found for: {time_frame}")
            target_price = round(db[db['Time Frame'] == target_time_frame]["Tunnel_EMA_Low"].iloc[-1],2)

            if (latest_close > ema_12_filter and
                ema_12_filter > wave_ema_low and
                ema_12_filter > tunnel_ema_high and
                latest_close < target_price * 0.99):
                stop_loss = min(wave_ema_low, tunnel_ema_low)
                entry_price = latest_close
                trade_trigger = 'Yes'
                potential_profit = np.round((target_price / entry_price) - 1, 2) * 100
                potential_loss = np.round((entry_price / stop_loss) - 1, 2) * 100
                risk_to_reward = round((target_price - entry_price) / (entry_price - stop_loss), 2)

                print(f'Trigger received in {time_frame} time frame:\n- Entry point: {entry_price}$\n- Stoploss: {stop_loss}$\n- Target: {target_price}$\n- Risk/Reward: {potential_profit / potential_loss}\n- Potential Loss: {potential_loss}%\n- Potential Profit: {potential_profit}%')

                signal = {
                    "ticker": ticker,
                    "trade_trigger": trade_trigger,
                    "time_frame": time_frame,
                    "entry_point": entry_price,
                    "stoploss": stop_loss,
                    "target": target_price,
                    "risk_to_reward": risk_to_reward
                }     
            else:
                signal={
                    "ticker": ticker,
                    "time_frame": time_frame,
                    "trade_trigger": "No",                    
                }
                print(f"No signal found for {ticker} in {time_frame} time frame")
        else:
            signal={
            "ticker": ticker,
            "time_frame": time_frame,
            "trade_trigger": "No",                    
            }
            print(f"No signal found for {ticker} in {time_frame} time frame")

        return signal
        #except KeyError as e:
        #    print(f"KeyError: {e}")
        #    return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}
        #except IndexError as e:
            #logging.error(f"IndexError: {e}")
        #    return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}
        #except Exception as e:
            #logging.error(f"An unexpected error occurred: {e}")
        #    return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}

