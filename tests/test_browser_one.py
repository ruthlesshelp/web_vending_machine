from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By

SUBDIRECTORY = 'vending_machine'

# See: Behavior-Driven Development(BDD) Testing
# Writing and running BDD tests using Behave
# https://www.jetbrains.com/guide/django/tutorials/django-aws/bdd-behave/

class TestBrowserOne(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.server_url = f"{self.live_server_url}/{SUBDIRECTORY}/"
        print(f'server_url={self.server_url}')
        self.browser.get(self.server_url)

    def tearDown(self):
        self.browser.quit()

    # Given: I am at the vending machine
    def test_given_vending_machine(self):
        """I have inserted a quarter."""
        # Arrange

        # Act
        actual_title = self.browser.title
        print(f'actual_title={actual_title}')

        # Assert
        assert "Vending Machine" in actual_title
