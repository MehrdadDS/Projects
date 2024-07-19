import pandas as pd
import matplotlib.pyplot as plt




def plot_trendlines(db_plots, db_peak, adjusting_variables, current_year=2024):
    # Ensure 'Week' and 'Year' are present in both dataframes
    if 'Week' not in db_plots.columns or 'Year' not in db_plots.columns:
        raise ValueError("Both 'Week' and 'Year' columns must be present in the dataframes")


    db_plots = db_plots[db_plots['Year']<current_year+1]
    db_peak = db_peak[db_peak['Year']<current_year+1]
    # Aggregate data by Year and Week
    db_plots_agg = db_plots.groupby(['Year', 'Week']).sum().reset_index()
    db_peak_agg = db_peak.groupby(['Year', 'Week']).sum().reset_index()

    # Merge db_plots and db_peak on common columns
    merged_df = pd.merge(db_plots_agg, db_peak_agg, on=['Year', 'Week'], suffixes=('', '_EDITED'), how='left')
    
    # Plot trendlines for each variable
    for variable in adjusting_variables:
        if variable not in merged_df.columns or f"{variable}_EDITED" not in merged_df.columns:
            raise ValueError(f"Both '{variable}' and '{variable}_EDITED' must be present in the merged dataframe")
        
        plt.figure(figsize=(14, 7))
        
        # Plot the regular variable
        for year in merged_df['Year'].unique():
            data = merged_df[merged_df['Year'] == year]
            plt.plot(data['Week'], data[variable], label=f'{variable} {year}')
        
        # Plot the edited variable for the current year
        data_current_year = merged_df[merged_df['Year'] == current_year]
        plt.plot(data_current_year['Week'], data_current_year[f"{variable}_EDITED"], label=f'{variable}_EDITED {current_year}', linestyle='--', color='black')
        
        plt.title(f'{variable}')
        plt.xticks(merged_df['Week'])
        plt.xlabel('Week')
        plt.ylabel('Volume')
        plt.legend()
        plt.grid(True)
        plt.show()
