import pandas as pd

def aggregate_excel_sheets(file_path):
    # Read both sheets into pandas dataframes
    sheet1 = pd.read_excel(file_path, sheet_name=0)  # Assuming the first sheet is indexed at 0
    sheet2 = pd.read_excel(file_path, sheet_name=1, header=None)  # Assuming the second sheet has no header
    sheet2.columns = sheet1.columns
    # Concatenate the dataframes vertically
    aggregated_data = pd.concat([sheet1, sheet2], ignore_index=True,axis=0)

    return aggregated_data

