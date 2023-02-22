from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


# serv_obj = Service("/usr/local/bin/chromedriver.exec")
# driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver.exec'))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.implicitly_wait(10)
mywait = WebDriverWait(driver, 10)
driver.get("https://example.cypress.io/commands/querying")
driver.maximize_window()
print("Maximised the window")

# Get command functions

btn = driver.find_elements(By.ID, 'query-btn')
btn = driver.find_elements(By.CLASS_NAME, 'query-btn')
print("Button is identified")


# Contains

fruit = driver.find_elements(By.XPATH, "//*[contains('.query-list', 'bananas')]")
print("Query list contains banana")
