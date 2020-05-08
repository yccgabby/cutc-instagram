from selenium import webdriver
import getpass
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

# if you want chrome window to run in the background, set as true; otherwise, set as false
headless = True

# Location of chromedriver, which helps navigate to web pages for automated testing of webapps
options = webdriver.ChromeOptions()
if headless:
    options.add_argument('headless')
chromedriver_path = "/Users/yccgabby/Desktop/chromedriver"  # copy and paste with your local path to chromedriver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
sleep(1)
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(1)

# gather keys needed to login from terminal
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
user = input('Please enter your username: ')
pswd = getpass.getpass('Please enter your password (input will be hidden): ')
username.send_keys(user)
password.send_keys(pswd)
sleep(3)

# discover the login button with above credentials to login
div = driver.find_element_by_css_selector('#react-root > section > main > div')
buttons = div.find_elements_by_css_selector('button')
sleep(1)
buttons[1].click()
sleep(3)

# optional git step to navigate away from popup asking about notifications
if not headless:
    notif_div = driver.find_elements_by_css_selector('body > div')
    sleep(2)
    print(len(notif_div))
    sleep(5)
    notif_buttons = notif_div[3].find_elements_by_css_selector('button')
    notif_buttons[1].click()