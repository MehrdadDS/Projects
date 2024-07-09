import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def plot_tier_pieces_by_week(db, main_title, subplot_column):
    # Define the order of tiers
    tier_order = ['1', '2', '3', '4', '5','Zero Volume 2024']
    
    # Create a list of unique values from subplot_column and sort them according to the desired order
    subplots = sorted(db[subplot_column].unique(), key=lambda x: tier_order.index(x) if x in tier_order else float('inf'))
    
    # Determine number of rows and columns based on subplots
    num_rows = len(subplots)
    num_cols = 1
    
    # Create subplots for each unique value in subplot_column
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(14, num_rows * 8), sharex=True)
    
    # Ensure axes is iterable
    if num_rows == 1:
        axes = [axes]
    
    # Format y-axis to show values in thousands
    def thousands(x, pos):
        return '%1.0fk' % (x * 1e-3)

    # Plot data for each unique value in subplot_column
    for ax, subplot_value in zip(axes, subplots):
        for year, color in zip([2023, 2024], ['blue', 'red']):
            subset = db[(db[subplot_column] == subplot_value) & (db['Year'] == year)]
            weekly_pieces = subset.groupby('Week')['Pieces'].sum()
            ax.plot(weekly_pieces.index, weekly_pieces.values, label=f'Year {year}', color=color)
        
        # Calculate YoY YTD % change and YTD volume for 2024
        pieces_2023 = db[(db[subplot_column] == subplot_value) & (db['Year'] == 2023)].groupby('Week')['Pieces'].sum()
        pieces_2024 = db[(db[subplot_column] == subplot_value) & (db['Year'] == 2024)].groupby('Week')['Pieces'].sum()
        
        if not pieces_2024.empty:
            last_week_2024 = pieces_2024.index.max()
            pieces_2023_ytd = pieces_2023[pieces_2023.index <= last_week_2024].sum()
            pieces_2024_ytd = pieces_2024.sum()
            yoy_ytd_change = (pieces_2024_ytd - pieces_2023_ytd) / pieces_2023_ytd * 100 if pieces_2023_ytd != 0 else 0
            pieces_2024_ytd_million = pieces_2024_ytd / 1e6
            title = f'{subplot_column} {subplot_value} (YoY YTD change: {yoy_ytd_change:.2f}%, YTD 2024 Volume: {pieces_2024_ytd_million:.3f}M)'
        else:
            title = f'{subplot_column} {subplot_value}' #(No volume in 2024)
        
        ax.set_title(title, pad=0)
        ax.set_ylabel('Pieces')
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(thousands))
        ax.grid(True)
    
    # Set x-axis ticks to show all weeks
    weeks = sorted(db['Week'].unique())
    plt.xticks(weeks)
    axes[-1].set_xlabel('Week')

    # Add a main title for the whole chart
    fig.suptitle(main_title, fontsize=16, weight='bold')
    
    # Add a single legend for the entire figure
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right')
    
    # Improve layout
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.subplots_adjust(hspace=0.3)
    plt.show()




def plot_customers_by_group(db, main_title, group_column='Tier'):
    # Create subplots for each year
    fig, axes = plt.subplots(1, 2, figsize=(18, 8), sharey=True)
    
    # Define colors for each year
    colors = {2023: 'blue', 2024: 'red'}
    
    # Plot data for each year
    for year, ax in zip([2023, 2024], axes):
        # Filter data for the specific year
        subset = db[db['Year'] == year]
        
        # Group by the specified column and count the number of unique customers
        customer_counts = subset.groupby(group_column)['Master Client'].nunique().sort_values()
        
        # Create a bar plot
        customer_counts.plot(kind='barh', ax=ax, color=colors[year])
        
        # Set titles and labels
        ax.set_title(f'Year {year}', fontsize=14)
        ax.set_xlabel('Number of Customers')
        ax.set_ylabel(group_column)
        ax.grid(True, axis='x')
    
    # Add a main title for the whole chart
    fig.suptitle(main_title, fontsize=16, weight='bold')
    
    # Improve layout
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

