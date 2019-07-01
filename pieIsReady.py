# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

# PieIsReady

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from twilio.rest import Client

# Twilio account credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Run Firefox with no window
options = Options()
options.headless = True

url = 'https://www.microcenter.com/product/608187/4-model-b-4gb?src=raspberrypi'
driver = webdriver.Firefox(options=options)
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, features="lxml")

quantity = soup.find_all("div", class_="inventoryCnt")

meAndTheBoys = []

with open('quantity.txt', 'r+') as db:
      if quantity in db.read():
        sys.exit()
      else:
        db.write(quantity)
        for number in meAndTheBoys:
          message = client.messages \
            .create(
            body=quantity,
            from_='',
            to=number
            )
