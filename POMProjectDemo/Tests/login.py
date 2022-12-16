from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(4)

driver.close()
driver.quit()
print("Test Complete");
