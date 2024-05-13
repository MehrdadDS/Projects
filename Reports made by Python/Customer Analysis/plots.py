import os
import matplotlib.pyplot as plt
from datetime import datetime


import matplotlib.pyplot as plt
import os
from datetime import datetime

def plot_yearly_trend(df, customer, output_folder, xticks_size=10, graph_title="Yearly Customer Trend", x_label="Week", y_label="Pieces"):
    # Group the dataframe by Year
    grouped = df.groupby('Year')

    # Create a new figure
    plt.figure()
    # Plot each group
    for name, group in grouped:
        plt.plot(group['Week'], group['Pieces'], label=name)

        
    # Customize xticks
    plt.xticks(fontsize=xticks_size)
    plt.yticks(fontsize=xticks_size)


    # Add labels and legend
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(title='Year')
    plt.title(f"{graph_title} - {customer}")
    plt.xticks(df['Week'])

    # Format y-axis to display in k's
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1000):,}k'))

    plt.grid(True)



    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get current date
    current_date = datetime.now().strftime("%Y%m%d")
    
    # Save as PNG with customer name and date in the specified output folder
    plt.savefig(os.path.join(output_folder, f"{customer}_trend_{current_date}.png"),dpi=300)
    
    # Show the plot
    #plt.show()


def plot_diff_division_bar_chart(df, customer, output_folder, title, title_font_size=16, label_font_size=12, xtick_font_size=10):
    # Set figure size
    fig = plt.figure(figsize=(10, len(df) * 0.7))  # Adjust figure height based on the number of divisions
    
    # Create a new axis
    ax = fig.add_subplot(111)
    
    # Extract relevant columns
    divisions = df['Dest Division']
    diffs = df['diff']
    pers = df['per']
    
    # Plot bars
    colors = ['green' if diff >= 0 else 'red' for diff in diffs]
    ax.barh(divisions, diffs, color=colors)
    
    # Add value annotations
    for i, (diff, per) in enumerate(zip(diffs, pers)):
        if diff >= 0:
            ax.text(diff, i, f'+{diff/1000:.1f}k | +{int(per)}%', ha='left', va='center', fontsize=label_font_size)
        else:
            ax.text(diff, i, f'{diff/1000:.1f}k | {int(per)}%', ha='left', va='center', fontsize=label_font_size)
    
    # Set title and labels
    ax.set_title(title+f"- {customer}", fontsize=title_font_size)
    ax.tick_params(axis='x', labelsize=xtick_font_size)
    
    # Remove spines from bottom, left, and right
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Rotate division names for better readability
    ax.set_yticklabels(divisions, rotation=0, fontsize=xtick_font_size)  # Adjust rotation angle if needed
    # Adjust left padding of y-axis to shift yticks to the right
    #ax.tick_params(axis='y', pad=-50)  # Adjust the value as needed
    # Remove xticks showing diff values
    ax.set_xticks([])
    plt.tight_layout()

    # Increase picture save quality to 300 DPI
    current_date = datetime.now().strftime("%Y%m%d")
    plt.savefig(os.path.join(output_folder, f"{customer}_division_{current_date}.png"), dpi=300)
    
    # Show the plot
    #plt.show()

# Example usage:
# plot_diff_division_bar_chart(df, 'Customer Name', 'output_folder', 'Title')



def plot_diff_terminal_bar_chart(df, customer, output_folder, title, top_positive=10, top_negative=15, title_font_size=16, label_font_size=12, xtick_font_size=1):
    # Sort the DataFrame based on 'diff' column
    df_sorted = df.sort_values(by='diff', ascending=False)
    
    # Extract top positive and negative divisions
    top_positive_terminals = df_sorted.head(top_positive)
    top_negative_terminals = df_sorted.tail(top_negative)
    
    # Plot top positive divisions
    plot_bar_chart(top_positive_terminals, customer, output_folder, f" Top {top_positive} Incliners", title_font_size, label_font_size, xtick_font_size)
    
    # Plot top negative divisions
    plot_bar_chart(top_negative_terminals, customer, output_folder, f" Top {top_negative} Decliners", title_font_size, label_font_size, xtick_font_size)
    plt.tight_layout()

    plt.close()

def plot_bar_chart(df, customer, output_folder, title, title_font_size=16, label_font_size=12, xtick_font_size=10):
    # Set figure size
    fig = plt.figure(figsize=(15, 8))
    df = df.sort_values(by='diff', ascending=True)
    # Create a new axis
    ax = fig.add_subplot(111)
    
    # Extract relevant columns
    terminals = df['Dest Terminal']
    diffs = df['diff']
    pers = df['per']
    
    # Plot bars
    colors = ['green' if diff >= 0 else 'red' for diff in diffs]
    ax.barh(terminals, diffs, color=colors)
    
    # Add value annotations
    for i, (diff, per) in enumerate(zip(diffs, pers)):
        if diff >= 0:
            ax.text(diff, i, f'+{diff/1000:.1f}k | +{int(per)}%', ha='left', va='center', fontsize=label_font_size)
        else:
            ax.text(diff, i, f'{diff/1000:.1f}k | {int(per)}%', ha='left', va='center', fontsize=label_font_size)
    
    # Set title and labels
    ax.set_title(title+f"- {customer}", fontsize=title_font_size)
    #ax.set_ylabel('Destination Division', fontsize=label_font_size)
    ax.tick_params(axis='x', labelsize=xtick_font_size)
    ax.tick_params(axis='y', labelsize=xtick_font_size)

    # Remove spines from bottom, left, and right
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Remove xticks showing diff values
    ax.set_xticks([])
    plt.tight_layout()

    # Save the plot
    current_date = datetime.now().strftime("%Y%m%d")
    plt.savefig(os.path.join(output_folder, f"{customer}_{title.lower().replace(' ', '_')}_{current_date}.png"),dpi=300)
    
    # Show the plot
    #plt.show()

def plot_diff_terminal_type_bar_chart(df, customer, output_folder, title, title_font_size=16, label_font_size=20, xtick_font_size=15):
    # Set figure size
    fig = plt.figure(figsize=(15, 8))
    
    # Create a new axis
    ax = fig.add_subplot(111)
    
    # Extract relevant columns
    divisions = df['Terminal Type']
    diffs = df['diff']
    pers = df['per']
    
    # Plot bars
    colors = ['green' if diff >= 0 else 'red' for diff in diffs]
    ax.barh(divisions, diffs, color=colors)
    
    # Add value annotations
    for i, (diff, per) in enumerate(zip(diffs, pers)):
        if diff >= 0:
            ax.text(diff, i, f'+{diff/1000:.1f}k | +{int(per)}%', ha='left', va='center', fontsize=label_font_size)
        else:
            ax.text(diff, i, f'{diff/1000:.1f}k | {int(per)}%', ha='left', va='center', fontsize=label_font_size)
    
    # Set title and labels
    ax.set_title(title+f" - {customer}", fontsize=title_font_size,loc='center')
    #ax.set_ylabel('Destination Division', fontsize=label_font_size)
    ax.tick_params(axis='x', labelsize=xtick_font_size)
    ax.tick_params(axis='y', labelsize=xtick_font_size)

    # Remove spines from bottom, left, and right
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    
    # Remove xticks showing diff values
    ax.set_xticks([])
    plt.tight_layout()

    # Save the plot
    current_date = datetime.now().strftime("%Y%m%d")
    plt.savefig(os.path.join(output_folder, f"{customer}_TerminalType_{current_date}.png"),dpi=300)
    
    # Show the plot
    #plt.show()
    
