from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_page_load_timeout(10)

driver.get('https://www.google.co.in')
driver.find_element(By.NAME,"q").send_keys("Avatar")
# driver.find_element(By.NAME,"btnK").click() # normal way to click
# driver.find_element(By.NAME,"btnK").send_keys(Keys.RETURN) # if normal click dont work because the element is not visisble
button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"btnK")))
button.click()
time.sleep(4)

driver.quit()
print("success")

