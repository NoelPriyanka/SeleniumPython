from _ast import Assert
from tokenize import String

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

#serv_obj = Service("/usr/local/bin/chromedriver.exec")
#driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver.exec'))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
mywait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
print("Maximised the window")

ele = driver.find_element(By.XPATH, "//a[normalize-space()='Form Authentication']")
ele.click()

eid = driver.find_element(By.XPATH, "//input[@id='username']")
eid.send_keys("tomsmith")

pwd = driver.find_element(By.XPATH, "//input[@id='password']")
pwd.send_keys("SuperSecretPassword!")

btn = driver.find_element(By.XPATH, "//button[@type='submit']")
btn.click()


message = driver.find_element(By.XPATH, ("//h2[normalize-space()='Secure Area']"))
print(message.is_displayed())


logout = driver.find_element(By.XPATH, "//a[@class='button secondary radius']")
logout.click()
print("Application successfully logged out")

