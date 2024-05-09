import pandas as pd
import matplotlib.pyplot as plt

def plot_top_dest_terminals(df, output_folder, customer_name, title_fontsize=16, label_fontsize=20, terminal_fontsize=12):
    # Sort by 'diff'
    sorted_df = df.sort_values(by='diff')

    # Get top 10 highest and lowest Dest Terminal based on 'diff'
    top_10_highest = sorted_df.tail(15)
    top_10_lowest = sorted_df.head(15)

    # Plot top 10 highest
    plt.figure(figsize=(9, 10))
    plt.barh(top_10_highest['Dest Terminal'], top_10_highest['diff'], color='green')
    plt.title(f'Top Terminal Incliners YoY YTD for {customer_name}', fontsize=title_fontsize)
    plt.xticks([])  # Hide x-axis ticks
    for index, value in enumerate(top_10_highest['diff']):
        plt.text(value, index, f'+{value/1000:.1f}k  |  +{top_10_highest["per"].iloc[index]}%', color='black',fontsize=label_fontsize)
    plt.yticks(fontsize=terminal_fontsize)  # Set font size for terminal labels
    plt.tight_layout()
    plt.gca().spines['top'].set_visible(False)  # Remove border
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.savefig(f"{output_folder}/top_10_highest_{customer_name}.png", dpi=400)  # Save as PNG with high resolution (300 dpi)
    plt.close()

    # Plot top 10 lowest
    plt.figure(figsize=(10, 10))
    plt.barh(top_10_lowest['Dest Terminal'], top_10_lowest['diff'], color='red')
    plt.title(f'Top Terminal Decliners YoY YTD for {customer_name}', fontsize=title_fontsize)
    plt.xticks([])  # Hide x-axis ticks
    for index, value in enumerate(top_10_lowest['diff']):
        plt.text(value, index, f'-{abs(value/1000):.1f}k  |  {top_10_lowest["per"].iloc[index]}%',ha='right', color='black',fontsize=label_fontsize)
    plt.yticks(fontsize=terminal_fontsize)  # Set font size for terminal labels
    plt.gca().spines['top'].set_visible(False)  # Remove border
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    # Reversing the y-axis
    #plt.gca().invert_yaxis()
    #plt.gca().tick_params(axis='y', direction='in', pad=-580,right=True)  # Set the major y-ticks to the right side
    # Moving y-ticks to the right side
    plt.tick_params(axis='y', direction='inout',pad=-580, right=True, left=False)
    plt.tight_layout()
    plt.savefig(f"{output_folder}/top_10_lowest_{customer_name}.png", dpi=400)  # Save as PNG with high resolution (300 dpi)
    plt.close()

# Example usage:
# plot_top_dest_terminals(df, "output_folder_path", "Customer Name", title_fontsize=16, label_fontsize=20, terminal_fontsize=14)



def plot_top_dest_divisions(df, output_folder, customer_name, title_fontsize=16, label_fontsize=20, terminal_fontsize=12):
    # Sort by 'diff'
    sorted_df = df.sort_values(by='diff')

    # Get top 10 highest and lowest Dest Terminal based on 'diff'
    top_10_highest = sorted_df.tail(7)
    top_10_lowest = sorted_df.head(7)

    # Plot top 10 highest
    plt.figure(figsize=(9, 10))
    plt.barh(top_10_highest['Dest Division'], top_10_highest['diff'], color='green')
    plt.title(f'Top Terminal Incliners YoY YTD for {customer_name}', fontsize=title_fontsize)
    plt.xticks([])  # Hide x-axis ticks
    for index, value in enumerate(top_10_highest['diff']):
        plt.text(value, index, f'+{value/1000:.1f}k  |  +{top_10_highest["per"].iloc[index]}%', color='black',fontsize=label_fontsize)
    plt.yticks(fontsize=terminal_fontsize)  # Set font size for terminal labels
    plt.tight_layout()
    plt.gca().spines['top'].set_visible(False)  # Remove border
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.savefig(f"{output_folder}/top_10_highest__division_{customer_name}.png", dpi=400)  # Save as PNG with high resolution (300 dpi)
    plt.close()

    # Plot top 10 lowest
    plt.figure(figsize=(10, 10))
    plt.barh(top_10_lowest['Dest Division'], top_10_lowest['diff'], color='red')
    plt.title(f'Top Terminal Decliners YoY YTD for {customer_name}', fontsize=title_fontsize)
    plt.xticks([])  # Hide x-axis ticks
    for index, value in enumerate(top_10_lowest['diff']):
        plt.text(value, index, f'-{abs(value/1000):.1f}k  |  {top_10_lowest["per"].iloc[index]}%',ha='right', color='black',fontsize=label_fontsize)
    plt.yticks(fontsize=terminal_fontsize)  # Set font size for terminal labels
    plt.gca().spines['top'].set_visible(False)  # Remove border
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    # Reversing the y-axis
    #plt.gca().invert_yaxis()
    #plt.gca().tick_params(axis='y', direction='in', pad=-580,right=True)  # Set the major y-ticks to the right side
    # Moving y-ticks to the right side
    plt.tick_params(axis='y', direction='inout',pad=-550, right=True, left=False)
    plt.tight_layout()
    plt.savefig(f"{output_folder}/top_10_lowest_division_{customer_name}.png", dpi=400)  # Save as PNG with high resolution (300 dpi)
    plt.close()

import matplotlib.pyplot as plt



def draw_diff_chart(df, output_folder, customer_name, title='', title_fontsize=14):
    # Sort the DataFrame based on absolute values of 'diff'
    df_sorted = df.reindex(df['diff'].sort_values(ascending=True).index)
    
    # Define colors based on the sign of the difference
    colors = ['red' if val < 0 else 'green' for val in df_sorted['diff']]
    
    # Convert difference values to a more readable format
    diff_values = []
    for i, val in enumerate(df_sorted['diff']):
        if val < 0:
            diff_values.append(f"{val/1000:.1f}K | -{abs(df_sorted['per'].iloc[i]/100):.0%}")
        else:
            diff_values.append(f"+{val/1000:.1f}K | +{abs(df_sorted['per'].iloc[i]/100):.0%}")
    
    # Plotting
    plt.figure(figsize=(7, 5))
    bars = plt.barh(df_sorted['Dest Division'], df_sorted['diff'], color=colors)
    
    # Adding the diff values on bars
    for i, (value, color) in enumerate(zip(diff_values, colors)):
        plt.text(df_sorted['diff'].iloc[i], i, value, ha='left', color='black')
    
    # Customizing the chart
    #plt.xlabel('Difference')
    plt.title(title, fontsize=title_fontsize)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.xticks([])  # Remove x-axis ticks
    
    # Remove spines in all directions
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.tight_layout()
    
    # Adjust y-axis limits to fit long division names
    plt.ylim(-0.5, len(df_sorted) - 0.5)
    
    #plt.show()
    plt.savefig(f"{output_folder}/divisions_{customer_name}.png", dpi=400)  # Save as PNG with high resolution (300 dpi)
    plt.close()

import matplotlib.pyplot as plt

def plot_yoy_weekly_trend(df, output_folder, customer_name,):
    # Group the dataframe by Year
    grouped = df.groupby('Year')
    
    # Define colors for each year
    colors = ['blue', 'green', 'red', 'orange', 'purple', 'cyan', 'magenta', 'yellow']
    
    # Plot each group
    for i, (year, group) in enumerate(grouped):
        plt.plot(group['Week'], group['Pieces'], color=colors[i % len(colors)], label=int(year))
    
    # Set labels and title
    plt.xlabel('Week')
    plt.ylabel('Pieces')
    plt.title('Year-over-Year Weekly Trend')
    
    # Add legend
    plt.legend(title='Year', loc='best')
    
    # Show plot
    plt.grid(True)
    #plt.show()
    plt.savefig(f"{output_folder}/{customer_name}-Trend chart.png", dpi=400)  # Save as PNG with high resolution (300 dpi)


# Call the function with your dataframe
