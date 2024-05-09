import time
import pandas as pd
import os
import glob
import time
from functools import wraps
from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service

# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import time
import datetime

print(datetime.datetime.now().strftime("%H:%M:%S"))

yoy_data = r"C:\My Folder\Python Projects\YoY Customer change\Input\yoy_data.csv"




service_obj = Service(
    "C:\\My Folder\\Python Projects\\Updating Dashboard\\chromedriver\\chromedriver.exe"
)

def retry(max_attempts=3, delay_seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts}/{max_attempts} failed: {e}")
                    time.sleep(delay_seconds)
            raise Exception(
                f"Function {func.__name__} failed after {max_attempts} attempts"
            )

        return wrapper

    return decorator


@retry(max_attempts=3, delay_seconds=1)
def yoy_data_grapper(starting_week, ending_week):
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(60)
    driver.get(
        "https://puro-analytics.cpggpc.ca/QvAJAXZfc/opendoc.htm?document=operations%5Cvolume%20tracker.qvw&lang=en-US&host=QVS%40ClusterPRD"
    )
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)
    # Depends on the window size that opens up, the below code will scroll to the right to find the required element
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='2']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "li[order='10']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='12']").click()
    time.sleep(5)


    # Find the element for the year 2023 and click on it
    #driver.find_element(By.CSS_SELECTOR, "div[title='2023']").click()
    
    # Hold down the Ctrl key
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).perform()
    
    # Click on the element for 2024 while Ctrl key is held down
    driver.find_element(By.CSS_SELECTOR, "div[title='2023']").click()
    
    # Release the Ctrl key
    webdriver.ActionChains(driver).key_up(Keys.CONTROL).perform()

    time.sleep(10)


    current_week = starting_week
    while current_week != ending_week+1:
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).perform()
        driver.find_element(By.CSS_SELECTOR, f"div[title='{current_week}']").click()
        current_week += 1

    
    webdriver.ActionChains(driver).key_up(Keys.CONTROL).perform()

    time.sleep(10)

    driver.find_element(By.CSS_SELECTOR, "div[title='Year']").click()
    time.sleep(2)
    #driver.find_element(By.CSS_SELECTOR, "div[title='Week']").click()
    #time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "div[title='MasterCLNTName']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "div[title='DestDivision']").click()
    time.sleep(5)
    #driver.find_element(By.CSS_SELECTOR, "div[title='DestinationTerminalName']").click()
    #time.sleep(3)
    #driver.find_element(By.CSS_SELECTOR, "div[title='DELIVERY STOPS']").click()
    #time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "div[title='Send to Excel']").click()
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    time.sleep(20)
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    wait = WebDriverWait(driver,5)
    wait.until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div[class='ModalDialog_Text']")
        )
    )
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    time.sleep(5)
    message = driver.find_element(By.CSS_SELECTOR, "div[class='ModalDialog_Text']").text
    time.sleep(5)
    home = os.path.expanduser("~")
    downloadspath = os.path.join(home, "Downloads")
    list_of_files = glob.glob(
        downloadspath + "\*.xlsx"
    )  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    # read excel file using pandas
    df = pd.read_excel(latest_file)
    df.to_csv(str(yoy_data))
    os.remove(latest_file)
    driver.quit()
    if ("The requested content has been opened in another window" in message) | (
        "Exporting" in message
    ):
        Flag = True
    else:
        Flag = False
    return Flag, df

