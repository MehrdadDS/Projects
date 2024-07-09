import pandas as pd
import numpy as np

def classify_clients_based_volumes(db, plus_threshold=50000, minus_threshold=-50000):
    # Step 1: Identify the latest week available in 2024
    latest_week_2024 = db[db['Year'] == 2024]['Week'].max()

    # Step 2: Calculate the YTD pieces for each client for the same number of weeks in 2023 and 2024
    db_2023 = db[(db['Year'] == 2023) & (db['Week'] <= latest_week_2024)]
    db_2024 = db[db['Year'] == 2024]

    ytd_2023 = db_2023.groupby('Master Client')['Pieces'].sum().rename('YTD 2023')
    ytd_2024 = db_2024.groupby('Master Client')['Pieces'].sum().rename('YTD 2024')

    # Step 3: Compute the YTD change for each client
    ytd_change = ytd_2024.subtract(ytd_2023, fill_value=0).rename('YTD Change')
    df_changes = pd.DataFrame(ytd_change).reset_index()
    df_changes.to_csv('Inclinersordecliners.csv',index=False)
    # Step 4: Classify clients into groups based on the YTD change
    def classify_client(change):
        if change > plus_threshold:
            return 'Group A'
        elif change < minus_threshold:
            return 'Group B'
        else:
            return 'Group C'

    ytd_change_classified = ytd_change.apply(classify_client).rename('Group')

    # Step 5: Merge the classification back into the original dataframe
    db = db.merge(ytd_change_classified, left_on='Master Client', right_index=True, how='left')

    return db

import pandas as pd

def classify_clients_sorted(db, top_increase=20, top_decline=15):
    # Step 1: Identify the latest week available in 2024
    latest_week_2024 = db[db['Year'] == 2024]['Week'].max()

    # Step 2: Calculate the YTD pieces for each client for the same number of weeks in 2023 and 2024
    db_2023 = db[(db['Year'] == 2023) & (db['Week'] <= latest_week_2024)]
    db_2024 = db[db['Year'] == 2024]

    ytd_2023 = db_2023.groupby('Master Client')['Pieces'].sum().rename('YTD 2023')
    ytd_2024 = db_2024.groupby('Master Client')['Pieces'].sum().rename('YTD 2024')

    # Step 3: Compute the YTD change for each client
    ytd_change = ytd_2024.subtract(ytd_2023, fill_value=0).rename('YTD Change')
    
    df_changes = pd.DataFrame(ytd_change).reset_index()
    df_changes.to_csv('Inclinersordecliners_basedontop.csv',index=False)
    # Step 4: Sort clients based on YTD change from biggest increase to biggest decline
    sorted_clients = ytd_change.sort_values(ascending=False)

    # Step 5: Classify clients into groups A, B, and C based on sorted YTD change
    top_increase_clients = sorted_clients.head(top_increase).index
    top_decline_clients = sorted_clients.tail(top_decline).index
    all_clients = sorted_clients.index

    group_dict = {}

    for client in all_clients:
        if client in top_increase_clients:
            group_dict[client] = 'Top 30 incliners'
        elif client in top_decline_clients:
            group_dict[client] = 'Top 30 decliners'
        else:
            group_dict[client] = 'Moderate Performers'

    # Step 6: Merge the classification back into the original dataframe
    db['Group'] = db['Master Client'].map(group_dict).fillna('Moderate Performers')

    return db




import pandas as pd
import numpy as np

def calculate_ytd_changes(db):
    # Step 1: Identify the latest week available in 2024
    latest_week_2024 = db[db['Year'] == 2024]['Week'].max()

    # Step 2: Calculate the YTD pieces for each client for the same number of weeks in 2023 and 2024
    db_2023 = db[(db['Year'] == 2023) & (db['Week'] <= latest_week_2024)]
    db_2024 = db[db['Year'] == 2024]

    # Group by 'Master Client', 'Tier', and 'Group', and sum the 'Pieces'
    ytd_2023 = db_2023.groupby(['Master Client', 'Tier', 'Group'])['Pieces'].sum().rename('YTD 2023')
    ytd_2024 = db_2024.groupby(['Master Client', 'Tier', 'Group'])['Pieces'].sum().rename('YTD 2024')

    # Step 3: Combine the results into a single dataframe
    df_combined = pd.concat([ytd_2023, ytd_2024], axis=1).reset_index()

    # Step 4: Replace NaN values in YTD 2023 with 0
    df_combined['YTD 2023'] = df_combined['YTD 2023'].fillna(0)

    # Step 5: Compute the YTD change and percentage change for each client
    df_combined['YTD Change'] = df_combined['YTD 2024'] - df_combined['YTD 2023']
    
    # Calculate percentage change, handling division by zero
    df_combined['YTD % Change'] = np.where(
        df_combined['YTD 2023'] != 0,
        (df_combined['YTD 2024'] / df_combined['YTD 2023'] - 1) * 100,
        100  # or you could use np.nan if you prefer
    )

    # Round the percentage change to 2 decimal places
    df_combined['YTD % Change'] = df_combined['YTD % Change'].round(2)

    # Step 6: Save the results to a CSV file
    #df_combined.to_csv('Inclinersordecliners_basedontop.csv', index=False)

    return df_combined
