import pandas as pd
import numpy as np
import logging

# Configure logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingStrategies:
    higher_time_frame = {
         '5 mins':'15 mins',
        '15 mins': '1 hour',
        '1 hour': '4 hours',
        '4 hours': '1 day',
        '1 day': '1 week',
        '1 week':'1 month'
    }

    def __init__(self, df):
        self.df = df

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
        db = self.df.copy(deep=True)
        trade_trigger = 'No'

        df = self.df[self.df["Time Frame"] == time_frame]
        ticker = df['Ticker'][0]
        print(f"start finding setup for {ticker} in {time_frame}")
        
        if df.empty:
            print(f"No data found for the time frame: {time_frame}")
            return trade_trigger, time_frame, None, None, None

        latest_close = df["Close"].iloc[-1]
        ema_12_filter = df["EMA_12_Filter"].iloc[-1]
        wave_ema_high = df["Wave_EMA_High"].iloc[-1]
        wave_ema_low = df["Wave_EMA_Low"].iloc[-1]
        tunnel_ema_high = df["Tunnel_EMA_High"].iloc[-1]
        tunnel_ema_low = df["Tunnel_EMA_Low"].iloc[-1]

        target_time_frame = self.higher_time_frame.get(time_frame)
        if target_time_frame!="1 month" :
            #logging.error(f"No higher time frame found for: {time_frame}")
            target = db[db['Time Frame'] == target_time_frame]["Tunnel_EMA_Low"].iloc[-1]

            if (latest_close > ema_12_filter and
                ema_12_filter > wave_ema_low and
                ema_12_filter > tunnel_ema_high and
                latest_close < target * 0.99):
                stoploss = min(wave_ema_low, tunnel_ema_low)
                entry_point = latest_close
                trade_trigger = 'Yes'
                potential_profit = np.round((target / entry_point) - 1, 2) * 100
                potential_loss = np.round((entry_point / stoploss) - 1, 2) * 100

                print(f'Trigger received in {time_frame} time frame:\n- Entry point: {entry_point}$\n- Stoploss: {stoploss}$\n- Target: {target}$\n- Risk/Reward: {potential_profit / potential_loss}\n- Potential Loss: {potential_loss}%\n- Potential Profit: {potential_profit}%')

                return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':entry_point, 'stoploss':stoploss, 'target':target,'Risk/Reward':potential_profit / potential_loss}
            else:
                print('No setup found')
                return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}
        else:
                print(f"No higher time frame found for: {time_frame}")
                return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}
                    
        #except KeyError as e:
        #    print(f"KeyError: {e}")
        #    return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}
        #except IndexError as e:
            #logging.error(f"IndexError: {e}")
        #    return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}
        #except Exception as e:
            #logging.error(f"An unexpected error occurred: {e}")
        #    return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':None, 'stoploss':None, 'target':None,'Risk/Reward':None}



    def strategy_two(self,time_frame):
            db = self.df.copy(deep=True)
            trade_trigger = 'Yes'

            df = self.df[self.df["Time Frame"] == time_frame]
            ticker = df['Ticker'][0]

            return {'ticker':ticker,'trade_trigger':trade_trigger, 'time_frame':time_frame, 'entry_point':1, 'stoploss':0.5, 'target':2}

# Example usage:
# df = pd.read_csv('your_data.csv')  # Load your data into a DataFrame
# strategy = TradingStrategies(df)
# result = strategy.wavy_tunnel_conservative_strategy('1 hour')
# print(result)
