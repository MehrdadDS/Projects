import time
import pandas as pd
import os
import glob


from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service

# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

# from seleniumbase import BaseCase

# Important: the file should be already in the folder

""" Upload Files' Paths"""
courierops_path = r"C:\Users\ramy.abdallah\Documents\1- Forecasting Files\6- First P&D Forecast Run-Jan 2023\P&D Forecast - Ramy\Python Projects\Updating Dashboard\Output\courierops_actuals - daily.csv"
# amz_path = r"C:\Users\ramy.abdallah\Documents\1- Forecasting Files\6- First P&D Forecast Run-Jan 2023\P&D Forecast - Ramy\Python Projects\Updating Dashboard\Output\amazon_actuals - daily.csv"
# amz_returns_path = r"C:\Users\ramy.abdallah\Documents\1- Forecasting Files\6- First P&D Forecast Run-Jan 2023\P&D Forecast - Ramy\Python Projects\Updating Dashboard\Output\amazon_returns - daily.csv"


# Provide the path to chromerdriver.exe
service_obj = Service(
    r"C:\My Folder\Python Projects\Updating Dashboard\chromedriver\chromedriver.exe"
)

# default_path = "https://purolator.sharepoint.com/sites/OperationsNetworkStrategy/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FOperationsNetworkStrategy%2FShared%20Documents%2FGeneral%2FInput%20Files&FolderCTID=0x0120002727444D25BE7A439A019F470AE463B5&View=%7B1EB84C9E%2DEFC8%2D425B%2D9C4A%2DE674F8C68EB5%7D"
# default_path = "https://purolator.sharepoint.com/sites/OperationsForecasts774/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FOperationsForecasts774%2FShared%20Documents%2FControl%20Group%20Customers%20Analysis%2FInput&FolderCTID=0x012000BF452146D7E287498242E01157DDD1F5&View=%7B2AF703EF%2D20A0%2D4D49%2D8E57%2DF40DF650E6BE%7D"



def teamFileUpload(file_path1, file_path2,file_path3):
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(30)
    # 30 seconds is max time out.. 2 seconds (3 seconds save)
    driver.get(
        "https://purolator.sharepoint.com/sites/OperationsForecasts774/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FOperationsForecasts774%2FShared%20Documents%2FControl%20Group%20Customers%20Analysis%2FInput&FolderCTID=0x012000BF452146D7E287498242E01157DDD1F5"
    )
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(
        "mehrdad.dadgar@purolator.com"
    )
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='idBtn_Back']").click()
    time.sleep(4)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(
        By.XPATH, "//a[@aria-label='Click or enter to return to classic SharePoint']"
    ).click()
    time.sleep(5)
    driver.find_element(
        By.XPATH, "//img[@title='Control Group Customers Analysis']"
    ).click()
    driver.find_element(By.XPATH, "//img[@title='Input']").click()
    driver.find_element(By.ID, "QCB1_Button2").click()
    time.sleep(1.5)
    winHandleBefore = driver.window_handles[0]
    iframe = driver.find_element(By.XPATH, "//iframe[@class='ms-dlgFrame']")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, "ctl00_PlaceHolderMain_ctl02_ctl04_InputFile").send_keys(
        file_path1
    )
    driver.find_element(By.ID, "ctl00_PlaceHolderMain_ctl02_ctl04_InputFile").send_keys(
        file_path2
    )
    driver.find_element(By.ID, "ctl00_PlaceHolderMain_ctl02_ctl04_InputFile").send_keys(
        file_path3
    )
    driver.find_element(
        By.ID, "ctl00_PlaceHolderMain_ctl02_ctl04_OverwriteSingle"
    ).click()
    driver.find_element(By.XPATH, "//input[@value='OK']").click()
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "//input[@id='ms-conflictDlgDoRest']").click()
    driver.find_element(By.XPATH, "//button[@id='ms-conflictDlgReplaceBtn']").click()
    wait = WebDriverWait(driver, 180)
    wait.until(expected_conditions.presence_of_element_located((By.ID, "QCB1_Button2")))
    # Upload time
    time.sleep(65)
    driver.quit()
    return print("File Uploaded Successfully")


#teamFileUpload(file_path1=default_path)
