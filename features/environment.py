import time
from selenium import webdriver

SUBDIRECTORY = 'vending_machine'

def before_all(context):
    context.driver = webdriver.Chrome()
    test_url = f"{context.base_url}/{SUBDIRECTORY}"
    context.driver.get(test_url)
    context.driver.implicitly_wait(3)
    time.sleep(5)

def before_scenario(context, scenario):
    pass

def before_step(context, scenario):
    pass

def after_scenario(context, scenario):
    pass

def after_all(context):
    time.sleep(5)
    context.driver.quit()