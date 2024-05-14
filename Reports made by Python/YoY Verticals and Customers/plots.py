
import matplotlib.pyplot as plt
import os
import numpy as np

def ploy_yoy_verticals(yoy_growth,yoy_pivot_by_years, plot_title,max_name_length=20):
    fig = plt.figure(figsize=(15, 8))

    # Truncate master client names
    truncated_names = [name[:max_name_length] + '...' if len(name) > max_name_length else name for name in yoy_growth['MC Verticals']]

    # Plot the bar chart with conditional positioning of y-axis labels
    bars = plt.bar(range(len(truncated_names)), yoy_growth['diff'], color=['red' if diff < 0 else 'green' for diff in yoy_growth['diff']])

    # Add annotations for diff and per values beside or below the bars
    for idx, (bar, diff, per) in enumerate(zip(bars, yoy_growth['diff'], yoy_growth['per'])):
        diff_str = f'{int(diff / 1000)}k'  # Format diff as thousands with "k" suffix
        #per_str = f'{int(per)}%'
        if per > 3000:
            per_str = '\u221e'
        else:
            per_str = f'{int(per)}%'  # Format per as percentage without decimal points
        
        if diff < 0:
            plt.text(idx, diff - 1000, f'{diff_str}\n{per_str}', ha='center', va='top')
        else:
            plt.text(idx, diff + 1000, f'{diff_str}\n{per_str}', ha='center', va='bottom')

    percentage = yoy_pivot_by_years['per'][0]
    diff_str_div = f'{yoy_pivot_by_years["diff"].iloc[0]/1000000:.2f}M'
    # Add the title
    plt.title(f"{plot_title}:  YOY YTD is {percentage}%    |    Volume Change is {diff_str_div}", fontsize=16)

    # Remove y-axis ticks and labels
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

    # Set x-axis tick positions and labels with rotation and adjust font size
    plt.xticks(range(len(truncated_names)), truncated_names, rotation=45, ha='right', fontsize=16)

    # Remove border box around the graph
    plt.box(False)

    # Save the chart as a PDF file in the output folder
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    pdf_file_path = os.path.join(output_folder, "yoy_customer_growth_analysis.pdf")
    plt.tight_layout()  # Adjust layout to prevent overlap
    #plt.savefig(pdf_file_path)

    #plt.show()

    return fig


def plot_yoy_vertical_and_customers(yoy_growth,yoy_division_dic, plot_title, title_fontsize=25, tick_fontsize=16, annotation_fontsize=25):
    fig = plt.figure(figsize=(15, 8))

    # Plot the bar chart with conditional positioning of y-axis labels
    bars = plt.bar(range(len(yoy_growth['Master Client'])), yoy_growth['diff'], color=['red' if diff < 0 else 'green' for diff in yoy_growth['diff']])

    # Add annotations for diff and per values beside or below the bars
    for idx, (bar, diff, per) in enumerate(zip(bars, yoy_growth['diff'], yoy_growth['per'])):
        diff_str = f'{int(diff / 1000)}k'  # Format diff as thousands with "k" suffix
        per_str = f'{int(per)}%'  # Format per as percentage without decimal points
        if diff < 0:
            plt.text(idx, diff - 600, f'{diff_str}\n{per_str}', ha='center', va='center_baseline', fontsize=annotation_fontsize)
        else:
            plt.text(idx, diff + 1000, f'{diff_str}\n{per_str}', ha='center', va='center_baseline', fontsize=annotation_fontsize)

    # Add the title
    percentage = list(yoy_division_dic[plot_title][0])[0]
    diff_str_div       = f'{int(yoy_division_dic[plot_title][1]/1000)}k'
    plt.title(f"{plot_title} --- YOY YTD is {percentage}%    OR   {diff_str_div} ", fontsize=title_fontsize)

    # Remove y-axis ticks and labels
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

    # Set x-axis tick positions and labels with rotation and adjust font size
    plt.xticks(range(len(yoy_growth['Master Client'])), yoy_growth['Master Client'], rotation=55, ha='right', fontsize=tick_fontsize)

    # Remove border box around the graph
    plt.box(False)

    # Save the chart as a PDF file in the output folder
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    pdf_file_path = os.path.join(output_folder, "yoy_customer_growth_analysis.pdf")
    plt.tight_layout()  # Adjust layout to prevent overlap
    #plt.savefig(pdf_file_path)

    #plt.show()

    return fig

