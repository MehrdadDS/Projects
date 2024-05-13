import matplotlib.pyplot as plt
import os
import numpy as np

def plot_yoy_growth(yoy_growth,yoy_pivot_by_years, starting_week, ending_week, plot_title,max_name_length=15, annotation_fontsize=15):
    fig = plt.figure(figsize=(15, 8))

    # Truncate master client names
    truncated_names = [name[:max_name_length] + '...' if len(name) > max_name_length else name for name in yoy_growth['Master Client']]

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
            plt.text(idx, diff - 1000, f'{diff_str}\n{per_str}', ha='center', va='top',fontsize=annotation_fontsize)
        else:
            plt.text(idx, diff + 1000, f'{diff_str}\n{per_str}', ha='center', va='bottom',fontsize=annotation_fontsize)

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

import matplotlib.pyplot as plt
import os

def plot_yoy_growth_div(yoy_growth,yoy_division_dic, starting_week, ending_week, plot_title, title_fontsize=25, tick_fontsize=16, annotation_fontsize=25):
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



import matplotlib.pyplot as plt
import os

def plot_yoy_growth_div_trunc(yoy_growth, yoy_division_dic, plot_title, title_fontsize=25, tick_fontsize=16, annotation_fontsize=25, max_name_length=10):
    fig = plt.figure(figsize=(15, 8))

    # Truncate master client names
    truncated_names = [name[:max_name_length] + '...' if len(name) > max_name_length else name for name in yoy_growth['Master Client']]

    # Plot the bar chart with conditional positioning of y-axis labels
    bars = plt.bar(range(len(truncated_names)), yoy_growth['diff'], color=['red' if diff < 0 else 'green' for diff in yoy_growth['diff']])

    # Add annotations for diff and per values beside or below the bars
    for idx, (bar, diff, per) in enumerate(zip(bars, yoy_growth['diff'], yoy_growth['per'])):
        diff_str = f'{int(diff / 1000)}k'  # Format diff as thousands with "k" suffix
                #per_str = f'{int(per)}%'
        if per > 10000:
            per_str = '\u221e'
        else:
            per_str = f'{int(per)}%'  # Format per as percentage without decimal points
        
        if diff < 0:
            plt.text(idx, diff - 600, f'{diff_str}\n{per_str}', ha='center', va='center_baseline', fontsize=annotation_fontsize)
        else:
            plt.text(idx, diff + 1000, f'{diff_str}\n{per_str}', ha='center', va='bottom', fontsize=annotation_fontsize)

    # Add the title
    percentage = list(yoy_division_dic[plot_title][0])[0]
    diff_str_div = f'{int(yoy_division_dic[plot_title][1]/1000)}k'
    plt.title(f"{plot_title} :  YOY YTD is {percentage}%    |    Volume Change is {diff_str_div} ", fontsize=title_fontsize)

    # Remove y-axis ticks and labels
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

    # Set x-axis tick positions and labels with rotation and adjust font size
    plt.xticks(range(len(truncated_names)), truncated_names, rotation=55, ha='right', fontsize=tick_fontsize)

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



def plot_pie_chart(dataframe,name,title_fontsize=15, label_fontsize=10):
    # Filter dataframe for negative differences and specified divisions
    dataframe = dataframe[dataframe['diff'] < 0]

    # Take absolute values of differences
    dataframe['diff'] = np.abs(dataframe['diff'])

    # Extracting data for the pie chart
    divisions = dataframe[name]
    differences = dataframe['diff']

    # Convert differences to "k" format with negative sign
    diff_k_format = [f"-{int(diff/1000)}k" for diff in differences]

    # Create a list of labels with negative differences
    labels = [f"{div}\n({diff_k})" for div, diff_k in zip(divisions, diff_k_format)]

    # Sort the data for the pie chart
    sorted_indices = np.argsort(differences)[::-1]  # Sort indices in descending order
    sorted_divisions = divisions.iloc[sorted_indices]
    sorted_labels = [labels[i] for i in sorted_indices]

    # Creating the pie chart
    fig, ax = plt.subplots(figsize=(12, 10))  # Increase figure size
    wedges, texts, autotexts = ax.pie(differences.iloc[sorted_indices], labels=None, startangle=140, labeldistance=1.1, pctdistance=0.85, autopct='%1.1f%%', textprops={'fontsize': label_fontsize})  # Increase pctdistance
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    
    # Add labels with lines
    for i, (div, diff_k, wedge) in enumerate(zip(sorted_divisions, diff_k_format, wedges)):
        ang = (wedge.theta2 + wedge.theta1) / 2.
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        ax.annotate(f"{div}\n({diff_k})", xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), fontsize=label_fontsize, textcoords="offset points", ha=horizontalalignment, va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"), arrowprops=dict(arrowstyle="->", connectionstyle=connectionstyle, color="black"))

    # Add title with some padding
    ax.set_title('Divisional Losses: Distribution of Volume Reduction', pad=30, fontsize=title_fontsize)

    return fig

