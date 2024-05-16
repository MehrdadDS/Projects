import win32com.client
import time
def refresh_pivot_table(file_path):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False  # You can set this to True if you want Excel to be visible while the script runs
    workbook = excel.Workbooks.Open(file_path)
    
    # Activate the workbook
    workbook.Activate()
    
    # Navigate to the "Data" tab
    #data_tab = workbook.Application.Worksheets("Data")
    #data_tab.Activate()
    
    # Refresh all data connections
    workbook.RefreshAll()
    time.sleep(15)

    # Save and close the workbook
    workbook.Save()
    workbook.Close()
    
    # Quit Excel
    excel.Quit()

