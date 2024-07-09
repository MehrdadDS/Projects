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

eid_path = r"C:\My Folder\Python Projects\Updating CG Dashboard\Input\CG EID actuals daily.csv"
edd_path = r"C:\My Folder\Python Projects\Updating CG Dashboard\Input\CG EDD actuals daily.csv"
pi_path  = r"C:\My Folder\Github\Automated dashboards\Updating CG dashboard\Output\PI EDD actuals.csv"


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
def ControlGroupEIDDataGrapper():
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(60)
    driver.get(
        "https://puro-analytics.cpggpc.ca/QvAJAXZfc/opendoc.htm?document=operations%5Cvolume%20tracker.qvw&lang=en-US&host=QVS%40ClusterPRD"
    )
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)
    # Depends on the window size that opens up, the below code will scroll to the right to find the required element
    # driver.find_element(By.CSS_SELECTOR, "a[class='qvtr-scroll-right']").click()
    # driver.find_element(By.CSS_SELECTOR, "a[class='qvtr-scroll-right']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='2']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div[title='2024']").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "div[class='QvFrame Document_BU38']").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, "li[order='10']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='12']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div[title='ExpectedInductionDate']").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, "div[title='MasterCLNTName']").click()
    time.sleep(6)
    driver.find_element(By.CSS_SELECTOR, "div[title='OriginDepotID']").click()
    time.sleep(5)
    #driver.find_element(By.CSS_SELECTOR, "div[title='DELIVERY PIECES']").click()
    #time.sleep(3)
    #driver.find_element(By.CSS_SELECTOR, "div[title='DELIVERY STOPS']").click()
    #time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "div[title='Send to Excel']").click()
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    time.sleep(35)
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    wait = WebDriverWait(driver,5)
    wait.until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div[class='ModalDialog_Text']")
        )
    )
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    time.sleep(10)
    message = driver.find_element(By.CSS_SELECTOR, "div[class='ModalDialog_Text']").text
    time.sleep(15)
    home = os.path.expanduser("~")
    downloadspath = os.path.join(home, "Downloads")
    list_of_files = glob.glob(
        downloadspath + "\*.xlsx"
    )  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    # read excel file using pandas
    df = pd.read_excel(latest_file)
    df.to_csv(str(eid_path))
    os.remove(latest_file)
    driver.quit()
    if ("The requested content has been opened in another window" in message) | (
        "Exporting" in message
    ):
        Flag = True
    else:
        Flag = False
    return Flag, df



@retry(max_attempts=3, delay_seconds=1)
def ControlGroupEDDDataGrapper():
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(60)
    driver.get(
        "https://puro-analytics.cpggpc.ca/QvAJAXZfc/opendoc.htm?document=operations%5Cvolume%20tracker.qvw&lang=en-US&host=QVS%40ClusterPRD"
    )
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)
    # Depends on the window size that opens up, the below code will scroll to the right to find the required element
    # driver.find_element(By.CSS_SELECTOR, "a[class='qvtr-scroll-right']").click()
    # driver.find_element(By.CSS_SELECTOR, "a[class='qvtr-scroll-right']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='2']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div[title='2024']").click()

    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "div[class='QvFrame Document_BU38']").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, "li[order='10']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='12']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div[title='ExpectedDeliveryDate']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div[title='MasterCLNTName']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div[title='DestDepotID']").click()
    time.sleep(10)
    #driver.find_element(By.CSS_SELECTOR, "div[title='DELIVERY PIECES']").click()
    #time.sleep(3)
    #driver.find_element(By.CSS_SELECTOR, "div[title='DELIVERY STOPS']").click()
    #time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "div[title='Send to Excel']").click()
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    time.sleep(50)#160
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    wait = WebDriverWait(driver, 10)
    wait.until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div[class='ModalDialog_Text']")
        )
    )
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    time.sleep(3)
    message = driver.find_element(By.CSS_SELECTOR, "div[class='ModalDialog_Text']").text
    time.sleep(5)
    home = os.path.expanduser("~")
    downloadspath = os.path.join(home, "Downloads")
    list_of_files = glob.glob(
        downloadspath + "\*.xlsx"
    )  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    # read excel file using pandas
    df = pd.read_excel(latest_file)
    time.sleep(20)

    print(latest_file)
    df.to_csv(str(edd_path))
    driver.quit()


##  #############
    print("EDD columns : {}",df.columns)

    df = df.iloc[1:,:]
    df['Expected Delivery Date']  = pd.to_datetime(df['Expected Delivery Date'])
    df = df[df['Expected Delivery Date'] >="2023-01-01"]

    df.to_csv(edd_path,index=False)
####    ##########
    if ("The requested content has been opened in another window" in message) | (
        "Exporting" in message
    ):
        Flag = True
    else:
        Flag = False
    return Flag, df



@retry(max_attempts=3, delay_seconds=1)
def PIDataGrapper():
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(60)
    driver.get(
        "https://puro-analytics.cpggpc.ca/QvAJAXZfc/opendoc.htm?document=operations%5Cvolume%20tracker.qvw&lang=en-US&host=QVS%40ClusterPRD"
    )
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)
    # Depends on the window size that opens up, the below code will scroll to the right to find the required element
    # driver.find_element(By.CSS_SELECTOR, "a[class='qvtr-scroll-right']").click()
    # driver.find_element(By.CSS_SELECTOR, "a[class='qvtr-scroll-right']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='2']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div[title='2024']").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "li[order='10']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "li[order='12']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div[title='ExpectedDeliveryDate']").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, "div[title='DestDepotID']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div[title='CompanyCode']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div[title='PR02']").click()
    time.sleep(3)

    #driver.find_element(By.CSS_SELECTOR, "div[title='DELIVERY STOPS']").click()
    #time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "div[title='Send to Excel']").click()
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    time.sleep(35)
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    wait = WebDriverWait(driver,5)
    wait.until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div[class='ModalDialog_Text']")
        )
    )
    print(datetime.datetime.now().strftime("%H:%M:%S"))

    time.sleep(10)
    message = driver.find_element(By.CSS_SELECTOR, "div[class='ModalDialog_Text']").text
    time.sleep(15)
    home = os.path.expanduser("~")
    downloadspath = os.path.join(home, "Downloads")
    list_of_files = glob.glob(
        downloadspath + "\*.xlsx"
    )  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    # read excel file using pandas
    df = pd.read_excel(latest_file)
    df.to_csv(str(eid_path))
    os.remove(latest_file)
    driver.quit()


    ######
    print("pi columns : {}",pi.columns)

    pi = pi.iloc[1:,:]
    pi['Expected Delivery Date']  = pd.to_datetime(pi['Expected Delivery Date'])
    pi.insert(1,'Master Client',"PI Customers")
    pi = pi[pi['Expected Delivery Date'] >="2023-01-01"]

    pi.to_csv(pi_path,index=False)

    ######


    if ("The requested content has been opened in another window" in message) | (
        "Exporting" in message
    ):
        Flag = True
    else:
        Flag = False
    return Flag, df

