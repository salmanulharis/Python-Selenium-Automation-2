from selenium.webdriver.common.by import By

class LoginPage():

	def __init__(self, driver): #constructor
		self.driver = driver

		self.username_textbox_name = "username"
		self.password_textbox_name = "password"
		self.login_button_class    = "orangehrm-login-button"
		self.invalidUsername_message_class = "oxd-alert-content-text"

	def enter_username(self, username): #actions
		self.driver.find_element(By.NAME, self.username_textbox_name).clear()
		self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

	def enter_password(self, password): #actions
		self.driver.find_element(By.NAME, self.password_textbox_name).clear()
		self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

	def click_login(self): #actions
		self.driver.find_element(By.CLASS_NAME, self.login_button_class).click()

	def check_invalid_username_message(self, message):
		msg = self.driver.find_element(By.CLASS_NAME, self.invalidUsername_message_class).text
		return msg
