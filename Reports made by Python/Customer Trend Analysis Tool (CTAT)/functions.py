import pandas as pd

def process_excel(file_path):
    # Read the Excel file
    xls = pd.ExcelFile(file_path)
    
    # Get all sheet names
    sheet_names = xls.sheet_names
    
    # Process the first sheet
    df = pd.read_excel(xls, sheet_name=sheet_names[0])
    df = df.iloc[1:, :]  # Remove the first row
    
    # Process other sheets and append to the first sheet
    for sheet in sheet_names[1:]:
        temp_df = pd.read_excel(xls, sheet_name=sheet)
        df = pd.concat([df, temp_df], ignore_index=True)
    
    return df

# Usage example:
# result = process_excel('path/to/your/excel/file.xlsx')
# print(result)