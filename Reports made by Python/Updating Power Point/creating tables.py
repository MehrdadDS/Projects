import pandas as pd
import matplotlib.pyplot as plt

# Sample data for stops variance
stops_variance_data = {
    'Terminal Type': ['A', 'B', 'C'],
    'Total Stops Variance': ['+4%', '+1.7%', '+1.4%'],
    'Stops per Day Variance': ['+5.4', '+1.2', '+1.3'],
    'Terminals more than 15% variance': [
        'Above – None\nBelow – None',
        'Above – None\nBelow – None',
        'Above – SARNIA, GRAND FALLS\nBelow – None'
    ]
}

stops_variance_df = pd.DataFrame(stops_variance_data)

# Sample data for pieces variance
pieces_variance_data = {
    'Terminal Type': ['A', 'B', 'C'],
    'Delivery Pieces Variance': ['+2%', '-0.8%', '0.2%'],
    'Pieces per Day Variance': ['+5.8', '-1.2', '0.3'],
    'Terminals more than 15% variance': [
        'Above – None\nBelow – None',
        'Above – None\nBelow – None',
        'Above – HIGH PRAIRIE\nBelow – None'
    ]
}

pieces_variance_df = pd.DataFrame(pieces_variance_data)

# Function to create table
def create_table(ax, df, title):
    ax.axis('off')
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc='center',
        loc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    col_widths = [0.1, 0.2, 0.2, 0.5]  # Adjusted column widths

    for (i, j), cell in table.get_celld().items():
        cell.set_edgecolor('black')
        if i == 0:
            cell.set_fontsize(12)
            cell.set_text_props(weight='bold')
            cell.set_edgecolor('black')
            cell.set_linewidth(2)
        cell.set_width(col_widths[j])

        if j == 3 and i != 0:  # Adjusting the alignment and spacing for the last column
            cell.set_text_props(ha='left', va='top')
            lines = cell.get_text().get_text().split('\n')
            cell.get_text().set_text('\n'.join(lines))
            cell.set_fontsize(10)

    ax.set_title(title, fontsize=14, fontweight='bold')

# Create plot
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# Plot the tables
create_table(axes[0], stops_variance_df, 'Stops Variance')
create_table(axes[1], pieces_variance_df, 'Pieces Variance')

plt.tight_layout()
plt.show()
