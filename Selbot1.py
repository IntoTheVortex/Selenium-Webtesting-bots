# This is a simple bot to log in to Powells.com
# It requires selenium and Chrome webdriver

from selenium import webdriver
import time

# Set browser equal to webdriver.Chrome
browser = webdriver.Chrome()

# Initialize the browser with the URL
browser.get('https://www.powells.com')

# Locates the Login button on the home page and clicks it
login_element = browser.find_element_by_css_selector('a[id="dnn_dnnLogin_loginLink"]')
login_element.click()

time.sleep(3)

# This section enters the login credentials
# Enter your own credentials or import them in a text file
login_email_element = browser.find_element_by_css_selector('input[id="txtUserNameSignIn"]')
login_email_element.send_keys('loginemail@email.com')  # Enter your login email
login_password_element = browser.find_element_by_css_selector('input[id="txtPasswordSignIn"]')
login_password_element.send_keys('thepassword')  # Enter your login password

login_button = browser.find_element_by_css_selector('input[id="dnn_ctr3187_CustomerSignIn_btnLogin"]')
login_button.click()
