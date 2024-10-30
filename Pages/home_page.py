"""Home Page, page object modeling"""
from selenium.webdriver.common.by import By
from Locators import home_page_locators as locators


class HomePage:
    """Home Page class to gather all functions"""
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_home_page(self):
        """Navigate to home page"""
        self.driver.get(locators.URL)

    def accept_all_cookies(self):
        """Click button accept all cookies"""
        accept_cookie_button = self.driver.find_element(By.XPATH, locators.ACCEPT_ALL_COOKIE_BUTTON)
        accept_cookie_button.click()

    def get_title(self):
        """Return home page tile"""
        return self.driver.title
