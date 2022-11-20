import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# Login credentials
username = "patient"
password = "bluecheese"

# initializoing Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# head to login page
driver.get("https://democlinic.janeapp.com/login")
driver.maximize_window()
driver.implicitly_wait(60)

# Input username
driver.find_element(By.ID, "auth_key").send_keys(username)
time.sleep(3)

# Click next button
driver.find_element(By.CLASS_NAME, "no-wrap").click()
time.sleep(3)

# Input password
driver.find_element(By.ID, "password").send_keys(password)
time.sleep(3)

# Click login button
driver.find_element(By.XPATH, '//*[@id="log_in"]/span').click()
time.sleep(5)

# Sign-out
driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[2]/a').click()
time.sleep(2)

# close the driver
driver.close()