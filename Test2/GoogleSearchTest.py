from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest

class GoogleSearch(unittest.TestCase):
	#-> setUpClass, run only once before all the test methods
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

	#-> test method 1
	def test_search_avatar(self):
		self.driver.get('https://www.google.co.in')
		self.driver.find_element(By.NAME,"q").send_keys("Avatar")
		self.driver.find_element(By.NAME,"btnK").click()

	#-> test method 2
	def test_search_avengers(self):
		self.driver.get('https://www.google.co.in')
		self.driver.find_element(By.NAME,"q").send_keys("Avengers")
		self.driver.find_element(By.NAME,"btnK").click()

	#-> tearDownClass, run only once after all the test methods
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test completed")


