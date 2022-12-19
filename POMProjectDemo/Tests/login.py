from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import time
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

	def test_login_valid(self):
		driver = self.driver
		driver.get('https://opensource-demo.orangehrmlive.com/')

		# Login Test
		login = LoginPage(driver) # creating login page object
		login.enter_username('Admin')
		login.enter_password('admin123')
		login.click_login()

		# Logout test
		homepage = HomePage(driver)
		homepage.click_welcome()
		homepage.click_logout()

		time.sleep(4)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Complete");

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports/test_login_valid'))