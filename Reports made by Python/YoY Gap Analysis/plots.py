import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt


def create_national_line_chart(df, holiday_weeks, output_pdf, title_fontsize=12, label_fontsize=10):
    fig, ax = plt.subplots(figsize=(10, 6))
    

    for year, weeks in holiday_weeks.items():
        for week in weeks:
            style = 'solid' if year == 2023 else 'dashed'
            linewidth_op = 5 if year == 2023 else 2
            color_year = 'orange' if year == 2023 else 'purple'
            ax.axvline(x=week, color=color_year, linestyle=style, linewidth=linewidth_op)
    
    national_label = f"National ({df['diff'].iloc[-1] / 1000:.1f}k)"   

    ax.plot(df['Week'], df['diff'], label=national_label, color='black', marker='o', markersize=5)
            
    ax.set_title('National', fontsize=title_fontsize)
    ax.set_xlabel('Week', fontsize=label_fontsize)
    ax.set_ylabel('YoY WoW Gap', fontsize=label_fontsize)
    ax.tick_params(axis='both', which='major', labelsize=label_fontsize)
    ax.legend(fontsize=label_fontsize)

    ax.set_xticks(df['Week'])
    
    ax.axhline(y=0, color='black', linestyle="--", linewidth=1)
    ax.fill_between(df['Week'], df['diff'], where=(df['diff'] > 0), color='lightgreen', alpha=0.3)
    ax.yaxis.set_major_formatter(lambda x, _: f'{x / 1000:.1f}k')
        
    plt.tight_layout()
    plt.savefig(output_pdf)
    plt.close()
    return fig





import matplotlib.pyplot as plt

def create_line_charts(df, holiday_weeks, output_pdf, title_fontsize=12, label_fontsize=10):
    regions = df['Region'].unique()
    colors = ['blue', 'green', 'red','orange','pink']  # Different colors for each region
    fig, axs = plt.subplots(len(regions), 1, figsize=(10, 6 * len(regions)))
    
    for i, region in enumerate(regions):
        region_df = df[df['Region'] == region]
        dest_divisions = region_df['Dest Division'].unique()

        for year, weeks in holiday_weeks.items():
            for week in weeks:
                style = 'solid' if year == 2023 else 'dashed'
                linewidth_op = 5 if year == 2023 else 2
                color_year = 'orange' if year == 2023 else 'purple'
                axs[i].axvline(x=week, color=color_year, linestyle=style, linewidth=linewidth_op)





        for j, dest_division in enumerate(dest_divisions):
            division_data = region_df[region_df['Dest Division'] == dest_division]
            division_label = f"{dest_division} ({division_data['diff'].iloc[-1] / 1000:.1f}k)"
            axs[i].plot(division_data['Week'], division_data['diff'], label=division_label, color=colors[j] ,marker='*', markersize=6)
            
        axs[i].set_title(region, fontsize=title_fontsize)
        axs[i].set_xlabel('Week', fontsize=label_fontsize)
        axs[i].set_ylabel('YoY WoW Gap', fontsize=label_fontsize)
        axs[i].tick_params(axis='both', which='major', labelsize=label_fontsize)
        axs[i].legend(fontsize=label_fontsize)
        

        
        axs[i].axhline(y=0, color='black', linestyle="--", linewidth=1)
        axs[i].fill_between(region_df['Week'], region_df['diff'], where=(region_df['diff'] > 0), color='lightgreen', alpha=0.3)
        axs[i].yaxis.set_major_formatter(lambda x, _: f'{x / 1000:.1f}k')
        
    plt.tight_layout()
    plt.savefig(output_pdf)
    plt.close()
    return fig




def create_line_charts_by_divisions(df, holiday_weeks,division_list, output_pdf, title_fontsize=12, label_fontsize=10):
    #dest_divisions = df['Dest Division'].unique()
    #colors = ['blue', 'green', 'red','orange','pink','yellow','black']  # Different colors for each region
    colors = ['#1E90FF', '#228B22', '#8B0000', '#FF8C00', '#FF69B4', '#FFD700', '#2F4F4F']

    fig, axs = plt.subplots(len(division_list), 1, figsize=(10, 6 * len(division_list)))
    
    for i, division in enumerate(division_list):
        division_df = df[df['Dest Division'] == division]
        #dest_divisions = region_df['Dest Division'].unique()

        for year, weeks in holiday_weeks.items():
            for week in weeks:
                style = 'solid' if year == 2023 else 'dashed'
                linewidth_op = 5 if year == 2023 else 2
                color_year = 'orange' if year == 2023 else 'purple'
                axs[i].axvline(x=week, color=color_year, linestyle=style, linewidth=linewidth_op)





        #for j, dest_division in enumerate(dest_divisions):
        division_data = df[df['Dest Division'] == division]
        division_label = f"{division} ({division_data['diff'].iloc[-1] / 1000:.1f}k)"
        axs[i].plot(division_data['Week'], division_data['diff'], label=division_label, color=colors[i] ,marker='*', markersize=6)
            
        axs[i].set_title(division, fontsize=title_fontsize)
        axs[i].set_xlabel('Week', fontsize=label_fontsize)
        axs[i].set_ylabel('YoY WoW Gap', fontsize=label_fontsize)
        axs[i].tick_params(axis='both', which='major', labelsize=label_fontsize)
        axs[i].legend(fontsize=label_fontsize)
        
        axs[i].set_xticks(df['Week'])

        
        axs[i].axhline(y=0, color='black', linestyle="--", linewidth=1)
        axs[i].fill_between(division_df['Week'], division_df['diff'], where=(division_df['diff'] > 0), color='lightgreen', alpha=0.3)
        axs[i].yaxis.set_major_formatter(lambda x, _: f'{x / 1000:.1f}k')
        
    plt.tight_layout()
    plt.savefig(output_pdf)
    plt.close()
    return fig




import matplotlib.pyplot as plt

def line_bar_plot(dataframe,holiday_weeks):
    fig, ax1 = plt.subplots()


    for year, weeks in holiday_weeks.items():
        for week in weeks:
            style = 'solid' if year == 2023 else 'dashed'
            linewidth_op = 5 if year == 2023 else 2
            color_year = 'orange' if year == 2023 else 'purple'
            ax1.axvline(x=week, color=color_year, linestyle=style, linewidth=linewidth_op)





    # Line plots for 2023 and 2024
    ax1.plot(dataframe['Week'], dataframe[2023], marker='o', label='2023')
    ax1.plot(dataframe['Week'], dataframe[2024], marker='o', label='2024')
    ax1.set_xlabel('Week')
    ax1.set_ylabel('Pieces')
    ax1.tick_params(axis='y')
    ax1.set_xticks(dataframe['Week'])

    # Bar plot for 'diff'
    ax2 = ax1.twinx()
    colors = ['lightgreen' if diff >= 0 else 'lightcoral' for diff in dataframe['diff_y']]
    ax2.bar(dataframe['Week'], dataframe['diff_y'], color=colors, alpha=0.5, label='Diff')
    ax2.set_ylabel('Diff')
    ax2.tick_params(axis='y')

    # Add legend
    fig.legend(loc='upper right')

    # Show the plot
    plt.title('Weekly Comparison: Pieces and Difference')
    plt.show()

