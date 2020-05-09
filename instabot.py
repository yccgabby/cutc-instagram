from instapy import InstaPy
from instapy import smart_run
import getpass

# Get username and password from stdin 
usr = input('Please enter your username: ')
pswd = getpass.getpass('Please enter your password (input will be hidden): ')

# start a instagram browser session
session = InstaPy(username=usr,password=pswd,headless_browser=True)