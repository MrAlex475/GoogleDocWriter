import time
from builtins import int, range
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("Docs URL")

time.sleep(2)

def type(keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    actions.perform()

def makeStyle(style):
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(style).key_up(Keys.CONTROL).key_up(Keys.ALT)
    actions.perform()

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)

for single_date in daterange(start_date, end_date):
    date = single_date.strftime("%d %b %Y")

    type(f'@{date}')
    time.sleep(0.5)
    type(Keys.ENTER)

    makeStyle("5")

    type(Keys.ENTER)
    makeStyle("0")
    type(Keys.ENTER)

time.sleep(2)
