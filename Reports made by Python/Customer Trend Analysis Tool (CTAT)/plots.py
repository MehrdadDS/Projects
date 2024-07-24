import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
from matplotlib.ticker import MultipleLocator

def plot_trend_lines(merged_db, result_db, output_file, last_week_2024):
    # Create a single figure with subplots
    num_customers = len(merged_db['Master Client'].unique())
    rows = (num_customers + 1) // 2  # Calculate number of rows (2 plots per row)
    fig, axs = plt.subplots(rows, 2, figsize=(20, 10 * rows))
    axs = axs.flatten()  # Flatten the 2D array of axes to 1D for easy indexing

    for idx, customer in enumerate(merged_db['Master Client'].unique()):
        ax = axs[idx]
        # Filter data for the current customer
        customer_data = merged_db[merged_db['Master Client'] == customer].copy()
        
        # Filter data up to last_week_2024
        customer_data = customer_data[(customer_data['Year'] < 2024) | 
                                      ((customer_data['Year'] == 2024) & (customer_data['Week'] <= last_week_2024))]
        
        # Calculate YTD volumes for 2023 and 2024
        ytd_2023 = customer_data[(customer_data['Year'] == 2023) & (customer_data['Week'] <= last_week_2024)]['Pieces'].sum()
        ytd_2024 = customer_data[(customer_data['Year'] == 2024) & (customer_data['Week'] <= last_week_2024)]['Pieces'].sum()
        
        # Calculate YoY YTD% change
        if ytd_2023 != 0:
            yoy_change = ((ytd_2024 - ytd_2023) / ytd_2023) * 100
        else:
            yoy_change = float('inf') if ytd_2024 > 0 else 0
        
        # Convert Year to integer and then to datetime
        customer_data['Year'] = customer_data['Year'].astype(int)
        customer_data['Date'] = pd.to_datetime(customer_data['Year'].astype(str) + '-W' + 
                                               customer_data['Week'].astype(str).str.zfill(2) + '-1', format='%Y-W%W-%w')
        
        # Sort the data by date
        customer_data = customer_data.sort_values('Date')
        
        # Plot the trend line
        ax.plot(customer_data['Date'], customer_data['Pieces'], label='Pieces')
        
        # Set x-axis ticks and labels for the years and weeks
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        ax.xaxis.set_minor_locator(MultipleLocator(7))  # Weekly intervals

        # Adding week numbers within each year
        for year in customer_data['Year'].unique():
            year_data = customer_data[customer_data['Year'] == year]
            for week in year_data['Week'].unique():
                date = pd.to_datetime(f"{year}-W{week:02d}-1", format='%Y-W%W-%w')
                if week % 4 == 0:  # Label every 4 weeks for clarity
                    ax.text(date, ax.get_ylim()[0], f"{week}", ha='center', va='top', fontsize=6, rotation=90)
        
        # Rotate and align the tick labels so they look better
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, ha='center')
        
        # Add labels and title
        ax.set_xlabel('Year - Week', fontsize=8)
        ax.set_ylabel('Pieces', fontsize=8)
        title = (f'{customer} | '
                 f'2024 YTD: {ytd_2024:,.0f} | '
                 f'2023 YTD: {ytd_2023:,.0f} | '
                 f'YoY YTD: {yoy_change:.2f}%')
        ax.set_title(title, fontsize=8, wrap=True)
        
        # Add trend information to the plot
        if customer in result_db:
            trend_info = result_db[customer]
            trend_text = f"Trend: {trend_info[0]}\n"
            trend_text += f"p: {trend_info[1]:.4f}\n"
            trend_text += f"Sig: {trend_info[2]}\n"
            trend_text += f"Avg: {trend_info[3]} pcs"
            ax.text(0.05, 0.95, trend_text, transform=ax.transAxes, verticalalignment='top', 
                    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8), fontsize=6)
        
        # Add legend
        ax.legend(fontsize=6)
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.tick_params(axis='both', which='minor', labelsize=6)

    # Remove any unused subplots
    for idx in range(num_customers, len(axs)):
        fig.delaxes(axs[idx])

    # Adjust layout
    plt.tight_layout()
    
    return fig  # Return the figure for saving in the main script