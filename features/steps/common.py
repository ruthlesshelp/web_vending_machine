import time
from behave import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

SUBDIRECTORY = 'vending_machine'

@given("I am at the vending machine")
def visit_vending_machine(context):
    time.sleep(5)
    test_url = f"{context.base_url}/{SUBDIRECTORY}"
    context.driver.get(test_url)
    time.sleep(5)
    context.driver.implicitly_wait(3)

@given("I have inserted a quarter")
def insert_quarter(context):
    time.sleep(5)
    insert_button = context.driver.find_element(By.ID, "insert-btn")
    time.sleep(5)
    context.driver.implicitly_wait(3)
    time.sleep(5)
    insert_button.click()

@when("I purchase a product")
def buy_a_product(context):
    time.sleep(5)
    buy_button = context.driver.find_element(By.ID, "buy-btn")
    time.sleep(5)
    context.driver.implicitly_wait(3)
    time.sleep(5)
    buy_button.click()

@then("I should receive the product")
def assert_receive_product(context):
    time.sleep(5)
    message_element = context.driver.find_element(By.ID, "msg")
    time.sleep(5)
    context.driver.implicitly_wait(3)
    time.sleep(5)
    assert message_element.text == 'Enjoy!'
