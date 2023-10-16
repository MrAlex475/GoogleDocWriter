import time
from builtins import int, range
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# The Google Docs URL to open - To avoid needing to auth I set it to editable by others with the link
driver.get("Docs URL")

# Small sleep to allow the doc to load and be ready
time.sleep(2)

def type(keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    actions.perform()

# Send the shortcut to format the text to a certain style (H1, H2, Body)
def makeStyle(style):
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(style).key_up(Keys.CONTROL).key_up(Keys.ALT)
    actions.perform()

# Create a date range between two dates - Note: it isn't last date inclusive
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2024, 1, 1)
end_date = date(2025, 1, 1)

for single_date in daterange(start_date, end_date):
    # Format the date to match the Smart Chip format of google docs Data Chip
    # September - Sep is not the correct format, Sept is the Google Chip format
    date = single_date.strftime("%d %b %Y").replace("Sep", "Sept")

    type(f'@{date}')
    # Sleep to let dialog open
    time.sleep(0.5)
    type(Keys.ENTER)

    makeStyle("5")

    type(Keys.ENTER)
    makeStyle("0")
    type(Keys.ENTER)

# Allow time for the doc to save after all edits are made
time.sleep(2)
