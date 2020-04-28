from selenium import webdriver
import getpass
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

# Location of chromedriver, which helps navigate to web pages for automated testing of webapps
options = webdriver.ChromeOptions()
options.add_argument('headless')
chromedriver_path = "/Users/yccgabby/Desktop/chromedriver" # copy and paste with your local path to chromedriver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
sleep(3)
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

# gather keys needed to login from terminal
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
user = input('Please enter your username: ')
pswd = getpass.getpass('Please enter your password (input will be hidden): ')
username.send_keys(user)
password.send_keys(pswd)

# discover the login button with above credentials to login
login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
login_button.click()
sleep(3)

# optional step to navigate away from popup asking about notifications (better solution is to disable popups on chrome)
notif = driver.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > '
                                            'button.aOOlW.HoLwm')
notif.click()




