# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

# PieIsReady

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

# Twilio account credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Run Firefox with no window
options = Options()
options.headless = True

url = ''
driver = webdriver.Firefox(options=options)
driver.get(url)
